from utils.formatter import format_timestamp

def display_stories(stories, output_config):
    if not stories:
        print("No matching stories found.")
        return

    print(f"\nFound {len(stories)} matching stories:\n")

    for i, story in enumerate(stories, 1):
        print(f"Story #{i}")

        if output_config.get('show_title', True):
            print(f"Title: {story.get('title')}")

        if output_config.get('show_url', True) and 'url' in story:
            print(f"URL: {story.get('url')}")

        if output_config.get('show_score', True):
            print(f"Points: {story.get('score', 0)}")

        if output_config.get('show_author', True):
            print(f"By: {story.get('by')}")

        if output_config.get('show_date', True):
            print(f"Posted: {format_timestamp(story.get('time', 0))}")

        if output_config.get('show_comments_count', True):
            print(f"Comments: {len(story.get('kids', []))}")

        print(f"HN Link: https://news.ycombinator.com/item?id={story.get('id')}")
        print(f"Matching Keywords: {', '.join(story.get('matching_keywords', []))}")

        if output_config.get('show_text_snippet', True) and 'text' in story:
            text = story.get('text')
            snippet_length = output_config.get('snippet_length', 150)
            snippet = text[:snippet_length] + "..." if len(text) > snippet_length else text
            print(f"Text: {snippet}")

        print("-" * 50)