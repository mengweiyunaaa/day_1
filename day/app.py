from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    name = 'mwy'
    movies = [
        {'title':'金瓶梅1'},
        {'title':'金瓶梅2'},
        {'title':'金瓶梅3'},
        {'title':'金瓶梅4'},
        {'title':'金瓶梅5'},
        {'title':'金瓶梅6'},
        {'title':'金瓶梅7'},
        {'title':'金瓶梅8'},
        {'title':'金瓶梅9'},
        {'title':'金瓶梅10'},
       

    ]
    return render_template('index.html',name=name,movies=movies)