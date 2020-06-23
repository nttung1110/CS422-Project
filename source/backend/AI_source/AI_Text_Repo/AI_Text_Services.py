# from AI_source.AI_Text_Repo.s_t_party.ShowAndTellManager import ShowAndTellManager
from AI_source.AI_Text_Repo.coco_api_party.COCOAPIManager import COCOAPIManager
class AI_Text_Services:
    '''can flexibly exchange among multiple repo'''

    def __init__(self):
        pass

    def party_show_and_tell_process(self, request):
        model = ShowAndTellManager(request)
        return model.process(request)

    def party_coco_api_process(self, request):
        model = COCOAPIManager(request)
        return model.process(request)

    def serve_request(self, request):
        '''calling a specific third party repo'''

        #self.party_show_and_tell_process(request) ## talk to this party to serve this request
        return self.party_coco_api_process(request)

