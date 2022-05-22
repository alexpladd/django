from django.http import request
from django.shortcuts import render
from .models import Song, SocialMedia, About, Contact

# Create your views here.
def index(request):
    
    songs = Song.objects.filter(public=True).order_by('-publication_date')
    social_medias = SocialMedia.objects.filter(public=True).order_by('order')
    
    return render(request, 'app/index.html', {
        'title': 'Official Website',
        'songs': songs,
        'social_medias': social_medias,
    })

def about(request):

    social_medias = SocialMedia.objects.filter(public=True).order_by('order')
    about =  About.objects.filter(public=True).order_by('-updated_at')[:1]

    return render(request, 'app/about.html', {
        'title': 'About Us',
        'social_medias': social_medias,
        'about': about
    })

def contact(request):

    social_medias = SocialMedia.objects.filter(public=True).order_by('order')
    contacts = Contact.objects.filter(public=True).order_by('-updated_at')
    
    return render(request, 'app/contact.html', {
        'title': 'Contact',
        'social_medias': social_medias,
        'contacts': contacts
    })

def error_404(request, exception):

    social_medias = SocialMedia.objects.filter(public=True).order_by('order')

    return render(request, 'error/404.html', {
        'title': 'Error 404',
        'social_medias': social_medias
    })

def error_500(request):

    social_medias = SocialMedia.objects.filter(public=True).order_by('order')
    
    return render(request, 'error/500.html', {
        'title': 'Error 500',
        'social_medias': social_medias
    })

def check():
    pass