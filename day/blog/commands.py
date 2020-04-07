

import click

from blog.models import User,Movie
from blog import app,db
#自定义命令
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop') #删除表后在创建
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')
#导入数据
@app.cli.command()
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

#生成管理员账户
@app.cli.command()
@click.option('--username',prompt=True,help='用户名')
@click.option('--password',prompt=True,help='密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    db.create_all()
    user = User.query.first()
    if user:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
        click.echo('1')
    else:
        click.echo('创新用户')
        user = User(username=username,name='mwy')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('完成')