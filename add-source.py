import json
import sys
from uuid import uuid4

from argsy import Argsy


ARG_DEF=Argsy(config_str="""
program:
  name: add-source.py
  description: Add a source.
  args:
    name:
      cmd_type: option
      flags: '-n|--name'
      help: "The name of the source."
      required: true
    url:
      cmd_type: option
      flags: '-u|--url'
      help: "The URL of the source."
      required: true
    description:
      cmd_type: option
      flags: '-d|--description'
      help: "The description of the source."
      required: false           
""")


CFG = dict()
DERIVED_CFG = dict()

with open('config.json', 'r') as config_file:
    CFG = json.load(config_file)
    DERIVED_CFG["sources_path"] = f'{CFG["data_base_dir"]}/{CFG["data_store_dir"]}/sources.json'
    DERIVED_CFG["feed_latest_path"] = f'{CFG["data_base_dir"]}/{CFG["data_store_dir"]}/latest.json'
    DERIVED_CFG["staging_dir"] = f'{CFG["data_base_dir"]}/{CFG["data_staging_dir"]}'
    DERIVED_CFG["store_dir"] = f'{CFG["data_base_dir"]}/{CFG["data_store_dir"]}'




def add_source(name: str, url: str, description: str) -> None:
    data_path = DERIVED_CFG.get('sources_path')
    data = []
    with open(data_path, 'r') as sources_file:
         data = json.load(sources_file)

    data.append(dict(
        id = str(uuid4().hex),
        name = name,
        url = url,
        description = description,
        state = 'active'
    ))

    with open(data_path, 'w') as sources_file:
        json.dump(data, sources_file, indent=2)

def main():
    args = ARG_DEF.parse_args(args=sys.argv[1:]).get('args')
    add_source(
        name = args.get('name'),
        url = args.get('url'),
        description = args.get('description')
    )
    


if __name__ == '__main__':
    main()