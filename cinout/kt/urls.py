from django.urls import path
from . import views


urlpatterns = [
   path('signup/',views.signup,name='signup'),
    #path('signup/',views.signView.as_view()),
   # path('checkin/',views.checkin,name='checkin'),
    path('checkin/',views.checkinView.as_view(),name='checkin'),

   #path('profile/',views.profile,name='profile'),
    path('profile/',views.profileView.as_view(),name='profile'),
    path('dtv/',views.date_time_view)

]