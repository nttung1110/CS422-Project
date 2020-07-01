import requests
import json

subscription_key = 'eb8e0024124b42ad8ac13b15ec45176d'
endpoint = 'https://cs422-image-captioning-api.cognitiveservices.azure.com/'

analyze_url = endpoint + "vision/v3.0/analyze"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'visualFeatures': 'Categories,Description,Color'}

class AI_ImgCaption_Services:
    def __init__(self):
        pass

    def serve_request(self, request):
        """
        Request should contains information about image url and access that information through request['image_url']
        """

        data = {'url': request['image_url']}
        response = requests.post(analyze_url, headers=headers, params=params, json=data)
        response.raise_for_status()

        analysis = response.json()
        #print(json.dumps(analysis))

        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
        #Function return caption of the image
        return image_caption
