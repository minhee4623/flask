from flask import Flask

# create_app() 이 실행되면 내부에 함수들이 모두 동작을 하게 된다
def create_app():
    # Flask는 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식해서 거기부터 코드를 찾아나갑니다.
    # Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return f'Hello, {__name__}'

    # 라우팅 주소를 만드실 때는 /경로명 까지만 적어줍니다. 
    # 그 다음에 만들어질 하위 경로도 /경로명 
    @app.route('/yeonji')
    def hello_yeonji():
        return f'Hello, yeonji'

    @app.route('/jjangu')
    def hello_jjangu():
        return f'<b> JJANGGU </b>'
    
    return app

#set FLASK_DEBUG= true는 서버를 끄지않아도 바로바로 동기된다 
#1. github 레파지토리 만든다
#2. 로컬 저장소에 텅 빈 폴더를 만든다 
#3. github 원격 저장소와 우리 컴퓨터의 텅빈 폴더(로컬저장소)를 연결한다
#4. 텅 빈 가상환경을 만든다(python -m venv 가상환경명)
#5. 가상환경의 pip를 업그레이드 하고, flask  패키지를 설치한다 
# app.py 만들고
# 매번 실행할 때 가상환경에 들어가고, set FLASK_DEBUG = true 로 만든다.


