import re


def song_decoder(song):
    return re.sub(r'(WUB)+', " ", song).strip()


if __name__ == '__main__':
    print(song_decoder("AWUBBWUBC"))
