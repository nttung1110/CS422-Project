from module.interface_module.Interface_Action import  Interface_Action

class Text_Action(Interface_Action):
    def __init__(self, request):
        # process request
        my_req = self.django_req_2_my_req(request)

        super().__init__(my_req)

    def django_req_2_my_req(self, request):
        my_req = {}
        my_req["type_request"] = request.POST["type_request"]
        my_req["text"] = request.POST["text"]
        return my_req

    def process_request(self, AI_Services_Manager):
        # go to AI_Services_Manager to view structure of result
        if "AI_Text_Services" not in AI_Services_Manager.services.keys():
            return False
        result = AI_Services_Manager.services["AI_Text_Services"].serve_request(self.request)
        return result

    
