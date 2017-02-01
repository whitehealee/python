# Create your views here.
from django.http import HttpResponse
import datetime
def hello(request):
    return HttpResponse("Здравствуй мир")
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now "+str(now)+".<body><html>"
    return HttpResponse(html)
