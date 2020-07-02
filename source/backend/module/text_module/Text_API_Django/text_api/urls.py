# mysite/urls.pyfrom django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import TextSearch

app_name = "text_api"

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('text_search/search/', TextSearch.as_view()),
    # path('text_retrieve/retrieve/', TextRetrieve.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]