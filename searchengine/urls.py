from django.urls import path, include
from .views import search
# urlpattern for searchengine app
""" create a url for the search engine with query as a parameter """
urlpatterns = [
    path("search/", search, name="search"),
]

