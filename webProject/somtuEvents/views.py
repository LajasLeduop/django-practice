from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.db.models import Count
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from . forms import LoginForm,AttendeeForm,eventform,BatchClassForm
from django.contrib.auth.decorators import login_required,permission_required
from .models import EventDetails,EventAttendee,BatchClass
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils import timezone



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
        current_datetime=timezone.now()
        currently_happening_events = EventDetails.objects.filter(event_start_date__lte=current_datetime, event_end_date__gte=current_datetime)
        upcoming_events = EventDetails.objects.filter(event_start_date__gt=current_datetime)
        data={
            'events_now':currently_happening_events,
            'events_future':upcoming_events
        }
        return render(request, 'index.html',data)

# better updated view written below instead of this
# def events(request):
#     event_details = EventDetails.objects.all()
#     data={
#             'events':event_details,
#         }
#     return render(request,"events_master.html",data)


def events(request):
    current_datetime = timezone.now()
    past_events = EventDetails.objects.filter(event_end_date__lt=current_datetime)
    currently_happening_events = EventDetails.objects.filter(event_start_date__lte=current_datetime, event_end_date__gte=current_datetime)
    upcoming_events = EventDetails.objects.filter(event_start_date__gt=current_datetime)
    data = {
        'past_events': past_events,
        'currently_happening_events': currently_happening_events,
        'upcoming_events': upcoming_events,
    }
    return render(request, "events_master.html", data)






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
    total_currently_happening_events = EventDetails.objects.filter(event_start_date__lte=timezone.now(), event_end_date__gte=timezone.now()).count()
    total_events = EventDetails.objects.count()
    total_upcoming_events = EventDetails.objects.filter(event_start_date__gt=timezone.now()).count()
    total_past_events = EventDetails.objects.filter(event_end_date__lt=timezone.now()).count()
    total_registered_attendees = EventAttendee.objects.count()
    upcoming_events=EventDetails.objects.filter(event_start_date__gt=timezone.now())[:5]
    events_with_attendee_count=upcoming_events.annotate(num_attendees=Count('eventattendee'))
    current_events=EventDetails.objects.filter(event_start_date__lte=timezone.now(), event_end_date__gte=timezone.now())[:5]
    current_with_attendee_count=current_events.annotate(num_attendees=Count('eventattendee'))

    context = {
        'total_currently_happening_events': total_currently_happening_events,
        'total_events': total_events,
        'total_upcoming_events': total_upcoming_events,
        'total_past_events': total_past_events,
        'total_registered_attendees': total_registered_attendees,
        'events_with_count':events_with_attendee_count,
        'current_with_count':current_with_attendee_count
    }
    return render(request,"admin-page.html",context)


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
@login_required
@permission_required('Somtuevents.update_event',login_url='login')
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
        if request.POST.get('is_active')=='on':
            user.is_active=True
        else:
            user.is_active=False
        if request.POST.get('is_staff')=='on':
            user.is_staff=True
        else:
            user.is_staff=False
        user.is_superuser=False

        user.has_perms(['Somtuevents.create_event', 'Somtuevents.view_event', 'Somtuevents.create_batch_class'])

        user.save()
        return redirect('login')
    else:
        
        return render(request,"register_admin.html")
    

def create_class(request):
    if request.method=="POST":
        form = BatchClassForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('index')
    else:
        form=BatchClassForm()
        return render(request,"classform.html",{'form':form})