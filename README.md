# CS422-Project

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

+ API Documentation:

https://documenter.getpostman.com/view/8735149/T17Dgomi?version=latest

+ Text services: 9cad890d9904.ngrok.io

+ Sketch services: e04e9e53a1d2.ngrok.io

+ Image services: ec35e7629360.ngrok.io

### Demo 
https://www.youtube.com/watch?v=hX6_5KruNC4
