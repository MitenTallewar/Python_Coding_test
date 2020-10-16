
"""
#Song
A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist.
Otherwise, the playlist will end with the last song which points to None.

Implement a function is_repeating_playlist that, efficiently with respect to time used,
returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.
"""

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs = []
        next_song = self.next
        while next_song != None:
            print(next_song.name)
            songs.append(next_song)
            next_song = next_song.next
            print(next_song.name)
            if next_song in songs:
                return True
        return False


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song('abcd')
fourth = Song('efgh')
fifth = Song('wxyz')

first.next_song(second)
second.next_song(third)
third.next_song(fourth)
fourth.next_song(fifth)
first.next_song(first)
print(first.is_repeating_playlist())