from django.contrib import admin
from .models import Contact, Song, SocialMedia, About

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'artists', 'cover_page', 'publication_date', 'public', 'created_at', 'updated_at')
    ordering = ('-publication_date',)
    search_fields = ('title', 'artists')
    list_filter = ('public',)

class SocialMediaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'slug', 'order', 'public', 'created_at', 'updated_at')
    ordering = ('order',)
    search_fields = ('name',)
    list_filter = ('public',)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'description', 'image', 'public', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('public',)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'email', 'public', 'order', 'created_at', 'updated_at')
    ordering = ('order',)
    search_fields = ('title', 'email')
    list_filter = ('public',)

admin.site.register(Song, SongAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)

title = "Control Panel"
subtitle = "DUBVISION"

admin.site.site_header = title.upper() + " | DUBVISION OFFICIAL WEBSITE"
admin.site.site_title = title
admin.site.index_title = subtitle
