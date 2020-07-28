from flask import Flask, render_template
import corona_data
from datetime import date, timedelta

#앱 생성
app = Flask(__name__)

#url라우터
@app.route('/')
def index():
    #20200728-오늘
    now = date.today()
    now_str=now.strftime("%Y%m%d")
    #print(now_str)

    data = corona_data.get_corona_data(now_str,now_str)
    #없으면 어제 날짜로 요청.
    if not data :
        yesterday = now - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y%m%d")
        print(yesterday_str)

        data = corona_data.get_corona_data(yesterday_str,yesterday_str)
    
    #print(data)


    return render_template('index.html',data=data[1:]) #합계가 [0]이라, 합계를 빼고 보냄

#메인 영역
if __name__ == "__main__":
    app.run(debug=True)