from django.contrib import admin
from .models import Publication, Lecturer


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['pub_title', 'author']


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Publication)
admin.site.register(Lecturer)

