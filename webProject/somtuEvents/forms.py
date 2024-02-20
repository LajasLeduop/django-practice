from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . models import *



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class eventform(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ['name', 'venue', 'venue_location', 'event_details', 'banner','event_start_date','event_end_date','is_active']


class AttendeeForm(forms.ModelForm):
    attendee_class = forms.ModelChoiceField(queryset=BatchClass.objects.all(), label="Attendee Class")

    class Meta:
        model = EventAttendee
        fields = ['attendee_name', 'attendee_email','attendee_phone','attendee_class','is_somtu_student','event']