import json
import urllib.request
import urllib.parse
import re

# Termenii tăi de căutare fixați pe "explore nature" pentru Shorts
WHITELIST_TERMS = [
    "explore nature shorts",
    "wildlife nature shorts",
    "nature documentary short"
]

def search_youtube_shorts(query):
    query_string = urllib.parse.urlencode({"search_query": query})
    req = urllib.request.Request(
        f"https://www.youtube.com/results?{query_string}",
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        html_content = urllib.request.urlopen(req).read().decode('utf-8')
        video_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html_content)
        return list(dict.fromkeys(video_ids))[:8]
    except Exception as e:
        print(f"Eroare căutare: {e}")
        return []

def generate_clean_playlist():
    print("Se generează lista curată de conținut (Explore Nature)...")
    all_videos = []
    
    for term in WHITELIST_TERMS:
        ids = search_youtube_shorts(term)
        for vid in ids:
            all_videos.append({
                "id": vid,
                "title": "Explore Nature Short",
                "category": "nature"
            })
            
    # Fallback de siguranță dacă nu returnează rețeaua
    if not all_videos:
        all_videos = [
            {"id": "Lu34rt8h3EA", "title": "Nature Exploration", "category": "nature"}
        ]

    with open("playlist.json", "w", encoding="utf-8") as f:
        json.dump(all_videos, f, ensure_ascii=False, indent=4)
        
    print("Fișierul playlist.json a fost actualizat!")

if __name__ == "__main__":
    generate_clean_playlist()
