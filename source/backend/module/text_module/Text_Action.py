from module.interface_module.Interface_Action import  Interface_Action

class Text_Action(Interface_Action):
    def __init__(self, request):
        super().__init__(request)


    def process_request(self, AI_Services_Manager):
        # go to AI_Services_Manager to view structure of result
        if "AI_Text_Services" not in AI_Services_Manager.services.keys():
            return False
        result = AI_Services_Manager.services["AI_Text_Services"].serve_request(self.request)
        return result

    
