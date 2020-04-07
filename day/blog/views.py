from flask import Flask,render_template,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from blog import db,app
from blog.models import User,Movie
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash
#首页    视图中
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])

def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('未登录不能添加')
            return redirect(url_for('index'))
        title = request.form.get('title')
        if not title:
            
            flash('请输入')
            return redirect(url_for('index'))
        movie = Movie(title=title)
        db.session.add(movie)
        db.session.commit()
        flash('ok')
        return redirect(url_for('index'))


    # user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

#改   编辑
@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        if not title:
            
            flash('请输入')
            return redirect(url_for('edit'),movie_id=movie_id)
        movie.title = title
       
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('index'))
    
    return render_template('edit.html',movie=movie)
#删
@app.route('/movie/delete/<int:movie_id>',methods=['GET','POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('index'))
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('错误')
            return redirect(url_for('login'))

        user = User.query.first()
        #验证信息是否一致

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登陆成功')
            return redirect(url_for('index'))
        
        flash('验证错误')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash('已注销')
    return redirect(url_for('index')) 



#设置
@app.route('/settings',methods=['GET','POST'])
@login_required
def settings():
    if request.method == 'post':
        name = request.form['name']
        if not name or len(name) > 20:
            flash('输入非法')
            return redirect(url_for('settings'))
        current_user.name = name
        db.session.commit()
        flash('设置name成功')
        return redirect(url_for('index'))
    return render_template('settings.html')