from flask import Flask, render_template, request

# initializing Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('register.html')


@app.route('/display')
def displayData():

    myname = "Mubassir"

    fruits = ['Apple', 'PineApple', 'Orange', 'Guava', 'Strwberry']

    return render_template('view.html', name=myname, fruits_data=fruits)


app.run(debug=True)