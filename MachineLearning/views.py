from django.shortcuts import render
from core.models import State,Dataset
from django.core import serializers
from django.db.models import Avg, Count
import json as simplejson
import os
import numpy as np
import pandas as pd


def stateComparsion(request):
    # os.chdir("D:\\DataSet")
    stateName = Dataset.objects.values_list('SUBDIVISION', flat=True).distinct()
    dataset = Dataset.objects.all()
    json_dataset=serializers.serialize("json",dataset)
    
    # os.chdir("D:\\DataSet")
    # df = pd.read_csv("rainfall_in_india.csv")
    # annual_rain_d, year_d = seperatingData(df)
    # df = removingNull(df, annual_rain_d, year_d)
    # annual_rain_d, year_d = seperatingData(df)
    # annual_data = simplejson.dumps(annual_rain_d)
    # list_state = list(annual_rain_d.keys())
    parameter = ["ANNUAL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    data = {
        "dataset": json_dataset,
        "stateList": list(stateName),
        "parameter": parameter
    }
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'machineLearning/statecomparsion.html', {"data": data,"welcome":"State Comparison"})

def index(request):
    return render(request, 'machineLearning/index.html')



def state_view(request, sid):
    #global annual_rain_d,annual_data, year_d, annual_bar_data
    # Loading Data from local disk 
    
    s = State.objects.get(pk=sid)
<<<<<<< HEAD
    A_N=Dataset.objects.filter(SUBDIVISION=s.name)
    All_State_Annual_Rainfall = Dataset.objects.values('SUBDIVISION').annotate(average_rainfall=Avg('ANNUAL'))
    All_State_Data = []
    All_State_Annual_Rainfall_data = []
    for item in All_State_Annual_Rainfall:
        for name,value in item.items():
            if(name=="SUBDIVISION"):
                All_State_Data.append(value)
            else:
                All_State_Annual_Rainfall_data.append(value)
        
    Grid_Table_data=serializers.serialize("json",A_N)
    annual_rainfall_data = A_N.values_list('YEAR', 'ANNUAL')
    linear_chart_data = simplejson.dumps(dict(annual_rainfall_data))
    mouthily_rainfall_data = Dataset.objects.filter(SUBDIVISION=s.name).aggregate(JAN=Avg('JAN'),FEB=Avg('FEB'),MAR=Avg('MAR'),APR=Avg('APR'),MAY=Avg('MAY'),JUN=Avg('JUN'),JUL=Avg('JUL'),AUG=Avg('AUG'),SEP=Avg('SEP'),OCT=Avg('OCT'),NOV=Avg('NOV'),DEC=Avg('DEC'))
    
    sessional_rainfall_data =  Dataset.objects.filter(SUBDIVISION=s.name).aggregate(Jan_Feb=Avg('Jan_Feb'),Mar_May=Avg('Mar_May'),Jun_Sep=Avg('Jun_Sep'),Oct_Dec=Avg('Oct_Dec'))
    
=======
    os.chdir("E:\P\Rain\media\CSV")
    df = pd.read_csv("rainfall_in_india.csv")
    # setting data into state-wise
    annual_rain_d, year_d = seperatingData(df)
    # Removing null value from dataset
    removingNull(df, annual_rain_d, year_d)
    # setting data into state-wise
    annual_rain_d, year_d = seperatingData(df)

    annual_data = simplejson.dumps(annual_rain_d)
    annual_bar_data = []
    list_state = list(annual_rain_d.keys())
    print("stateName:-", s.name)
    annual_rain_d[s.name].insert(0,year_d[s.name])
    A_N_test = np.transpose(annual_rain_d[s.name])
    print(len(A_N_test))
    print(len(A_N_test[0]))
    new_dataset = pd.DataFrame(A_N_test, columns=[
                               'YEAR', 'Annual', 'Jan', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])
    x = new_dataset[['YEAR', 'Annual', 'Jan', 'FEB', 'MAR', 'APR', 'MAY',
                     'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].values
    x_d = x.tolist()
    json_x = simplejson.dumps(x_d)
>>>>>>> 89084d8a28081ec6f53c4b060f3ec802e02efad4
    json_columns = simplejson.dumps(
        ['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',"ANNUAL","Jan_Feb","Mar_May","Jun_Sep","Oct_Dec"])
    
    data = {"state": s,
            "line_chart": linear_chart_data,
            "stateList": All_State_Data,
            "state_data":Grid_Table_data,
            "columns": json_columns, 
            "json_pie_data": list(sessional_rainfall_data.values()),
            "json_bar_data": list(mouthily_rainfall_data.values()),
            "json_annual_bar_data": All_State_Annual_Rainfall_data
            
    }

    
    return render(request, 'machineLearning/state_view.html', {"data": data,"welcome":"State View"})
# machineLearning/state_view.html

# os.chdir("D:\\DataSet")
# df = pd.read_csv("rainfall_in_india.csv")
# annual_rain_d, year_d = seperatingData(df)
# df = removingNull(df, annual_rain_d, year_d)
# annual_rain_d, year_d = seperatingData(df)
# for i in annual_rain_d.keys():
#     for a in range(len(annual_rain_d[i][0])):
#         c = Dataset(SUBDIVISION=i, YEAR=year_d[i][a], JAN=annual_rain_d[i][1][a], FEB=annual_rain_d[i][2][a], MAR=annual_rain_d[i][3][a], APR=annual_rain_d[i][4][a], MAY=annual_rain_d[i][5][a], JUN=annual_rain_d[i][6][a], JUL=annual_rain_d[i]
#                     [7][a], AUG=annual_rain_d[i][8][a], SEP=annual_rain_d[i][9][a], OCT=annual_rain_d[i][10][a], NOV=annual_rain_d[i][11][a], DEC=annual_rain_d[i][12][a], ANNUAL=annual_rain_d[i][0][a], Jan_Feb=annual_rain_d[i][14][a], Mar_May=annual_rain_d[i][15][a], Jun_Sep=annual_rain_d[i][16][a], Oct_Dec=annual_rain_d[i][17][a])
#         c.save()

# A_N=Dataset.objects.filter(SUBDIVISION="ANDAMAN & NICOBAR ISLANDS")
# post_list=serializers.serialize("json",A_N)
# print(post_list)