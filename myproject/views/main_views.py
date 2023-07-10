# views\,main_views.py
from flask import Blueprint

# Blueprint 클래스를 통해 임의의 객체를 만듭니다
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello():
    return f'Hello, {__name__}'

# 라우팅 주소를 만드실 때는 /경로명 까지만 적어줍니다. 
# 그 다음에 만들어질 하위 경로도 /경로명 
@bp.route('/yeonji')
def hello_yeonji():
    return f'Hello, yeonji'

@bp.route('/jjangu')
def hello_jjangu():
    return f'<b> JJANGGU </b>'
    