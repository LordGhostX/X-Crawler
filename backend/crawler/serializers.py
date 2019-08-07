from rest_framework import serializers
from .models import Publication, Lecturer


class PublicationSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        return {
            'pub_title': obj.pub_title,
            'author': obj.author,
            'pub_summary': obj.pub_summary,
            'pub_url': obj.pub_url,
            'pub_picture': obj.pub_picture,
        }

    class Meta:
        model = Publication
        fields = [
            'pub_title',
            'author',
            'pub_summary',
            'pub_url',
            'pub_picture',
        ]


class LecturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecturer
        fields = [
            'name',
            'email',
            'date_of_birth',
            'description',
            'fields',
            'works',
            'pictures',
        ]