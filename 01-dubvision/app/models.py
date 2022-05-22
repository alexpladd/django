from django.db import models
from django.db.models.fields import EmailField

class Song(models.Model):

    title = models.CharField(max_length=100, verbose_name="Title")
    artists = models.CharField(max_length=255, verbose_name="Artists")
    cover_page = models.ImageField(default="default.jpg", verbose_name="Cover Page", upload_to="songs")
    public = models.BooleanField(verbose_name="Public")
    url = models.URLField(default=" ", verbose_name="URL")
    publication_date = models.DateField(blank=True, null=True, verbose_name="Publication Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
    
    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.CharField(max_length=100, verbose_name="Slug")
    public = models.BooleanField(verbose_name="Public")
    order = models.PositiveSmallIntegerField(unique=True, default=0, verbose_name="Order")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"
    
    def __str__(self):
        return self.name

class About(models.Model):

    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(default='dubvision.jpg', verbose_name="Image", upload_to="abouts")
    public = models.BooleanField(verbose_name="Public")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    email = models.EmailField(max_length=200, verbose_name="Email")
    public = models.BooleanField(verbose_name="Public")
    order = models.PositiveSmallIntegerField(unique=True, default=0, verbose_name="Order")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.title
