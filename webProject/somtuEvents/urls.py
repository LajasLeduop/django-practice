from django.urls import path
from . import views


urlpatterns=[
    path("",views.index.as_view(),name="index"),
    path("view/events/",views.events,name="events"),
    path("create/event",views.create_event,name="create-event"),
    path("login/",views.loginuser.as_view(),name="login" ),
    path("admin-dash/", views.admindash,name="admindash"),
    path("logout/",views.logout.as_view(),name="logout"),
    path("eventdetail/<str:eventid>/", views.event_details, name="event_detail"),
    path("register/attendee/",views.register.as_view(),name="register_attendee"),
    path("view/registrations/",views.view_registrations,name="view_registrations")
]