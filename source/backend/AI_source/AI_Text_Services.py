
class AI_Text_Services:
    def __init__(self):
        pass

    def retrieve_image(self, text_query):
        return "Ready to retrieve image by using queries: "+text_query
    
    def refine_results(self, text_query):
        return "Ready to refine image by using queries: "+text_query

    def serve_request(self, request_type, text_query):

        if(request_type == "search"):
            return self.retrieve_image(text_query)

        if(request_type == "refine"):
            return self.refine_results(text_query)