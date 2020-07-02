### This class is used for talking to show_and_tell repository
from pycocotools.coco import COCO
import numpy as np
import json
dataDir = '/home/nttung/CS422-Project/data_COCO'
dataType = 'train2017'
save_path = '/home/nttung/CS422-Project/data_COCO/availabel_train2017_annot.json'
save_retrieved_imgIds = '/home/nttung/CS422-Project/list_imgID.txt'

class COCOAPIManager():

    def __init__(self, request):
        self.request= request
    
    def build_available_anno(self, imgIds):
        '''
            Params: 
                imgIds: list of all available image ID
            Function:
                Storing all annotation for an imgID
        '''
        print("On building available_annotation")

        annot_dict = {}
        annFile = '{}/annotations/captions_{}.json'.format(dataDir,dataType)
        coco_caps=COCO(annFile)
        count = 0

        for each_id in imgIds:
            print(count)
            annIds = coco_caps.getAnnIds(each_id)
            anns = coco_caps.loadAnns(annIds)
            
            list_cap = []
            for each_cap in anns:
                list_cap.append(each_cap["caption"])
            annot_dict[each_id] = list_cap
            count += 1
            

        with open(save_path, "w+") as f_p:
            json.dump(annot_dict, f_p, indent=2)


    def init_COCO_model(self):
        annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
        return COCO(annFile)

    def normalize_query_list(self, query_text):
        # returned list of keyword in text
        return query_text.split(" ")

    def lowercase_sen(self, sentence):
        return sentence.lower()

    def load_annot(self):
        
        with open(save_path) as fp:
            data = json.load(fp)

        return data

        
    def calculate_score(self, kw_list, list_cap):
        # calculate score by caption and keywords
        score = 0
        for each_kw in kw_list:
            for each_cap in list_cap:
                each_cap = self.lowercase_sen(each_cap)
                if each_kw in each_cap:
                    score += 1
        return score


    def sort_most_relevant(self, kw_list, imgIds, list_annot):
        score = {}


        for each_id in imgIds:
            cur_score = self.calculate_score(kw_list, list_annot[each_id])
            if cur_score != 0:
                score[each_id] = cur_score
        
        # score by descending score
        score = sorted(score.items(), key=lambda x:x[1], reverse=True)
        return score

    def mutual_process(self, imgIds, norm_q_list, coco, limit_size, list_annot):
        '''
            both refine and retrieve use this function
        '''
        score = self.sort_most_relevant(norm_q_list, imgIds, list_annot)

        res = {}
        count = 0
        res["list_img"] = []
        for (each_id, each_score) in score: #score in list of tuple with format ('imageId', 'score')
            img_instance = coco.loadImgs([int(each_id)])[0]
            img_instance["score"] = each_score
            res["list_img"].append(img_instance)

            count += 1
            if count == limit_size:
                break

        return res

    def save_imgID_for_debug_retrieve(self, res):
        res = res["list_img"]
        list_retrieved_imgID= []
        for each_img in res:
            list_retrieved_imgID.append(each_img["id"])

        with open(save_retrieved_imgIds , "w") as output:
            output.write(str(list_retrieved_imgID))

    def retrieve(self, request):
        # get coco instance
        coco = self.init_COCO_model()
        

        # extract field
        limit_size = request["limit_size"]
        text = request["text"]
        norm_q_list = self.normalize_query_list(text)
        
        # self.match_score(458054, ["skateboard", "dog"])
        list_annot = self.load_annot()

        imgIds = list_annot.keys()
        res = self.mutual_process(imgIds, norm_q_list, coco, limit_size, list_annot)
        self.save_imgID_for_debug_retrieve(res)
        return res

    def normalize_listid_for_refine(self, imgIds):
        imgIds = imgIds.split(',')
        imgIds[-1] = imgIds[-1][:-1]

        for index in range(len(imgIds)):
            imgIds[index] = imgIds[index][1:]

        return imgIds

    def refine(self, request):
        coco = self.init_COCO_model()

        imgIds = request["list_imgIds"]
        imgIds = self.normalize_listid_for_refine(imgIds)
        
        text = request["text"]
        norm_q_list = self.normalize_query_list(text)
        list_annot = self.load_annot()
        limit_size = 10
        score = self.sort_most_relevant(norm_q_list, imgIds, list_annot)

        res = self.mutual_process(imgIds, norm_q_list, coco, limit_size, list_annot)

        return res

    def process(self, request):
        type_req = request['type_request']
        if type_req == "search":
            return self.retrieve(request)

        if type_req == "refine":
            return self.refine(request)

if __name__ == "__main__":


    tmp = COCOAPIManager("Test")

    coco = tmp.init_COCO_model()
    imgIds = coco.getImgIds()
    
    tmp.build_available_anno(imgIds)
