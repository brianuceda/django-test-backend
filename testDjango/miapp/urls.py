from django.urls import path
from miapp.views import search_youtube_view
from miapp.views import search_birthday_by_separated_names_view
from miapp.views import search_birthday_by_full_name_view

urlpatterns = [
    path('search_youtube', search_youtube_view, name='search_youtube'),
    path('search_birthday_by_separated_names', search_birthday_by_separated_names_view, name='search_birthday_by_separated_names'),
    path('search_birthday_by_full_name', search_birthday_by_full_name_view, name='search_birthday_by_full_name')
]