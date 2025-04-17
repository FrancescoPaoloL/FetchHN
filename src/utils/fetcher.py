import asyncio
import aiohttp
from typing import List, Dict, Any, Optional

# see: https://github.com/HackerNews/API

async def fetch_json(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    async with session.get(url) as response:
        return await response.json()

async def fetch_story(session: aiohttp.ClientSession, story_id: int, keywords: List[str]) -> Optional[Dict[str, Any]]:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story = await fetch_json(session, story_url)
    if story and 'title' in story:
        title = story.get('title', '').lower()
        text = story.get('text', '').lower()
        matching_keywords = []
        for keyword in keywords:
            if keyword.lower() in title or keyword.lower() in text:
                matching_keywords.append(keyword)
        if matching_keywords:
            story['matching_keywords'] = matching_keywords
            return story
    return None

async def fetch_top_stories(session: aiohttp.ClientSession, limit: int = 500) -> List[int]:
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    stories = await fetch_json(session, url)
    return stories[:limit]

async def fetch_stories_by_keywords(keywords: List[str], max_stories: int = 100, concurrent_connections: int = 50) -> List[Dict[str, Any]]:
    async with aiohttp.ClientSession() as session:
        story_ids = await fetch_top_stories(session, max_stories)
        
        # Process stories in batches to control concurrency
        results = []
        for i in range(0, len(story_ids), concurrent_connections):
            batch = story_ids[i:i+concurrent_connections]
            tasks = [fetch_story(session, story_id, keywords) for story_id in batch]
            batch_results = await asyncio.gather(*tasks)
            
            # Filter None results and append to results list
            results.extend([r for r in batch_results if r])
            
        return results
