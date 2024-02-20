from django.shortcuts import render,redirect
from django.views import View
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from . forms import LoginForm,AttendeeForm
from django.contrib.auth.decorators import login_required
from .models import EventDetails,EventAttendee,BatchClass
from django.contrib.auth import logout
# Create your views here.


class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('admin_request')


def logout_user(request):
    logout(request)
    return redirect('index')


# didn't work
# class LogoutUser(LogoutView):
#     next_page = reverse_lazy('index')


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
        form = AttendeeForm(request.POST)
        if form.is_valid():
            # Create an instance of the EventAttendee model but don't save it yet
            event_attendee = form.save(commit=False)
            if event_attendee.is_somtu_student== 'on':
                event_attendee.is_somtu_student=True
            else:
                event_attendee.is_somtu_student=False
        event_attendee.save()        
        return redirect('index')


    def get(self,request):
        form=AttendeeForm()
        classes=BatchClass.objects.all()
        data={
            'form':form,
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