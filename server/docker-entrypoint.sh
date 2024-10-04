#!/bin/sh
set -e

USER_ID=${LOCAL_USER_ID:-1000}
usermod -u $USER_ID  nonroot
chown -R nonroot ./

exec /usr/local/bin/pysu nonroot "$@"