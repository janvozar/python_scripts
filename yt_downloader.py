from pytube import YouTube
from sys import argv

#utl = input("url"), it is better to use arguments
print(argv)
url = argv [1]
youtube = YouTube (url)
print(youtube.title)
#print(youtube.author)
#print(youtube.keywords)
#print(youtube.length)

stream = youtube.streams.get_highest_resolution ()
stream.download("/Users/janvozar/Downloads") 