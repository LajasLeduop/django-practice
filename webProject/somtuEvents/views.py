from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from . forms import LoginForm,AttendeeForm,eventform
from django.contrib.auth.decorators import login_required,permission_required
from .models import EventDetails,EventAttendee,BatchClass
from django.contrib.auth import logout
from django.contrib.auth.models import User



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
@permission_required('Somtuevents.create_event',login_url='login')
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
    event = get_object_or_404(EventDetails, pk=eventid)
    data={
        'event':event
    }
    return render(request,"event_detail.html",data)

class register(View):
    def post(self,request):
        form = AttendeeForm(request.POST)
        if form.is_valid():
            # Create an instance of the EventAttendee model but don't save it yet
            event_attendee = form.save(commit=False)
            if 'is_somtu_student' in request.POST:
                event_attendee.is_somtu_student = True
            else:
                event_attendee.is_somtu_student = False
            
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

def update_event(request,eventid):
    event = EventDetails.objects.get(pk=eventid)
    if request.method == 'POST':
        form = eventform(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
        return redirect('event_detail', eventid=eventid)
    else:
        form = eventform(instance=event)
    return render(request,"update_events.html",{'form':form})

@login_required
@permission_required('Somtuevents.delete_event',login_url='login')
def delete_event(request,eventid):
    if request.method=="POST":
        event=EventDetails.objects.get(pk=eventid)
        event.delete()
        return redirect('events')
    elif request.method == "GET":
        message={
            'type':"error",
            'message':"Sorry but this route does not support GET method."
        }
        return render(request,"message.html",message)
    

@login_required
@permission_required('Somtuevents.create_user',login_url='login')
def create_user(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        user=User.objects.create_user(username=username,password=password,email=email)
        user.is_active=False
        user.is_staff=True
        user.is_superuser=False
        user.save()
    else:
        if not request.user.is_authenticated():
            message={
                'type':'warning',
                'message':'User not Logged In'
            }
            return render(request,"login.html",message)
        else:
            return render(request,"register_admin.html")