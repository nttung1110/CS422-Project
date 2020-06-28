from django.shortcuts import render

from rest_framework.response import Response

# from rest_framework import viewsets
from rest_framework.views import APIView
import sys
## Ubuntu path
sys.path.append("../../../../")

## Window path
sys.path.append(r"D:\CS422_Project_Updated\CS422-Project\source\backend")

from AI_source.AI_Services_Manger import AI_Services_Manager
from module.text_module.Text_Action import Text_Action

# from .serializers import HeroSerializer
# from .models import Hero


# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

class TextSearch(APIView):
    def post(self, request):# do search request
        all_services = AI_Services_Manager()
        get_action = Text_Action(request)
        results_search = get_action.process_request(all_services)
        print(results_search)
        return Response({"results": results_search})
# Create your views here.
