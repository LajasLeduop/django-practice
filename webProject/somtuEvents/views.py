from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.
def index(request):
    now= datetime.now()
    if now.month==1 and now.day==1:
        message="Happy New Year!!!!"
    else:
        message="Sorry, It's not new year yet."

    data={
        "name": "Sajal Poudel",
        "message":message
    }
    return render(request,"index.html",data)