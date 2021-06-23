from flask import Flask, render_template,request
import random


app = app = Flask(__name__)

from watanabe import sub_app_w
app.register_blueprint(sub_app_w)

from yusuke import sub_app_y
app.register_blueprint(sub_app_y)

@app.route('/')
def hello():
    list=["大吉","中吉","小吉"]
    uranai = random.choice(list)
    return render_template('index.html',fortune=uranai,fortune_list=list)


if __name__ == "__main__":
    app.run(debug=True)

