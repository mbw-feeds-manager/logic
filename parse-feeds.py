import hashlib
import json
import requests

from shared_functions import parse_feed_to_dict

CFG=dict(
    data_is_local = True,
    data_path = '/Users/matt/Codespace/mbw-feeds-manager/data/feature/initial-data-model/data/sources.json'
)


def create_article_hash(article: dict) -> str:
    hash = hashlib.md5()
    hash.update(json.dumps(article).encode('utf-8'))
    return hash.hexdigest()


def load_sources(sources_path: str, is_local = False) ->  list:
    """Load the sources from the sources file."""

    if is_local:
        with open(sources_path, 'r') as sources_file:
            sources = json.load(sources_file)
    else:
        sources = requests.get(sources_path).json()

    return sources


def main():

    sources = load_sources(
        sources_path = CFG["data_path"],
        is_local = CFG["data_is_local"]
    )

    for source in sources:
        feed_url = source['url']
        json_data = parse_feed_to_dict(feed_url)
        
        for article in json_data.get('feed_items'):
          hash = create_article_hash(article)
          print(f'{hash} : {article.get("title")}')
        

if __name__ == '__main__':
    main()