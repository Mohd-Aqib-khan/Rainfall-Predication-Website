import email
from email import message
from django.shortcuts import redirect, render
# from matplotlib.style import context
from core.models import Contact, Destination, Slider, State, News, Dataset, SubscribedUsers
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
import re
# from core.form import ContactForm
# Create your views here.
from django.db.models import Avg, Sum


def index(request):

    st = State.objects.all().order_by('id')
    # paginations

    # news start

    # news end

    paginator = Paginator(State.objects.all().order_by("id"), 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
        



    l = []
    for state in st:
        l.append(state.name)

    sl = Slider.objects.all()

    nw = News.objects.all()

    overall_annual_rainfall = Dataset.objects.values(
        'YEAR').annotate(average_rainfall=Avg('ANNUAL'))

    monthly_overall_rainfall = Dataset.objects.values('YEAR').annotate(JAN=Sum('JAN'), FEB=Sum('FEB'), MAR=Sum('MAR'), APR=Sum(
        'APR'), MAY=Sum('MAY'), JUN=Sum('JUN'), JUL=Sum('JUL'), AUG=Sum('AUG'), SEP=Sum('SEP'), OCT=Sum('OCT'), NOV=Sum('NOV'), DEC=Sum('DEC'))
    total_monthly_rainfall = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0,
                              "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, "Nov": 0, "Dec": 0}

    for item in monthly_overall_rainfall:
        total_monthly_rainfall["Jan"] += item["JAN"]
        total_monthly_rainfall["Feb"] += item["FEB"]
        total_monthly_rainfall["Mar"] += item["MAR"]
        total_monthly_rainfall["Apr"] += item["APR"]
        total_monthly_rainfall["May"] += item["MAY"]
        total_monthly_rainfall["Jun"] += item["JUN"]
        total_monthly_rainfall["Jul"] += item["JUL"]
        total_monthly_rainfall["Aug"] += item["AUG"]
        total_monthly_rainfall["Sep"] += item["SEP"]
        total_monthly_rainfall["Oct"] += item["OCT"]
        total_monthly_rainfall["Nov"] += item["NOV"]
        total_monthly_rainfall["Dec"] += item["DEC"]
    monthly_rain = []
    for item in total_monthly_rainfall.values():
        monthly_rain.append(item/114)

    overall_annual_rainfall_data = {}
    for item in overall_annual_rainfall:
        overall_annual_rainfall_data[item["YEAR"]] = item["average_rainfall"]

    context = {
        'home': "active",
        'states': st,
        'slider': sl,
        "news": nw,
        "page_obj": page_obj,
        "welcome": "Rainfall Home Page",
        "line_chart": overall_annual_rainfall_data,
        "bar_chart": monthly_rain
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        namec = request.POST.get("c_names")
        emailc = request.POST.get("c_email")
        subjectc = request.POST.get("c_subject")
        messagec = request.POST.get("c_message")
        data = Contact(name=namec, email=emailc,
                       subject=subjectc, message=messagec)
        data.save()
        return redirect('/')

    c = Contact.objects.all()
    context = {
        'contact': "active",
        'welcome': "Contact Page"
    }

    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html', {'about': "active", 'welcome': "About Us Page"})


def email(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        email = request.GET.get("email")
        # names=SubscribedUsers.objects.filter().only('name')
        # print(names.values())
        # print(type(names))
        emails = SubscribedUsers.objects.values_list('email')
        t = (email,)
        if t in emails:
            return redirect('/')

        subscribedUsers = SubscribedUsers(name=name, email=email)
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'Regin Wise Rainfall Prediction'
        message = f"Hello {name} , Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return render(request, "index.html", {'res': res, 'alert_it': "alert"})
    return render(request, 'index.html')


def predictions(request):
    return render(request, "predictions.html")
