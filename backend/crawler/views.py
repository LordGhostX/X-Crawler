from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Lecturer, Publication
from .serializers import PublicationSerializer, LecturerSerializer
from rest_framework import filters


class SearchView(generics.ListAPIView):
    crawler = [
        "Prof. Waled", "Plans on how next to destroy engineering students lives",
        "summary talk slowly", "www.killingdem.com"
    ]
    new_pub = Publication()
    new_pub.author = crawler[0]
    new_pub.pub_title = crawler[1]
    new_pub.pub_summary = crawler[2]
    new_pub.pub_url = crawler[3]

    for pub in Publication.objects.all():
        if new_pub == pub:
            new_pub.delete()
    new_pub.save()
    context_object_name = "all_publications"
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'pub_title']


class LecturerList(APIView):
    serializer_class = LecturerSerializer

    def get_queryset(self):
        return Lecturer.objects.all()


