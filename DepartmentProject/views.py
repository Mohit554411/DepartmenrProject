import re
from turtle import title
from django.shortcuts import render
from faculty.models import FacultyDetails
from activity.models import ActivityDetails
from syllabus.models import SyllabusDetails
from recruiter.models import RecruiterDetails
from placementDetail.models import PlacementDetail
from django.core.paginator import Paginator
from event.models import EventDetails
from enquiryDetail.models import EnquiryDetail
def home(request):
    facultyDetails = FacultyDetails.objects.get(id=1)
    data={
        'title':'CSE Department',
        'facultyDetails':facultyDetails
    }
    return render(request,"index.html",data)

def about(request):
    syllabusDetails = SyllabusDetails.objects.all()
    data={
        'title':'About',
        'syllabusDetails':syllabusDetails
    }
    return render(request,"About.html",data)

def faculty(request):
    facultyDetails = FacultyDetails.objects.all()
    data={
        'title':'Faculty',
        'facultyDetails':facultyDetails
    }
    return render(request,"Faculty.html",data)

def events(request):
    eventTitle = {}
    eventDetails = EventDetails.objects.all()
    for n in eventDetails:
        if n.title not in eventTitle:
            eventTitle[n.title]=n.imgs
    data={
        'title':'Events',
        'eventDetails':eventDetails,
        'eventTitle':eventTitle
    }
    return render(request,"Events.html",data)
def eventDetails(request,title):
    eventDetails = EventDetails.objects.all().filter(title = title)
    data={
        'title':title,
        'eventDetails':eventDetails
    }
    return render(request,"EventDetails.html",data)
def upcomingevents(request):
    data={
        'title':'Upcomung Events'
    }
    return render(request,"UpcomingEvents.html",data)

def activity(request):
    activityDetails = ActivityDetails.objects.all()
    data={
        'title':'Activity',
        'activityDetails':activityDetails
    }
    return render(request,"Activity.html",data)

def placements(request):
    data={
        'title':'Placements'
    }
    return render(request,"Placements.html",data)

def ourRecruiter(request):
    recruiterDetails = RecruiterDetails.objects.all()
    paginator = Paginator(recruiterDetails,10)
    if( request.GET.get('page')==None):
        page_num = request.GET.get('page')
    else:
        page_num = int(request.GET.get('page'))
    finalPage = paginator.get_page(page_num)
    totalPage = finalPage.paginator.num_pages
    data={
        'title':'OurRecruiter',
        'recruiterDetails': finalPage,
        'totalPage':[n+1 for n in range(totalPage)],
        'page_num':page_num
    }
    print(page_num)
    return render(request,"OurRecruiter.html",data)

def placementTraining(request):
    data={
        'title':'PlacementTraining'
    }
    return render(request,"PlacementTraining.html",data)

def placementAchievement(request):
    placementDetail = PlacementDetail.objects.all()
    if request.method == "POST":
        name = request.POST.get('Name')
        print(name)
        if len(name) != 0:
            placementDetail = PlacementDetail.objects.all().filter(student_name__icontains=name)
    paginator = Paginator(placementDetail,25)
    if( request.GET.get('page')==None):
        page_num = request.GET.get('page')
    else:
        page_num = int(request.GET.get('page'))
    finalPage = paginator.get_page(page_num)
    totalPage = finalPage.paginator.num_pages
    
    data={
        'title':'PlacementAchievement',
        'placementDetail': finalPage,
        'totalPage':[n+1 for n in range(totalPage)],
        'page_num':page_num
    }
    return render(request,"PlacementAchievement.html",data)

def facility(request):
    data={
        'title':'Facility'
    }
    return render(request,"Facility.html",data)

def contact(request):
    data={
        'title':'Contact'
    }
    return render(request,"Contact.html",data)

def thankYou(request):
    data = {}
    try:
        name = request.POST['name'].capitalize()
        subject = request.POST['subject'].capitalize()
        email = request.POST['email'].capitalize()
        mobile = request.POST['mobile']
        msg = request.POST['msg'].capitalize()
        enquiry_details = EnquiryDetail(name=name,email=email,mobile=mobile,subject=subject,msg=msg)
        enquiry_details.save()
        data ={
            'title' : 'ThankYou',
            'name' : name,
            'email' : email,    
        }
    except:
        pass
    return render(request,"ThankYou.html",data)

def footerDetails(request,footer):
    data={
        'title':footer
    }
    if(footer == 'r&d'):
        return render(request,"R&D.html",data)
    elif(footer == 'bos'):
        return render(request,"BOS.html",data)