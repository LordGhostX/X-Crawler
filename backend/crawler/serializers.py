from rest_framework import serializers
from .models import Publication, Lecturer


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = [
                    'author',
                    'pub_title',
                    'pub_url',
                    'pub_summary',
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