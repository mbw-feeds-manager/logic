import json
import feedparser

def parse_feed_to_dict(feed_url) -> dict:
    """Parse a feed and return the data as JSON."""

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

    return feed_data

    # # Convert the feed data to JSON
    # json_data = json.dumps(feed_data, indent=4)

    # return json_data



