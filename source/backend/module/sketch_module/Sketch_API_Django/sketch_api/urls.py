# mysite/urls.pyfrom django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import SketchSearch

app_name = "sketch_api"

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('sketch_search/search/', SketchSearch.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]