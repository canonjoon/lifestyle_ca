from flask import Flask, render_template
import life_data

from datetime import date, timedelta

#앱 생성
app = Flask(__name__)

#url라우터
@app.route('/')
def index():
    
    #오늘 날짜 추출
    now = date.today()
    now_str=now.strftime("%Y%m%d")
    

    data = life_data.get_uv_data(1100000000,now_str)


    return render_template('index.html',data=data, now=now) 

#메인 영역
if __name__ == "__main__":
    app.run(debug=True)