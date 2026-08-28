import json
import os
import urllib.request
import urllib.parse

# Termenii tăi de căutare aprobați (Whitelist-ul tău inițial)
WHITELIST_TERMS = [
    "science experiments for kids",
    "diy skills",
    "how things work explained"
]

def generate_clean_playlist():
    print("Se generează lista curată de conținut...")
    
    clean_videos = [
        {
            "id": "dQw4w9WgXcQ", # Exemplu de ID video YouTube
            "title": "Experiment științific simplu",
            "category": "science"
        }
    ]
    
    with open("playlist.json", "w", encoding="utf-8") as f:
        json.dump(clean_videos, f, ensure_ascii=False, indent=4)
        
    print("Fișierul playlist.json a fost generat cu succes!")

if __name__ == "__main__":
    generate_clean_playlist()
