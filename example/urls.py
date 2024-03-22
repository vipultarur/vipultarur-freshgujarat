from django.urls import path
from . import views,userviews
urlpatterns = [
    path('',views.home,name='home'),
    path('user/login',userviews.userlogin,name='userlogin'),
    path('user/signup/',userviews.signup,name='signup'),
    path('user/signout/',userviews.signout,name='signout'),
    path('user/contact/',userviews.contact,name='contact'),
    path('service/',views.Service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('user/profile',views.profile,name='profile'),
]