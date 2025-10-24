import os
import time

import paramiko

def check_for_locked_system(hostname, port=22, timeout=5):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username="none", password="none",
                       look_for_keys=False, allow_agent=False, timeout=timeout)
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        try:
            banner = str(client._transport.get_banner(), encoding="utf-8")
            if "This system is locked" in banner:
                return True
        except TypeError:
            # The banner content isn't available for some reason
            return False
        finally:
            client.close()
        return False


def unlock_system(hostname, username, password, port=22, timeout=5):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password, timeout=timeout)
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        # We don't actually get a shell after successful authentication
        pass
    finally:
        client.close()


if __name__ == "__main__":
    target = os.environ.get("SPURS_TARGET", "127.0.0.1")
    username = os.environ.get("SPURS_USERNAME", "spurs")
    password = os.environ.get("SPURS_PASSWORD", "")
    if check_for_locked_system(target):
        unlock_system(target, username, password)
