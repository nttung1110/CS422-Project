import requests
import json
import pprint

quickdraw_url = 'https://inputtools.google.com/request?ime=handwriting&app=quickdraw&dbg=1&cs=1&oe=UTF-8'
headers = {
		'Accept': '*/*',
		'Referer': 'https://quickdraw.withgoogle.com/',
		'Origin': 'https://quickdraw.withgoogle.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
		'Content-Type': 'application/json'
        }

class AI_Sketch_Services:
    def __init__(self):
        pass

    def serve_request(self, request):
        """
        Request should be a dictionary contains these key-value pairs:
            width: str
            height: str
            ink: str provides information in format [x, y, t] where x,y,t are lists of value

        For example:
            request['width'] = '886'
            request['height'] = '348'
            request['ink'] = '[[217,218,220,...], [81,81,81,...], [0,298.4149999999995,316.1100000000001,...]]'
        """

        data = '{"input_type":0,"requests":[{"language":"quickdraw","writing_guide":{"width":' + request['width'] + ',"height":' + request['height'] + '},"ink":[' + request['ink'] + ']}]}'

        r = requests.post(quickdraw_url, headers=headers, data=data)

        d = json.loads(r.content)

        #pprint.pprint(d)

        #Return top 1 result, can change to return top 3,5 or sth like that
        return d[1][0][1][0]
