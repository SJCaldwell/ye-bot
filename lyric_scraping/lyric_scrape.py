import requests
from bs4 import BeautifulSoup
import os


GENIUS_API_TOKEN = os.environ.get('genius_token')

base_url = "https://api.genius.com"
headers = {'Authorization': 'Bearer '+ GENIUS_API_TOKEN}

song_title = "Runaway"
artist_name = "BROCKHAMPTON"

def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  #gotta go regular html scraping... come on Genius
  page_url = "https://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  #remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  #at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
  return lyrics

if __name__ == "__main__":
  has_results = True
  page_count = 1
  while has_results:
    has_results = False
    search_url = base_url + "/search"
    data = {'q': artist_name, 'page': page_count}
    page_count +=1
    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()
    song_info = None
    for hit in json["response"]["hits"]:
      has_results = True
      if hit["result"]["primary_artist"]["name"] == artist_name:
        song_info = hit
        title = song_info['result']['title']
        song_api_path = song_info['result']['api_path']
        filename = title.replace(" ", "").lower()
        artist_folder = artist_name.replace(" ", "").lower()
        with open('../data/rap/' + artist_folder + "/" + filename, 'w') as f:
          f.write(lyrics_from_song_api_path(song_api_path))
    page_count += 1