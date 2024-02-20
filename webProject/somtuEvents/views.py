from django.shortcuts import render,redirect
from django.views import View
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from . forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import EventDetails,EventAttendee,BatchClass
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        venue = request.POST.get('venue')
        venue_location = request.POST.get('venue_location')
        event_details = request.POST.get('event_details')
        banner = request.FILES.get('banner')
        event_start_date=request.POST.get('event_start_date')
        event_end_date=request.POST.get('event_end_date')
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
            event_start_date=event_start_date,
            event_end_date=event_end_date,
            is_active = is_active
        )
        event.save()
        return redirect('index')
            # Redirect or show a success message
    else:
        return render(request, 'createevent.html')
    
def admindash(request):
    return render(request,"admin-page.html")

def event_details(request,eventid):
    return HttpResponse(f"EventID: {eventid}, Valid Path")

class register(View):
    def post(self,request):
        attendee_name=request.POST.get('attendee_name')
        attendee_email=request.POST.get('attendee_email')
        attendee_phone=request.POST.get('attendee_phone')
        attendee_class=request.POST.get('attendee_class')
        attendee_is_somtu_student=request.POST.get('is_somtu_student')

        if attendee_is_somtu_student=="on":
            attendee_is_somtu_student=True
        else:
            attendee_is_somtu_student=False

        attendee=EventAttendee(
            attendee_name=attendee_name,
            attendee_email=attendee_email,
            attendee_phone=attendee_phone,
            attendee_class=attendee_class,
            is_somtu_student=attendee_is_somtu_student
        )

        attendee.save()
        return redirect('index')


    def get(self,request):
        classes=BatchClass.objects.all()
        data={
            'classes':classes
        }
        return render(request,"register_attendee.html",data)

def view_registrations(request):
    attendees=EventAttendee.objects.all()
    events=EventDetails.objects.all()
    data={
        'events':events,
        'attendees':attendees

    }
    return render(request,"view_registration.html",data)