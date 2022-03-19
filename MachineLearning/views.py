from django.shortcuts import render
from core.models import State
import json as simplejson
import os
import numpy as np
import pandas as pd


def removingNull(df, annual_rain_d, year_d):
    annual_mean = 0
    nan_arr = 0
    nan_jan = 0
    mean_jan = 0
    for a in annual_rain_d.keys():
        srr = pd.DataFrame(annual_rain_d[a][0])
        jdata = pd.DataFrame(annual_rain_d[a][1])
        fdata = pd.DataFrame(annual_rain_d[a][2])
        mrdata = pd.DataFrame(annual_rain_d[a][3])
        apdata = pd.DataFrame(annual_rain_d[a][4])
        madata = pd.DataFrame(annual_rain_d[a][5])
        jundata = pd.DataFrame(annual_rain_d[a][6])
        juldata = pd.DataFrame(annual_rain_d[a][7])
        audata = pd.DataFrame(annual_rain_d[a][8])
        spdata = pd.DataFrame(annual_rain_d[a][9])
        ocdata = pd.DataFrame(annual_rain_d[a][10])
        nodata = pd.DataFrame(annual_rain_d[a][11])
        dedata = pd.DataFrame(annual_rain_d[a][12])
        nan_arr = int(srr.isnull().sum())
        nan_jan = int(jdata.isnull().sum())
        nan_feb = int(fdata.isnull().sum())
        nan_mar = int(mrdata.isnull().sum())
        nan_apr = int(apdata.isnull().sum())
        nan_may = int(madata.isnull().sum())
        nan_jun = int(jundata.isnull().sum())
        nan_jul = int(juldata.isnull().sum())
        nan_aug = int(audata.isnull().sum())
        nan_sep = int(spdata.isnull().sum())
        nan_oct = int(ocdata.isnull().sum())
        nan_nov = int(nodata.isnull().sum())
        nan_dec = int(dedata.isnull().sum())
        annual_mean = (srr.mean())
        jan_mean = (jdata.mean())
        feb_mean = (fdata.mean())
        mar_mean = (mrdata.mean())
        apr_mean = (apdata.mean())
        may_mean = (madata.mean())
        jun_mean = (jundata.mean())
        jul_mean = (juldata.mean())
        aug_mean = (audata.mean())
        sep_mean = (spdata.mean())
        oct_mean = (ocdata.mean())
        nov_mean = (nodata.mean())
        dec_mean = (dedata.mean())
        if nan_arr != 0:
            df["ANNUAL"].fillna(int(annual_mean), limit=nan_arr, inplace=True)
        if nan_jan != 0:
            df["JAN"].fillna(int(jan_mean), limit=nan_jan, inplace=True)
        if nan_feb != 0:
            df["FEB"].fillna(int(feb_mean), limit=nan_feb, inplace=True)
        if nan_mar != 0:
            df["MAR"].fillna(int(mar_mean), limit=nan_mar, inplace=True)
        if nan_apr != 0:
            df["APR"].fillna(int(apr_mean), limit=nan_apr, inplace=True)
        if nan_may != 0:
            df["MAY"].fillna(int(may_mean), limit=nan_may, inplace=True)
        if nan_jun != 0:
            df["JUN"].fillna(int(jun_mean), limit=nan_jun, inplace=True)
        if nan_jul != 0:
            df["JUL"].fillna(int(jul_mean), limit=nan_jul, inplace=True)
        if nan_aug != 0:
            df["AUG"].fillna(int(aug_mean), limit=nan_aug, inplace=True)
        if nan_sep != 0:
            df["SEP"].fillna(int(sep_mean), limit=nan_sep, inplace=True)
        if nan_oct != 0:
            df["OCT"].fillna(int(oct_mean), limit=nan_oct, inplace=True)
        if nan_nov != 0:
            df["NOV"].fillna(int(nov_mean), limit=nan_nov, inplace=True)
        if nan_dec != 0:
            df["DEC"].fillna(int(dec_mean), limit=nan_dec, inplace=True)


def seperatingData(df):
    list_title = ["ANNUAL", "JAN", 'FEB', "MAR", "APR", "MAY",
                  "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    annual_rain_d = {}
    year_d = {}
    for a in range(len(df["SUBDIVISION"])):
        if not(df["SUBDIVISION"][a] in annual_rain_d.keys()):
            annual_rain_d[df["SUBDIVISION"][a]] = [[]for i in range(13)]
            year_d[df["SUBDIVISION"][a]] = []
        for i_list_title in range(len(list_title)):
            annual_rain_d[df["SUBDIVISION"][a]][i_list_title].append(
                df[list_title[i_list_title]][a])
        year_d[df["SUBDIVISION"][a]].append(df["YEAR"][a])
    return annual_rain_d, year_d


def stateComparsion(request):
    # os.chdir("D:\\DataSet")
    global annual_rain_d, year_d
    annual_data = simplejson.dumps(annual_rain_d)
    list_state = list(annual_rain_d.keys())
    data = {
        "year": year_d["ANDAMAN & NICOBAR ISLANDS"],
        "datasets": annual_data,
        "stateList": list_state
    }
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'machineLearning/statecomparsion.html', {"data": data})


def index(request):
    return render(request, 'machineLearning/index.html')


def state_view(request, sid):
    #global annual_rain_d,annual_data, year_d, annual_bar_data
    s = State.objects.get(pk=sid)
    os.chdir("D:\\DataSet")
    df = pd.read_csv("rainfall_in_india.csv")
    annual_rain_d, year_d = seperatingData(df)
    removingNull(df, annual_rain_d, year_d)
    annual_rain_d, year_d = seperatingData(df)
    annual_data = simplejson.dumps(annual_rain_d)
    annual_bar_data = []
    list_state = list(annual_rain_d.keys())
    print("stateName:-", s.name)
    annual_rain_d[s.name].append(year_d[s.name])
    A_N_test = np.transpose(annual_rain_d[s.name])
    print(len(A_N_test))
    print(len(A_N_test[0]))
    new_dataset = pd.DataFrame(A_N_test, columns=[
                               'Annual', 'Jan', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'YEAR'])
    x = new_dataset[['Annual', 'Jan', 'FEB', 'MAR', 'APR', 'MAY',
                     'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'YEAR']].values
    x_d = x.tolist()
    json_x = simplejson.dumps(x_d)
    json_columns = simplejson.dumps(
        ['Annual', 'Jan', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'YEAR'])
    bar_dataset = []
    for index in range(len(annual_rain_d[s.name])-1):
        bar_dataset.append(np.mean(annual_rain_d[s.name][index]))
    for state in annual_rain_d.values():
        annual_bar_data.append(np.mean(state[0]))
    json_bar_dataset = simplejson.dumps(bar_dataset)
    json_annual_bar_data = simplejson.dumps(annual_bar_data)
    data = {"state": s, "year": year_d[s.name], "datasets": annual_data, "stateList": list_state, "state_data": json_x,
            "columns": json_columns, "json_bar_data": json_bar_dataset, "json_annual_bar_data": json_annual_bar_data}
    return render(request, 'machineLearning/state_view.html', {"data": data})
