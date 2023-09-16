#!/usr/bin/env bash

function main {

  local staging_dir="${1}"
  local store_dir="${2}"

  if [[ -z "${staging_dir}" ]]; then
    echo "Data staging directory is not set"
    exit 1
  fi 

  if [[ -z "${store_dir}" ]]; then
    echo "Data store directory is not set"
    exit 1
  fi

  for i in $(ls ${staging_dir}); do 
    mkdir -p "${store_dir}/${i}"
    cp -r "${staging_dir}/${i}"/* "${store_dir}/${i}"
  done

}
main "${@}"