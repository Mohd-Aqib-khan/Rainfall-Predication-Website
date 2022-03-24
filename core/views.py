import email
from email import message
from django.shortcuts import redirect, render
# from matplotlib.style import context
from core.models import Contact, Destination, Slider, State,News
from django.core.paginator import Paginator
from core.form import ContactForm
# Create your views here.


def index(request):
    state = ['ANDAMAN & NICOBAR ISLANDS',
             'ARUNACHAL PRADESH',
             'ASSAM & MEGHALAYA',
             'NAGA MANI MIZO TRIPURA',
             'SUB HIMALAYAN WEST BENGAL & SIKKIM',
             'GANGETIC WEST BENGAL',
             'ORISSA',
             'JHARKHAND',
             'BIHAR',
             'EAST UTTAR PRADESH',
             'WEST UTTAR PRADESH',
             'UTTARAKHAND',
             'HARYANA DELHI & CHANDIGARH',
             'PUNJAB',
             'HIMACHAL PRADESH',
             'JAMMU & KASHMIR',
             'WEST RAJASTHAN',
             'EAST RAJASTHAN',
             'WEST MADHYA PRADESH',
             'EAST MADHYA PRADESH',
             'GUJARAT REGION',
             'SAURASHTRA & KUTCH',
             'KONKAN & GOA',
             'MADHYA MAHARASHTRA',
             'MATATHWADA',
             'VIDARBHA',
             'CHHATTISGARH',
             'COASTAL ANDHRA PRADESH',
             'TELANGANA',
             'RAYALSEEMA',
             'TAMIL NADU',
             'COASTAL KARNATAKA',
             'NORTH INTERIOR KARNATAKA',
             'SOUTH INTERIOR KARNATAKA',
             'KERALA',
             'LAKSHADWEEP']

    dests = []
    for i in range(len(state)):
        dests.append(Destination())
        dests[i].name = state[i]
        dests[i].desc = "The City That Never Sleeps"
        dests[i].img = "destination_9.jpg"
        dests[i].price = 700

    st = State.objects.all()
    print(len(st))

    # paginations

    paginator = Paginator(st, 6)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)
    l = []
    for state in st:
        l.append(state.name)
    print(len(l))

    sl = Slider.objects.all()
    
    nw=News.objects.all()

    context = {
        'home': "active",
        'dests': dests,
        'states': st,
        'slider': sl,
        "news":nw,
        "page_obj": page_obj,
        "welcome":"Rainfall Home Page"
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method=="POST":
        namec=request.POST.get("names")
        emailc=request.POST.get("email")
        subjectc=request.POST.get("subject")
        messagec=request.POST.get("message")
        
        data=Contact(name=namec,email=emailc,subject=subjectc,message=messagec)
        data.save()
        return redirect('/')
    else:
        redirect('/')
    
    c=Contact.objects.all()
        
    context={
        'contact': "active",
        'welcome':"Contact Page"
    }
    
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html', {'about': "active",'welcome':"About Us Page"})
