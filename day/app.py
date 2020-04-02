from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sys
import click
import os
#配置数据库时报错
WIN = sys.platform.startswith('win')
if WIN:
    pre =  'sqlite:///'
else:
    pre =  'sqlite:////'
#定义
app = Flask(__name__)
#配置
app.config['SQLALCHEMY_DATABASE_URI'] = pre + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



#模型
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
#自定义命令
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop') #删除表后在创建
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')

def forge():
    db.create_all()
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
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'])
        db.session.add(movie)
    db.session.commit()
    click.echo('导入数据完成')
#首页    视图中
@app.route('/')
@app.route('/index')

def index():
    # user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)
#404
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html'),404
#模板上下文

@app.context_processor
def inject_users():
    user = User.query.first()
    return dict(name=user)
# @app.route('/index/<name>')
# def home(name):
#     print(url_for('home',name='mwy'))
#     return 'hello,%s'%name