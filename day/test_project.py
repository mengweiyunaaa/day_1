import unittest

from blog import app,db
from blog.models import User,Movie

class ProjectTestCase(unittest.TestCase):
#测试固件
    def setUp(self):
        #更新配置
        app.config.update(
            #测试模式
            TESTING=True,
            #改变sqlite  安全
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'

        )
        db.create_all()
        user = User(name='Test',username='tsst')
        user.set_password('123')
        movie = Movie(title='a')
        db.session.add_all([user,movie])
        db.session.commit()
        #创建客户端
        self.client = app.test_client()
        #创建测试
        self.runner = app.test_cli_runner()
         

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    #测试app是否存在
    def test_app_exist(self):
        self.assertIsNotNone(app)

    #是否处于测试程序
    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    #测试404
    def test_404_page(self):
        response = self.client.get('/404')
        data = response.get_data(as_text=True)
        self.assertIn('404',data)
        self.assertIn('返回首页',data)
        self.assertEqual(response.status_code,404)

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('a',data)
        self.assertIn('Test',data)
        
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()
        




