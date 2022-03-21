from django.shortcuts import render
from core.models import Destination, Slider, State
from django.core.paginator import Paginator
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

    context = {
        'home': "active",
        'dests': dests,
        'states': st,
        'slider': sl,
        "page_obj": page_obj
    }
    return render(request, "index.html", context)


def contact(request):

    return render(request, 'contact.html', {'contact': "active"})


def about(request):
    return render(request, 'about.html', {'about': "active"})
