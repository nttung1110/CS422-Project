from module.interface_module.Interface_Action import  Interface_Action

class Text_Action(Interface_Action):
    def __init__(self, request):
        # process request
        if "is_internal" in request:
            my_req = request
        else:
            my_req = self.django_req_2_my_req(request)

        super().__init__(my_req)

    def django_req_2_my_req(self, request):
        my_req = {}
        my_req["type_request"] = request.POST["type_request"]
        my_req["limit_size"] = int(request.POST["limit_size"])
        my_req["text"] = request.POST["text"]
        return my_req

    def process_request(self, AI_Services_Manager):
        # go to AI_Services_Manager to view structure of result
        result = {}
        if "AI_Text_Services" not in AI_Services_Manager.services.keys():
            result["status"] = "AI_Text_Services not exist"
        else:
            result = AI_Services_Manager.services["AI_Text_Services"].serve_request(self.request)
        return result

    
