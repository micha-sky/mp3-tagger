import eyed3

import os

downloads_ = '/Users/alex/Downloads/'


def parse_filename(file_name):
    os.chdir(downloads_)
    things = str.split(file_name, ' - ')
    artist = things[0]
    rest = str.split(things[1], '-')
    track = rest[0]
    audiofile = eyed3.load(file_name)
    if audiofile.tag.artist is None:
        audiofile.tag.artist = unicode(artist, "utf-8")
    if audiofile.tag.title is None:
        audiofile.tag.title = unicode(track, "utf-8")
    print 'parsed ', artist, track
    audiofile.tag.save()


for filename in os.listdir(downloads_):
    if filename.endswith(".mp3"):
        print 'reading ' + filename
        parse_filename(filename)
