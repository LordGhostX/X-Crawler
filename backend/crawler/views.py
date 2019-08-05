from rest_framework.views import APIView
from rest_framework import generics
from .models import Lecturer, Publication
from .serializers import PublicationSerializer, LecturerSerializer
from rest_framework import filters
from .pagination import PostPageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class SearchView(generics.ListAPIView):
    template_name = "index.html"
    queryset = Publication.objects.all()
    context_object_name = "all_publications"
    serializer_class = PublicationSerializer
    renderer_classes = [TemplateHTMLRenderer]
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        return Publication.objects.all()
    # with open('data.txt', "r") as text_file:
    #     text = eval(text_file.read())
    #     for research in text:
    #
    #             new_pub = Publication()
    #             new_pub.author = research['author']
    #             new_pub.pub_url = research['research_link']
    #             new_pub.pub_title = research['research_title']
    #             new_pub.pub_summary = research['abstract']
    #
    #             for pub in Publication.objects.all():
    #                 if new_pub == pub:
    #                     new_pub.delete()
    #             new_pub.save()


class AboutView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name='about.html')


class ContactView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name='contact.html')


class SearchResultsView(APIView):
    queryset = Publication.objects.all()
    context_object_name = "all_publications"
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'pub_title']
    renderer_classes = [TemplateHTMLRenderer]


class LecturerList(APIView):
    serializer_class = LecturerSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        return Lecturer.objects.all()


