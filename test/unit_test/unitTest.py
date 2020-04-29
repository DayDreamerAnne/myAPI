import tempfile
import os
from src.model.user import User
import pytest
from flask import app
#from flask import create_app
# from flaskr.db import get_db, init_db


@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()

    def teardown():
        app.config['TESTING'] = False
    request.addfinalizer(teardown)

    return client


def login(client, userid, password):
    return client.post('/login', data=dict(
        userid=userid,
        password=password
    ), follow_redirects=True)

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app('flask_test.cfg')
#
#     # Flask provides a way to test your application by exposing the Werkzeug test Client
#     # and handling the context locals for you.
#     testing_client = app.test_client()
#
#     # Establish an application context before running the tests.
#     ctx = flask_app.app_context()
#     ctx.push()
#
#     yield testing_client  # this is where the testing happens!
#
#     ctx.pop()


def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200


def test_login(client):
    """Test login"""
    userid=''
    password=''
    rv = login(client, userid,password)
    assert b'logged in' in rv.data

# @pytest.fixture
# def app():
#     db_fd, db_path = tempfile.mkstemp()
#
#     app = create_app({
#         'TESTING': True
#     })
#
#     with app.app_context():
#         init_db()
#         get_db().executescript(_data_sql)
#
#     yield app
#
#     os.close(db_fd)
#     os.unlink(db_path)
#
#
# @pytest.fixture
# def client ():
#     # db_fd
#     # tempfile 模块可以创建一个临时的数据库和初始化它。
#     db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#     flaskr.app.config['TESTING'] = True
#
#     with flaskr.app.test_client() as client:
#         with flaskr.app.app_context():
#             flaskr.init_db()
#         yield client
#
#     os.close(db_fd)
#     os.unlink(flaskr.app.config['DATABASE'])
#
#
# with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
#     _data_sql = f.read().decode('utf8')