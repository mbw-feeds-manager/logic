import hashlib
import json
import os
import requests

from shared_functions import parse_feed_to_dict

CFG = dict()
DERIVED_CFG = dict()

with open('config.json', 'r') as config_file:
    CFG = json.load(config_file)
    DERIVED_CFG["sources_path"] = f'{CFG["data_base_dir"]}/{CFG["data_store_dir"]}/sources.json'
    DERIVED_CFG["feed_latest_path"] = f'{CFG["data_base_dir"]}/{CFG["data_store_dir"]}/latest.json'
    DERIVED_CFG["staging_dir"] = f'{CFG["data_base_dir"]}/{CFG["data_staging_dir"]}'
    DERIVED_CFG["store_dir"] = f'{CFG["data_base_dir"]}/{CFG["data_store_dir"]}'



def create_article_hash(article: dict) -> str:
    """Create a hash for the article."""
    hash = hashlib.md5()
    hash.update(json.dumps(article).encode("utf-8"))
    return hash.hexdigest()


def load_sources(sources_path: str, is_local=False) -> list:
    """Load the sources from the sources file."""

    if is_local:
        with open(sources_path, "r") as sources_file:
            sources = json.load(sources_file)
    else:
        sources = requests.get(sources_path).json()

    return sources


def make_dir(new_dir: str):
    """Create a new directory if it doesn't already exist."""
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print(f"Directory '{new_dir}' created successfully.")
    else:
        print(f"Directory '{new_dir}' already exists.")


def main():
    feed_sources = load_sources(
        sources_path=DERIVED_CFG["sources_path"],
        is_local=CFG["is_local_data"],
    )

    for feed_source in feed_sources:
        feed_source_dir = f'{DERIVED_CFG["staging_dir"]}/{feed_source.get("id")}'
        make_dir(feed_source_dir)

        feed_dict = parse_feed_to_dict(requests.get(feed_source.get("url")).text)
        latest_feed_items = []

        for feed in feed_dict.get("feed_items"):
            feed_hash = create_article_hash(feed)

            feed.update(
                {
                    "source_id": feed_source.get("id"),
                    "feed_hash": feed_hash,
                }
            )
            latest_feed_items.append(feed)

            # Save the article to the staging directory
            with open(
                f'{feed_source_dir}/{feed_hash}.json', "w"
            ) as feed_file:
                json.dump(feed, feed_file, indent=2)

            # Save the latest feed items to the staging directory
            with open(
                f'{feed_source_dir}/latest.json', "w"
            ) as latest_feed_file:
                json.dump(latest_feed_items, latest_feed_file, indent=2)



if __name__ == "__main__":
    main()
