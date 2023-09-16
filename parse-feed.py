import sys
import json

from argsy import Argsy

from shared_functions import parse_feed_to_dict  


ARG_DEF=Argsy(config_str="""
program:
  name: parse-feed.py
  description: Parse a feed.
  args:
    feed-url:
      cmd_type: option
      flags: '-f|--feed-url'
      help: "The URL of the feed to parse."
      required: true
""")


def main():
    args=ARG_DEF.parse_args(args=sys.argv[1:]).get('args')
    feed_url=args.get('feed_url')
    print(json.dumps(parse_feed_to_dict(feed_url), indent=4))

if __name__ == '__main__':
    main()