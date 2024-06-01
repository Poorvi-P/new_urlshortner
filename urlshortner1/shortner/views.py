from django.shortcuts import render
from django.http import JsonResponse
import uuid
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# Create your views here.
def hello(request):
    return JsonResponse({'message':'hello'})
@csrf_exempt
def create(request):
    data = json.loads(request.body)
    long_url = data['link']
    count = 0
    while count<=5:
        count = count + 1
        uid = str(uuid.uuid4())[:5]
        # uid = "48ef8"
        if not Url.objects.filter(uuid = uid).exists():
            new_url = Url(link = long_url, uuid = uid)
            new_url.save()
            return JsonResponse({"shortened_url":"localhost:8000/"+uid})
                # break
        # if count>=5:
    return JsonResponse({'message':"not able to generate"}) 

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)

    
        

