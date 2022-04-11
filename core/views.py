import email
from email import message
from django.shortcuts import redirect, render,HttpResponseRedirect
# from matplotlib.style import context
from core.models import Contact, Destination, Slider, State,News,Dataset
from django.core.paginator import Paginator
# from core.form import ContactForm
# Create your views here.
from django.db.models import Avg, Sum

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

    st = State.objects.all().order_by('id')
    

    # paginations

    paginator = Paginator(st, 6)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)
    l = []
    for state in st:
        l.append(state.name)
    

    sl = Slider.objects.all()
    
    nw=News.objects.all()

    overall_annual_rainfall = Dataset.objects.values('YEAR').annotate(average_rainfall=Avg('ANNUAL'))
    
    monthly_overall_rainfall = Dataset.objects.values('YEAR').annotate(JAN=Sum('JAN'),FEB=Sum('FEB'),MAR=Sum('MAR'),APR=Sum('APR'),MAY=Sum('MAY'),JUN=Sum('JUN'),JUL=Sum('JUL'),AUG=Sum('AUG'),SEP=Sum('SEP'),OCT=Sum('OCT'),NOV=Sum('NOV'),DEC=Sum('DEC'))
    total_monthly_rainfall = {"Jan":0,"Feb":0,"Mar":0,"Apr":0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0,"Dec":0}    

    for item in monthly_overall_rainfall:
        total_monthly_rainfall["Jan"] +=item["JAN"]
        total_monthly_rainfall["Feb"] +=item["FEB"]
        total_monthly_rainfall["Mar"] +=item["MAR"]
        total_monthly_rainfall["Apr"] +=item["APR"]
        total_monthly_rainfall["May"] +=item["MAY"]
        total_monthly_rainfall["Jun"] +=item["JUN"]
        total_monthly_rainfall["Jul"] +=item["JUL"]
        total_monthly_rainfall["Aug"] +=item["AUG"]
        total_monthly_rainfall["Sep"] +=item["SEP"]
        total_monthly_rainfall["Oct"] +=item["OCT"]
        total_monthly_rainfall["Nov"] +=item["NOV"]
        total_monthly_rainfall["Dec"] +=item["DEC"]
    monthly_rain = []
    for item in total_monthly_rainfall.values():
        monthly_rain.append(item/114)

    overall_annual_rainfall_data = {}
    for item in overall_annual_rainfall:
        overall_annual_rainfall_data[item["YEAR"]] = item["average_rainfall"]
        
    context = {
        'home': "active",
        'dests': dests,
        'states': st,
        'slider': sl,
        "news":nw,
        "page_obj": page_obj,
        "welcome":"Rainfall Home Page",
        "line_chart": overall_annual_rainfall_data,
        "bar_chart": monthly_rain
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
    
    c=Contact.objects.all()
    context={
        'contact': "active",
        'welcome':"Contact Page"
    }
    
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html', {'about': "active",'welcome':"About Us Page"})

def sign_up(request):
    return render(request,'signup.html')
