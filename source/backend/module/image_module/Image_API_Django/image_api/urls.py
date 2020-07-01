# mysite/urls.pyfrom django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import ImageSearch

app_name = "image_api"

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('image_search/search/', ImageSearch.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]