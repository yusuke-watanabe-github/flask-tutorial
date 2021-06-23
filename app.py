from flask import Flask, render_template,request
import random

import os
from dotenv import load_dotenv

import urllib.request, urllib.parse
import json

load_dotenv()
API_KEY=os.environ.get("API_KEY")
print("API_KEY=",API_KEY)

FORECAST_API='https://api.openweathermap.org/data/2.5/forecast'


app = app = Flask(__name__)

@app.route('/forecast',methods=["GET","POST"])
def forecast():
    setplace=''
    if request.method == "POST":
        setplace = request.form["place"]
    else:
        setplace='Tokyo'
    
    params = {
        'appid' : API_KEY,
        'q' : setplace,
        'units' : 'metric'
    }
    url = FORECAST_API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    result = res.read().decode('utf-8')    
    res.close()

    json_body = json.loads(result)

    forecasts = []
    for api_data in json_body["list"]:
        forecasts.append({
            "time": api_data["dt_txt"],
            "temp": api_data["main"]["temp"],
            "humidity": api_data["main"]["humidity"],
            "pressure": api_data["main"]["pressure"],
            "icon": api_data["weather"][0]["icon"],
        })

    return render_template('forecast.html',forecasts=forecasts,setplace=setplace)


@app.route('/')
def hello():
    list=["大吉","中吉","小吉"]
    uranai = random.choice(list)
    return render_template('index.html',fortune=uranai,fortune_list=list)



@app.route('/fortune',methods=["GET","POST"])
def fortune():
    list=["大吉","中吉","小吉"]

    if request.method == "POST":
        pcomment = request.form["comment"]
        numofdays = int(request.form["num_of_days"])
        uranai_list=[]

        for i in range(numofdays):
            uranai_list.append(
                {"day":str(i+1)+"日目","fortune":random.choice(list)}
            )
        return render_template('fortune.html',fortune_list=uranai_list,comment=pcomment)

    else:
        flist = [
            {"day":"今日","fortune":random.choice(list)},
            {"day":"明日","fortune":random.choice(list)},
            {"day":"明後日","fortune":random.choice(list)}
        ]
        return render_template('fortune.html',fortune_list=flist)

if __name__ == "__main__":
    app.run(debug=True)

