## serve all services involving with AI, produce services and act as factory
from AI_source.AI_Text_Repo.AI_Text_Services import AI_Text_Services
class AI_Services_Manager():
    def __init__(self):
        #gather all involving resources

        self.services = {}
        self.add_default_services()

    def add_default_services(self):
        self.services["AI_Text_Services"] = AI_Text_Services()
        # self.services["AI_Sketch_Services"] = AI_Sketch_Services

    def add_AI_Services(self, service_x_name, AI_X_Services):
        self.services[service_x_name] = AI_X_Services
        
