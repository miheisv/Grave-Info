from django.urls import path, re_path
from . import views


app_name = 'homepage'

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'search/',
        views.SearchView.as_view(),
        name='search_results'
    ),
    re_path(
        r'^human/(?P<pk>[1-9][0-9]*)/$',
        views.DetailView.as_view(),
        name='human'
    ),
]
