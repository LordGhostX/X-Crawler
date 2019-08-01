from django.urls import path
from .views import SearchView, LecturerList


app_name = 'crawler'

urlpatterns = [

    path('', SearchView.as_view(), name='search'),
    path('list_of_lecturers/', LecturerList.as_view(), name='list_of_lecturers'),

]