## serve all services involving with AI, produce services and act as factory
from AI_source.AI_Text_Repo.AI_Text_Services import AI_Text_Services
from AI_source.AI_Sketch_Repo.AI_Sketch_Services import AI_Sketch_Services
from AI_source.AI_Image_Captioning_Repo.AI_Image_Captioning_Services import AI_ImgCaption_Services

class AI_Services_Manager():
    def __init__(self):
        #gather all involving resources

        self.services = {}
        self.add_default_services()

    def add_default_services(self):
        self.services["AI_Text_Services"] = AI_Text_Services()
        self.services["AI_Sketch_Services"] = AI_Sketch_Services()
        self.services["AI_Image_Captioning_Services"] = AI_ImgCaption_Services()

    def add_AI_Services(self, service_x_name, AI_X_Services):
        self.services[service_x_name] = AI_X_Services
        
