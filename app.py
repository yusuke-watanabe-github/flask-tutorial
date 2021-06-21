from flask import Flask, render_template,request
import random

app = app = Flask(__name__)

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
