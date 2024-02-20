from django.urls import path
from . import views


urlpatterns=[
    path("",views.index.as_view(),name="index"),
    path("view/events/",views.events,name="events"),
    path("create/event",views.create_event,name="create-event"),
    path("login/",views.LoginUser.as_view(),name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("admin-dash/", views.admindash,name="admindash"),
    path("eventdetail/<str:eventid>/", views.event_details, name="event_detail"),
    path("register/attendee/",views.register.as_view(),name="register_attendee"),
    path("view/registrations/",views.view_registrations,name="view_registrations")
]