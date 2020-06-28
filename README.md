# CS422-Project
## Environment setup

```
ssh nttung@thevncore-lab.mooo.com -p 19523

cd CS422-Project

conda activate CS422_tung
```

### Text module

text module path = 'source/backend/module/Text_API_Django'

Text module API implementation is located inside text_module_path

To start deploy text module services, follow these steps:

+ Start to forward local host from server to your local machine for testing

Run on terminal
```
ngrok http 8000
```

<img src="/instruction/ngrok.png" width=800 height=300 />

Replace underlined text to the last elements of ALLOWED_HOSTS array as following 

<img src="/instruction/setting.png" width=500 height=50 />

+ Deploy text services

Run on terminal
```

cd source/backend/module/Text_API_Django

python manage.py runserver
```

+ API Access:

Text service currently serve POST request to retrieve images

Sample POST request can be as following: 

<img src="/instruction/sample_request.png" width=800 height=300 />
