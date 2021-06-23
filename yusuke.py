from flask import Flask, render_template,request,Blueprint
import urllib.request, urllib.parse
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.environ.get("API_KEY")
print("API_KEY=",API_KEY)


FORECAST_API='https://api.openweathermap.org/data/2.5/forecast'

#Blueprintでモジュールの登録
sub_app_y = Blueprint('yusuke', __name__)

@sub_app_y.route('/yusuke',methods=["GET","POST"])
def yusuke():
    
    return render_template('yusuke.html')
