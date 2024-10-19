class Music:
    def __init__(self):
        self.tracks = []

    def display(self):
        if not self.tracks:
            return "No tracks available."
        return "\n".join(self.tracks)

    def add(self, track):
        self.tracks.append(track)
        return f"Track '{track}' added."

    def delete(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            return f"Track '{track}' deleted."
        else:
            return f"Track '{track}' not found."

    def display_all_sorted(self, *genres):
        all_tracks = []
        for genre in genres:
            all_tracks.extend(genre.tracks)
        all_tracks.sort()
        if not all_tracks:
            return "No tracks available in all genres."
        return "\n".join(all_tracks)

class Pop(Music):
    def genre_info(self):
        return "This is Pop music."

class Rock(Music):
    def genre_info(self):
        return "This is Rock music."

class Jazz(Music):
    def genre_info(self):
        return "This is Jazz music."

def main():
    pop_music = Pop()
    rock_music = Rock()
    jazz_music = Jazz()

    # Menambahkan track
    print(pop_music.add("Shape of You"))
    print(rock_music.add("Bohemian Rhapsody"))
    print(jazz_music.add("Take Five"))
    print(pop_music.add("Blinding Lights"))
    print(rock_music.add("Hotel California"))
    print(jazz_music.add("So What"))

    # Menampilkan track secara terpisah
    print("\nPop Tracks:")
    print(pop_music.display())

    print("\nRock Tracks:")
    print(rock_music.display())

    print("\nJazz Tracks:")
    print(jazz_music.display())

    # Menampilkan seluruh lagu dari semua genre secara terurut
    print("\nAll Tracks (sorted A-Z):")
    print(pop_music.display_all_sorted(pop_music, rock_music, jazz_music))

    # Menghapus track
    print("\n" + rock_music.delete("Bohemian Rhapsody"))
    
    # Menampilkan kembali setelah penghapusan
    print("\nRock Tracks after deletion:")
    print(rock_music.display())

if __name__ == "__main__":
    main()
