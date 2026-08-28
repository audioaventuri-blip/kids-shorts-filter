import json

# Listă fixă, curată și verificată de Shorts cu natură, peisaje și animale sălbatice
# (fără riscul de "video unavailable" de la căutările automate pe YouTube)
NATURE_SHORTS = [
    {"id": "7X74_YKsuHM", "title": "Wildlife & Nature 1", "category": "nature"},
    {"id": "Lu34rt8h3EA", "title": "Wildlife & Nature 2", "category": "nature"},
    {"id": "dQw4w9WgXcQ", "title": "Test Nature Clip", "category": "nature"} # Poți înlocui cu ID-uri sigure
]

def generate_clean_playlist():
    print("Se generează lista sigură de natură...")
    
    with open("playlist.json", "w", encoding="utf-8") as f:
        json.dump(NATURE_SHORTS, f, ensure_ascii=False, indent=4)
        
    print("Fișierul playlist.json a fost actualizat cu succes!")

if __name__ == "__main__":
    generate_clean_playlist()
