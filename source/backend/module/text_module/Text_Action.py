from module.interface_module.Interface_Action import  Interface_Action

class Text_Action(Interface_Action):
    def __init__(self, request):
        super().__init__(request)

    def get_text_field(self):
        return self.request['text']

    def process_search(self, AI_Services_Manager):
        text_query = self.get_text_field()
        request_type = "search"
        # go to AI_Services_Manager to view structure of result
        if "AI_Text_Services" not in AI_Services_Manager.services.keys():
            return False
        result = AI_Services_Manager.services["AI_Text_Services"].serve_request(request_type, text_query)
        return result
    
    def process_refine(self, AI_Services_Manager):
        text_query = self.get_text_field()
        request_type = "refine"
        if "AI_Text_Services" not in AI_Services_Manager.services.keys():
            return False
        result = AI_Services_Manager.services["AI_Text_Services"].serve_request(request_type, text_query)
        return result
    
