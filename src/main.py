import asyncio
# import time
from config.loader import load_config
from utils.fetcher import fetch_stories_by_keywords
from utils.saver import save_results_to_file
from display.output import display_stories

async def main():
    config_file = "config/config.yaml"
    config = load_config(config_file)

    # Extract settings from config
    keywords = config.get('keywords', ['math'])
    settings = config.get('settings', {})
    max_stories = settings.get('max_stories_to_check', 100)
    concurrent_connections = settings.get('concurrent_connections', 50)
    save_results = settings.get('save_results', False)
    results_file = settings.get('results_file', 'hn_search_results.json')
    output_config = config.get('output', {})

    print(f"=" * 32)
    print(f"Hacker News Multi-Keyword Search")
    print(f"=" * 32)

    # start_time = time.time()
    stories = await fetch_stories_by_keywords(keywords, max_stories, concurrent_connections)
    # end_time = time.time()
    # print(f"Search completed in {end_time - start_time:.2f} seconds")
    print(f"Found {len(stories)} stories matching keywords: {', '.join(keywords)}")
    display_stories(stories, output_config)


    if save_results and stories:
        save_results_to_file(stories, results_file)


if __name__ == "__main__":
    asyncio.run(main())