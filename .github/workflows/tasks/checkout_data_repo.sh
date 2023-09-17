#!/usr/bin/env bash

set -eo pipefail
git clone "https://x-access-token:${TOKEN}@github.com/mbw-feeds-manager/data.git" "${CLONE_TARGET_DIR}"
cd "${CLONE_TARGET_DIR}"
git config user.name "Matt Wiley"
git config user.email "mattwiley+github@fastmail.com"
cd data_store
ls -la
pwd