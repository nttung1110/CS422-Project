from module.interface_module.Interface_Action import  Interface_Action
class Sketch_Action(Interface_Action):
    def __init__(self, request):
        # process request
        my_req = self.django_req_2_my_req(request)

        super().__init__(my_req)

    def django_req_2_my_req(self, request):
        my_req = {}
        my_req["width"] = str(request.POST["width"])
        my_req["height"] = str(request.POST["height"])

        a = str(request.POST["a"])
        b = str(request.POST["b"])
        c = str(request.POST["c"])

        my_req["ink"] = "[" + a + "," + b + "," + c + "]"
        my_req["limit_size"] = int(request.POST["limit_size"])
        return my_req

    def process_request(self, AI_Services_Manager):
        # go to AI_Services_Manager to view structure of result
        result = {}
        if "AI_Sketch_Services" not in AI_Services_Manager.services.keys():
            result["status"] = "AI_Sketch_Services not exist"
        else:
            result = AI_Services_Manager.services["AI_Sketch_Services"].serve_request(self.request)

        '''
            result = "keyword here"
        '''
        keyword = result

        # continue to call text services with keyword extracted from sketch
        internal_req = {}
        internal_req["type_request"] = "search"
        internal_req["limit_size"] = self.request["limit_size"]
        internal_req["text"] = keyword
        internal_req["is_internal"] = "YES"
        final_result = AI_Services_Manager.services["AI_Text_Services"].serve_request(internal_req)

        return final_result

    
