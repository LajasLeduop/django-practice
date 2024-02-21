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
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['name'].initial = instance.name
            self.fields['venue'].initial = instance.venue
            self.fields['venue_location'].initial = instance.venue_location
            self.fields['event_details'].initial = instance.event_details
            self.fields['event_start_date'].initial = instance.event_start_date
            self.fields['event_end_date'].initial = instance.event_end_date
            self.fields['is_active'].initial = instance.is_active
          
class AttendeeForm(forms.ModelForm):
    attendee_class = forms.ModelChoiceField(queryset=BatchClass.objects.all(), label="Attendee Class")

    class Meta:
        model = EventAttendee
        fields = ['attendee_name', 'attendee_email','attendee_phone','attendee_class','is_somtu_student','event']