import abc

class Album:
    def __init__(self,album_name,artist_name):
        self.album_name = album_name,
        self.artist_name = artist_name
    
    def __str__(self) -> str:
        return f"Album Name: {self.album_name} {self.artist_name}\n"
    
class Songs:
    def __init__(self, album: Album):
        self.album = album 
        self.song_item = []
        self.current_playing_song = 0
    
    def printMenu(self):
        print("Available options\nPress 0,1,2 to select options: \n")
        print("1 - to play next song\n2 - to play previous song\n3 - replay current song\n4 - print all available songs\n5 - show menu again\n6 - delete current playing song\n7 - start again\n8 - exit player\n")

    def addSong(self,song_title,song_duration):
        if len(self.song_item) == 0:
            dict = {"Song Name" :song_title, "Duration":song_duration}
            self.song_item.append(dict)
        
        else: 
            flag = False
            for index in range(len(self.song_item)):
                
                if song_title != self.song_item[index]["Song Name"]:
                    flag = True
                    continue
                else:
                    flag = False

            if flag == True:
                dict = {"Song Name" :song_title, "Duration":song_duration}
                self.song_item.append(dict)
            else:
                print(f"Song Name: {song_title} already in playlist.\n")
                
    def displayAlbums(self):
        return f"{self.album} \n Songs Playlist: {self.song_item}"
    
    def _start_player(self):

        if len(self.song_item) == 0:
            print("This playlist have no songs.\n")
        else:
            for song in self.song_item:
                name = song["Song Name"]
                if self.song_item.index(song) == self.current_playing_song:
                    print(f"-> {name}\n")
                else:
                    print("  ",name, "\n")

    def play_next(self):
        if 0 <= self.current_playing_song < len(self.song_item)-1:
            self.current_playing_song += 1
            self._start_player()
        else:
            print("Cannot go next anymore, end of songs queue.\n")
            
    def play_previous(self):
        if 0 <= self.current_playing_song <= len(self.song_item):
            if self.current_playing_song ==0:
                print("Cannot go previous anymore, at the start of song queue.\n")
            else:
                self.current_playing_song -= 1
                self._start_player()
        
    
    def replay_current(self):
        self._start_player()

    def show_all_songs(self):
        print(self.displayAlbums())  
        
    def show_menu(self):
        self.printMenu()
    
    def delete_current_playing_song(self):
        if len(self.song_item) > 0:
            name = self.song_item.pop(self.current_playing_song)
            print(f"{name}\n")
            
    def start_again(self):
        self.current_playing_song = 0
        self._start_player()

        
    def exit_player(self):
        print("exiting player...")
        print()
        raise SystemExit
    
    abc.abstractmethod
    def runner(action_dict):
        songs._start_player()
        
        while True:
            try:
                songs.printMenu()
                option = int(input())
            except ValueError as e:
                print("Please enter only digits and not any other character.\nRe-run the program and try again.")
                break
            if 1 <= option <= 8:
                actions_dict.get(option)()
            else:
                print("Not a valid menu option, try again.\n")

if __name__ == "__main__":
    album1 = Album(album_name = "Night Visions",artist_name = "Imagine Dragons")
    songs = Songs(album1)
    songs.addSong(song_title = "Deamons", song_duration = "2:57")
    songs.addSong(song_title = "Kala Chasma",song_duration = "3.5")
    songs.addSong(song_title = "Nachho Nachho",song_duration = "5.0")
    songs.addSong(song_title = "Happy New Year",song_duration = "5.0")
    songs.addSong(song_title = "Ole Ole",song_duration = "4.0")
    
    actions_dict = {1 : songs.play_next,
                    2 : songs.play_previous,
                    3 : songs.replay_current,
                    4 : songs.show_all_songs,
                    5 : songs.show_menu,
                    6 : songs.delete_current_playing_song,
                    7 : songs.start_again,
                    8 : songs.exit_player}
        
        
        
    Songs.runner(actions_dict) 
