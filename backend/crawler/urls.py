from django.urls import path
from django.views.generic.base import TemplateView

from crawler.views import SearchView, LecturerList, SearchResultsView


app_name = 'crawler'

urlpatterns = [
    path('', SearchView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='crawler/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='crawler/contact.html'), name='contact'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('list_of_lecturers/', LecturerList.as_view(), name='list_of_lecturers')
]