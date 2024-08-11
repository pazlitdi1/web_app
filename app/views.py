from django.shortcuts import render
from django.views import View
import requests


class HomeView(View):
    def get(self, request):
        artist = requests.get("http://127.0.0.1:8000/artist-web/").json()
        context = {"artist": artist}

        return render(request, 'home.html', context)


class ArtistView(View):
    def get(self, request):
        artist = requests.get("http://127.0.0.1:8000/artist-web/").json()
        context = {"artist": artist}

        return render(request, 'artist.html', context)


class AlbumView(View):
    def get(self, request):
        album = requests.get("http://127.0.0.1:8000/album-web/").json()
        context = {"album": album}

        return render(request, 'album.html', context)


class SongView(View):
    def get(self, request):
        song = requests.get("http://127.0.0.1:8000/song-web/").json()
        context = {"song": song}

        return render(request, 'song.html', context)
