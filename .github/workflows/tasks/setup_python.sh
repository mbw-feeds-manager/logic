#!/usr/bin/env bash

set -eo pipefail
apt-get update
apt-get install -y --no-install-recommends python3 python3-pip
ln -sf /usr/bin/python3 /usr/bin/python
ln -sf /usr/bin/pip3 /usr/bin/pip