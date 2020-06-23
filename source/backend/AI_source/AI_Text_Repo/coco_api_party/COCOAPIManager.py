### This class is used for talking to show_and_tell repository
# from pycocotools.coco import COCO
import numpy as np
class COCOAPIManager():

    def __init__(self, request):
        self.request= request
    
    def init_COCO_model(self):
        dataDir = '..'
        dataType = 'val2017'
        annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
        return COCO(annFile)

    def normalize_query_list(self, query_text):
        # returned list of keyword in text
        return query_text.split(" ")

    def retrieve(self, request):
        # # get coco instance
        # coco = self.init_COCO_model()


        # # extract field
        # limit_size = request["limit_size"]
        # text = request["text"]
        # norm_q_list = self.normalize_query_list(text)

        # catIds = coco.getCatIds(catNms=norm_q_list)
        # imgIds = coco.getImgIds(catIds=catIds)
        # imgIds = coco.getImgIds(imgIds = [limit_size])
        # img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

        ###testing
        res = {}
        res["list_img"] = []
        res["list_img"].append({"name": "a","content":"img_content_a","query_search":request["text"]})
        res["list_img"].append({"name": "b","content":"img_content_b","query_search":request["text"]})
 
        return res

    # def refine(self, request):


    def process(self, request):
        type_req = request['type_request']
        if type_req == "search":
            return self.retrieve(request)

        if type_req == "refine":
            return self.refine(request)
