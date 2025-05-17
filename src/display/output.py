import shutil
from typing import List, Dict, Any, Optional
from utils.formatter import format_timestamp

def paginated_print(lines: List[str], lines_per_page: Optional[int] = None) -> None:
    if lines_per_page is None:
        try:
            lines_per_page = shutil.get_terminal_size().lines - 2
            # Subtract 2 to account for the prompt line and buffer
        except (AttributeError, OSError):
            # More specific error handling
            lines_per_page = 20
            
    for i in range(0, len(lines), lines_per_page):
        chunk = lines[i:i + lines_per_page]
        print("\n".join(chunk))
        if i + lines_per_page < len(lines):
            input("\nPress Enter to continue...")


def display_stories(stories: List[Dict[str, Any]], output_config: Dict[str, Any]) -> None:
    if not stories:
        print("No matching stories found.")
        return
        
    all_lines = []
    all_lines.append(f"\nFound {len(stories)} matching stories:\n")
    
    for i, story in enumerate(stories, 1):
        story_lines = [f"Story #{i}"]
        
        # Add optional fields based on configuration
        field_configs = [
            ('show_title', 'Title', 'title', None),
            ('show_url', 'URL', 'url', None),
            ('show_score', 'Points', 'score', 0),
            ('show_author', 'By', 'by', None),
            ('show_date', 'Posted', 'time', 0, format_timestamp),
            ('show_comments_count', 'Comments', 'kids', [], lambda x: len(x))
        ]
        
        for config_key, label, story_key, default, *transform in field_configs:
            if output_config.get(config_key, True) and (story_key in story or default is not None):
                value = story.get(story_key, default)
                if transform:  # Apply transformation function if provided
                    value = transform[0](value)
                story_lines.append(f"{label}: {value}")
        
        story_lines.append(f"HN Link: https://news.ycombinator.com/item?id={story.get('id')}")
        story_lines.append(f"Matching Keywords: {', '.join(story.get('matching_keywords', []))}")
        
        if output_config.get('show_text_snippet', True) and 'text' in story:
            text = story.get('text', '')
            snippet_length = output_config.get('snippet_length', 150)
            snippet = f"{text[:snippet_length]}..." if len(text) > snippet_length else text
            story_lines.append(f"Text: {snippet}")
            
        story_lines.append("-" * 50)
        all_lines.extend(story_lines)
        
    paginated_print(all_lines)