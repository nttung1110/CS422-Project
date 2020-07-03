# mysite/urls.pyfrom django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import TextSearch
from AI_source.AI_Services_Manger import AI_Services_Manager

import sys
sys.path.append("../../../")

def init_AI_services():
    return AI_Services_Manager()

ai_service = init_AI_services()
app_name = "text_api"

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('text_search/search/', TextSearch.as_view(ai_service=ai_service)),
    # path('text_retrieve/retrieve/', TextRetrieve.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]