import json
import urllib.request
import urllib.parse
import re

# Termenii tăi de căutare aprobați (Whitelist-ul tău)
WHITELIST_TERMS = [
    "science experiments for kids shorts",
    "diy skills short",
    "how things work short"
]

def search_youtube_shorts(query):
    # Facem o căutare sigură pe YouTube după termeni
    query_string = urllib.parse.urlencode({"search_query": query})
    html_content = urllib.request.urlopen(f"https://www.youtube.com/results?{query_string}").read().decode('utf-8')
    
    # Extragem ID-urile video din pagina de rezultate folosind expresii regulate
    video_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html_content)
    
    # Returnăm primele 5 unice
    return list(dict.fromkeys(video_ids))[:5]

def generate_clean_playlist():
    print("Se generează lista curată de conținut...")
    all_videos = []
    
    # Căutăm pentru fiecare termen din whitelist
    for term in WHITELIST_TERMS:
        try:
            ids = search_youtube_shorts(term)
            for vid in ids:
                all_videos.append({
                    "id": vid,
                    "title": f"Skill Clip ({term})",
                    "category": "skills"
                })
        except Exception as e:
            print(f"Eroare la căutarea pentru {term}: {e}")
            
    # Dacă din 
    if not all_videos:
        # Fallback de siguranță dacă nu returnează rețeaua
        all_videos = [
            {"id": "3JZ_D3ELwOQ", "title": "Experiment științific rapid", "category": "skills"}
        ]

    # Salvăm în playlist.json
    with open("playlist.json", "w", encoding="utf-8") as f:
        json.dump(all_videos, f, ensure_ascii=False, indent=4)
        
    print("Fișierul playlist.json a fost actualizat cu succes!")

if __name__ == "__main__":
    generate_clean_playlist()
