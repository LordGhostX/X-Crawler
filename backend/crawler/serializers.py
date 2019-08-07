from rest_framework import serializers
from .models import Publication, Lecturer


class PublicationSerializer(serializers.BaseSerializer):

    # def to_representation(self, obj):
    #     return {
    #         'title': obj.pub_title,
    #         'author': obj.author,
    #         'summary': obj.pub_summary,
    #         'url': obj.pub_url,
    #         'picture': obj.pub_picture,
    #     }

    class Meta:
        model = Publication
        fields = [
            'title',
            'author',
            'summary',
            'url',
            'picture',
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