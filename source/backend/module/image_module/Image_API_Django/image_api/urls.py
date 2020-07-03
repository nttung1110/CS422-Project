# mysite/urls.pyfrom django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import ImageSearch
import sys
from AI_source.AI_Services_Manger import AI_Services_Manager

sys.path.append("../../../")

app_name = "image_api"
def init_AI_services():
    return AI_Services_Manager()

ai_service = init_AI_services()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('image_search/search/', ImageSearch.as_view(ai_service=ai_service)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]