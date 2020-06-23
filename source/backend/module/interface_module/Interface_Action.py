import os 
# from sketch_module import Query_Sketch
from AI_source.AI_Services_Manger import AI_Services_Manager
class Interface_Action:
    def __init__(self, request):
        # request must first have value to decide type of query and that query
        # 1 as text, 2 as image and 3 as sketch
        self.request = request

    # def init_query(self, type_query):
    #     if self.type_query == 1: # Text queries
    #         return Query_Text(self.request, self.type_query)
    #     if self.type_query == 2: # Image queries
    #         return "NotImplemented"
    #     if self.type_query == 3: # Sketch queries
    #         return "NotImplemented"

    # def decode_request(self):
    #     # Getting field from request and store it inside a dictionary with key as name of field and value as results of that field
    #     self.field_request = {}
    #     self.field_request["query"] = self.init_query()

    def process_request(self, AI_Services_Manager):
        ## checking which type of search user want
        pass




