import os

import paramiko

def get_ssh_banner(hostname, port=22, timeout=5):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, port=port, username='spurs', password='',
                       look_for_keys=False, allow_agent=False, timeout=timeout)
    except paramiko.ssh_exception.AuthenticationException:
        return client._transport.get_banner()
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    target = os.environ.get("SPURS_TARGET", "127.0.0.1")
    print(get_ssh_banner(target))
