import json

def save_results_to_file(stories, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {filename}")