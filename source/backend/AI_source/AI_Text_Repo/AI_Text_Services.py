# from AI_source.AI_Text_Repo.s_t_party.ShowAndTellManager import ShowAndTellManager
from AI_source.AI_Text_Repo.coco_api_party.COCOAPIManager import COCOAPIManager
from pycocotools.coco import COCO

dataDir = '/home/nttung/CS422-Project/data_COCO'
dataType = 'train2017'

class AI_Text_Services:
    '''can flexibly exchange among multiple repo'''
    def init_COCO_model(self):
        annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
        return COCO(annFile)

    def __init__(self):
        self.coco = self.init_COCO_model()

    def party_show_and_tell_process(self, request):
        model = ShowAndTellManager(request)
        return model.process(request)

    def party_coco_api_process(self, request):
        model = COCOAPIManager(request, self.coco)
        return model.process(request)

    def serve_request(self, request):
        '''calling a specific third party repo'''

        #self.party_show_and_tell_process(request) ## talk to this party to serve this request
        return self.party_coco_api_process(request)

