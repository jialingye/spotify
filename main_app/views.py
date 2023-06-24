from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Artist
from django.views.generic.edit import CreateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class SongList(TemplateView):
    template_name = "song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = songs
        return context
    
class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Artist.objects.filter(name__icontains=name)
            context['header'] = f'searching for {name}'
        else:
            context["artists"] = Artist.objects.all()
            context['header'] = 'All trending artists'
        return context
    
class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"
    success_url = "/artists/"

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

songs = [
    Song("Lost", "hayd"),
    Song("Never Ending Song", "Connor Gray"),
]

