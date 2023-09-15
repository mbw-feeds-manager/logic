import sys
import json

import feedparser

from argsy import Argsy


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


def parse_feed_to_json(feed_url):
    # Parse the RSS or Atom feed
    feed = feedparser.parse(feed_url)

    # Create a list to store the feed items
    feed_items = []

    # Loop through the entries in the feed
    for entry in feed.entries:
        item = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary,
        }
        feed_items.append(item)

    # Create a dictionary to store the feed metadata
    feed_info = {
        'feed_title': feed.feed.title,
        'feed_link': feed.feed.link,
        # 'feed_description': feed.feed.description,
    }

    # Create a dictionary to store the entire feed data
    feed_data = {
        'feed_info': feed_info,
        'feed_items': feed_items,
    }

    # Convert the feed data to JSON
    json_data = json.dumps(feed_data, indent=4)

    return json_data


def main():
    args=ARG_DEF.parse_args(args=sys.argv[1:]).get('args')
    feed_url=args.get('feed_url')
    print(parse_feed_to_json(feed_url))



if __name__ == '__main__':
    main()