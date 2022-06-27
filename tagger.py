import eyed3

import os

dir_ = '/Users/alex/Downloads' 


def parse_artist_name(_dir, file_name):
    """
    normally filename should contain artist - trackname
    other option that its in folder name
    :param _dir:
    :param file_name:
    """
    dirs_split = str.split(_dir, os.sep)
    filename_split = str.split(filename, ' - ')

def parse_filename(_dir, file_name):
    os.chdir(_dir)

    things = str.split(file_name, ' - ')
    artist = things[0]
    rest = str.split(things[1], '-')
    track = rest[0]

    audiofile = eyed3.load(file_name)
    if audiofile.tag.artist is None:
        # detect artist here. add more complicated logic
        audiofile.tag.artist = unicode(artist, "utf-8")
    if audiofile.tag.title is None:
        # detect title here. add more complicated logic
        audiofile.tag.title = unicode(track, "utf-8")
    print("parsed %s - %s " % (artist, track))
    audiofile.tag.save()


for root, directories, filenames in os.walk(dir_):
    for directory in directories:
        pass
    for filename in filenames:
        if filename.endswith(".mp3"):
            try:
                parse_filename(root, filename)
            except (StandardError, IndexError) as e:
                print(e)
