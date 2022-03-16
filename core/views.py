from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    state = ['ANDAMAN & NICOBAR ISLANDS', 
    'ARUNACHAL PRADESH',
    'ASSAM & MEGHALAYA',
    'NAGA MANI MIZO TRIPURA',
    'SUB HIMALAYAN WEST BENGAL & SIKKIM',
    'GANGETIC WEST BENGAL',
    'ORISSA', 'JHARKHAND',
    'BIHAR',
    'EAST UTTAR PRADESH','WEST UTTAR PRADESH',
    'UTTARAKHAND',
    'HARYANA DELHI & CHANDIGARH',
    'PUNJAB','HIMACHAL PRADESH',
    'JAMMU & KASHMIR','WEST RAJASTHAN',
    'EAST RAJASTHAN',
    'WEST MADHYA PRADESH',
    'EAST MADHYA PRADESH','GUJARAT REGION',
    'SAURASHTRA & KUTCH',
    'KONKAN & GOA',
    'MADHYA MAHARASHTRA','MATATHWADA',
    'VIDARBHA',
    'CHHATTISGARH',
    'COASTAL ANDHRA PRADESH','TELANGANA',
    'RAYALSEEMA',
    'TAMIL NADU',
    'COASTAL KARNATAKA','NORTH INTERIOR KARNATAKA',
    'SOUTH INTERIOR KARNATAKA',
    'KERALA',
    'LAKSHADWEEP']

    
    dests = []
    for item in range(len(state)):
        dests.append(Destination())
        dests[item].name = state[item]
        dests[item].desc = "The City That Never Sleeps"
        dests[item].img = "destination_1.jpg"
        dests[item].price = 700

    return render(request, "index.html", {'dests': dests})
