import urllib3
from bs4 import BeautifulSoup
import requests
import json
import os
import re, string
import sys
import pprint


class LyricScraper:

    def __init__(self):
        self.bases = list("1abcdefghijklmnopqrstuvwxyz")

    def scrapeMainArtists(self, numPages=1, letterInd=0):
        baseUrl = "http://www.metrolyrics.com/artists-"+self.bases[letterInd]+"-"

        artistList = []
        
        for i in range(0,numPages):
            url = baseUrl + str(i) + ".html"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            artistTable = soup.find("tbody")
            allRows = artistTable.find_all("tr")

            for row in allRows:
                allEntries = row.find_all("td")[0:2]
                artistName = allEntries[0].text.replace("Lyrics", "").strip()
                artistGenre = allEntries[1].text.strip()
                if artistGenre is "":
                    artistGenre = "Unknown"
                artistUrl = allEntries[0].find("a", href=True)['href']
                artistList.append({
                    "name": artistName,
                    "genre": artistGenre,
                    "url": artistUrl,
                })
        return artistList

    def scrapeArtist(self, artist):
        songlist = []
        url = artist['url']
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        artistTable = soup.find(class_="songs-table compact").find("tbody")
        allRows = artistTable.find_all("tr")

        for row in allRows:
            songEntry = row.find_all("td")[1]
            songName = songEntry.text.replace("Lyrics", "").strip()
            songUrl =  songEntry.find("a", href=True)['href']
            songlist.append({
                "songname": songName, 
                "songurl": songUrl
            })
        artist["songlist"] = songlist
        return artist

    def scrapeSong(self, artist):
        for song in artist["songlist"]:
            lyrics = ""
            page = requests.get(song["songurl"])
            soup = BeautifulSoup(page.content, "html.parser")
            allLyrics = soup.find_all(class_="verse")
            translator = str.maketrans('', '', string.punctuation)
            for lyric in allLyrics:
                lyrics += lyric.text.lower().translate(translator).replace('\n',' ')
            song["lyrics"] = lyrics
        return artist

    @staticmethod
    def scrapeSingleSong(self, url):
        lyricsDict = {
            "url": url,
            "lyrics": ""
        }

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        allLyrics = soup.find_all(class_="verse")

        translator = str.maketrans('', '', string.punctuation)
        for lyric in allLyrics:
            lyricsDict['lyrics'] += lyric.text.lower().translate(translator).replace('\n',' ')
        return lyricsDict['lyrics']
    
    def run(self, numPages=1):
        for i in range(0, len(self.bases)):
            artists = self.scrapeMainArtists(numPages, i)
            for artist in artists:
                artist = self.scrapeSong(self.scrapeArtist(artist))
                self.write(artist, f"songscraping/songscraping-{self.bases[i]}.json", True)
        self.fixJson()
        self.makeDset()


    def write(self, artist, filename, append=False):
        with open(filename, 'a' if append else 'w') as outfile:
            json.dump(artist, outfile, sort_keys = True, indent = 4)


    def fixJson(self):
        directory = os.scandir('./songscraping')
        for filename in directory:
            if filename.is_file():
                if filename.name.endswith('json'):
                    filestr = ""
                    with open('./songscraping/'+filename.name, "r") as f:
                        filestr = f.read().replace("}{", "},{")
                    with open('./songscraping/'+filename.name, "w") as f:
                        f.write("[\n" + filestr + "\n]")

    def makeDset(self):
        directory = os.scandir('./songscraping')
        genreLyrics = {}
        '''
            {
                "rock": {
                    "lyrics": "askdjhkalsdkj",
                    "artists": ["one", "two",...]
                }
            }
        '''
        for filename in directory:
            if filename.is_file():
                if filename.name.endswith('json') and filename.name.startswith("songscraping"):
                    with open('./songscraping/'+filename.name, "r") as f:
                        currentList = json.load(f)
                        for artist in currentList:
                            print(artist["name"], artist["genre"])
                            artistname = artist["name"].lower().strip()
                            genre = artist["genre"].lower().strip()
                            if genre not in genreLyrics:
                                genreLyrics[genre] = {"lyrics":"", "artists":[]}
                            if artistname not in genreLyrics[genre]["artists"]:
                                genreLyrics[genre]["artists"].append(artistname)
                            for song in artist["songlist"]:
                                genreLyrics[genre]["lyrics"]+=song["lyrics"]+"\n"
        with open('./songscraping/dset.json', "w") as f:
            json.dump(genreLyrics, f, indent=2)


if __name__ == "__main__":
    scraper = LyricScraper()
    scraper.run()
