def is_name_blocked(name: str, blocked_words: list[str]) -> bool:
    for word in blocked_words:
        if word in name:
            return True
        
    return False

def build_radio_queue(song_names: list[str], blocked_words: list[str]) -> list[str]:
    queue: list[str] = []
    
    for song_name in song_names:
        
        already_in_queue = song_name in queue
        if already_in_queue:
            continue
        
        if is_name_blocked(song_name, blocked_words):
            continue
                
        if song_name != '':
            queue.append(song_name)
    
    return queue

songs = ["Blue Sky", "Ad Break", "Blue Sky", "Night Drive", ""]
blocked_words = ["Ad"]

print(build_radio_queue(songs, blocked_words))