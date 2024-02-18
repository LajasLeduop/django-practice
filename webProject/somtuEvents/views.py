from django.shortcuts import render
from django.views import View
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from . forms import LoginForm
from .models import EventDetails
# Create your views here.


class loginuser(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('admin_request')

class logout(LogoutView):
    next_page = reverse_lazy('index')


class index(View):
    def post(self,request):
        pass


    def get(self,request):

        event_details = EventDetails.objects.all()
        data={
            'events':event_details,
        }
        return render(request, 'index.html',data)

def events(request):
    event_details = EventDetails.objects.all()
    data={
            'events':event_details,
        }
    return render(request,"events_master.html",data)

def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        venue = request.POST.get('venue')
        venue_location = request.POST.get('venue_location')
        event_details = request.POST.get('event_details')
        banner = request.FILES.get('banner')
        event_date=request.POST.get('event_date')
        active_stat=request.POST.get('is_active')
        if active_stat=="on":
            is_active=True
        else:
            is_active=False
        

        event = EventDetails(
            name=name,
            venue=venue,
            venue_location=venue_location,
            event_details=event_details,
            banner=banner,
            event_date=event_date,
            is_active = is_active
        )
        event.save()
        return HttpResponse("Success")
            # Redirect or show a success message
    else:
        return render(request, 'createevent.html')
    
def admindash(request):
    return render(request,"admin-page.html")

def event_details(request,eventid):
    return HttpResponse(f"EventID: {eventid}, Valid Path")

