from module.interface_module.Interface_Action import  Interface_Action

class Image_Action(Interface_Action):
    def __init__(self, request):
        # process request
        my_req = self.django_req_2_my_req(request)

        super().__init__(my_req)

    def django_req_2_my_req(self, request):
        my_req = {}
        my_req["image_url"] = request.POST["image_url"]
        my_req["limit_size"] = int(request.POST["limit_size"])
        return my_req

    def parse_caption(self, caption):
        '''
            filter important keywords in caption
        '''
        return caption

    def process_request(self, AI_Services_Manager):
        # go to AI_Services_Manager to view structure of result
        result = {}
        if "AI_Image_Captioning_Services" not in AI_Services_Manager.services.keys():
            result["status"] = "AI_Image_Captioning_Services not exist"
        else:
            result = AI_Services_Manager.services["AI_Image_Captioning_Services"].serve_request(self.request)
        '''
            result = "image caption here"
        '''
        print("Caption:", result)
        caption = result

        internal_req = {}
        internal_req["type_request"] = "search"
        internal_req["limit_size"] = self.request["limit_size"]
        internal_req["text"] = self.parse_caption(caption)
        internal_req["is_internal"] = "YES"
        final_result = AI_Services_Manager.services["AI_Text_Services"].serve_request(internal_req)

        return final_result

    
