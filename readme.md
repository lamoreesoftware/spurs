Put the spurs to a macOS system that is currently locked. 

## Setup

It may make sense for you to create a Spurs user to unlock the system after boot. Consider the following:

```shell
spurs_group="spurs"
spurs_gid=401
spurs_username="spurs"
spurs_uid=401
spurs_password="$(OP_ACCOUNT=account op read 'op://vault/item/password')"
spurs_fullname="Spurs User"

sudo dseditgroup -o create -i "$spurs_gid" "$spurs_group"

sudo sysadminctl -addUser "$spurs_username" -fullName "$spurs_fullname" \
  -UID "$spurs_uid" -GID "$spurs_gid" -shell /bin/sh -home /var/empty -password "$spurs_password"

sudo sysadminctl interactive -secureTokenOn "$spurs_username" -password "$spurs_password"

sudo dscl . create "/Users/$spurs_username" IsHidden 1
```

## Cleanup

```shell
spurs_group="spurs"
spurs_username="spurs"

sudo sysadminctl -deleteUser "$spurs_username"
sudo dseditgroup -o delete "$spurs_group"
```
