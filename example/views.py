
from django.shortcuts import render
from home.models import Marks_Of_User
from .models import Banner, Events, Masessage , Services , About , Gallary, links , Classcis , Title , Profile
from django.core.exceptions import ObjectDoesNotExist


banner=Banner.objects.all().filter(status=True)
events=Events.objects.all().filter(status=True)
services=Services.objects.all().filter(status=True)
about=About.objects.all().filter(status=True)
masessage=Masessage.objects.all().filter(status=True)
gallary=Gallary.objects.all().filter(status=True)
link=links.objects.all().filter(status=True)
classcis=Classcis.objects.all().filter(status=True)
title=Title.objects.all().filter(status=True)
# Create your views here.
def home(request):
    
    return render(request,'user/index.html',{'banner':banner,'events':events,'Services':services,'About':about,'Masessage':masessage,'gallary':gallary,'links':link,'classcis':classcis,'title':title})

def Service(request):
    return render(request,'user/service.html',{'Services':services,'About':about,'links':link})
def contact(request):
    return render(request,'user/contact.html',{'About':about,'links':link,})
def profile(request):
    try:
        marks = Marks_Of_User.objects.filter(user=request.user)
        profile = Profile.objects.get(user=request.user)
        quiz_data = []
        for mark in marks:
            quiz_data.append({
                'mark': mark,
                'quiz': mark.quiz
            })
        return render(request,'user/profile.html',{'profile': profile,'marks':marks,'quiz_data': quiz_data})
    except ObjectDoesNotExist:
        return render(request, 'user/profile_not_found.html')
    