#!/usr/bin/env bash

set -eo pipefail

cd ${SOURCE_DIR}
git config --list
date > blap.txt
git status --short
git add .
git commit -m "Update from: ${UPDATED_FROM}"
git push -u origin main