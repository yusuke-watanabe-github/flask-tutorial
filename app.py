from flask import Flask
app = app = Flask(__name__)

@app.route('/')
def hello():
#    return "Hello world"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)