from django.urls import path
from .views import SearchView, LecturerList, SearchResultsView, AboutView, ContactView


app_name = 'crawler'

urlpatterns = [

    path('', SearchView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('list_of_lecturers/', LecturerList.as_view(), name='list_of_lecturers'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]