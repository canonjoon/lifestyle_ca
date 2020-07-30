from flask import Flask, render_template
import life_data
import test

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
    uv_list = test.uv_list(data[0],data[1],data[2])
    print(data[0])       

    return render_template('index.html',data=data, now=now,uv_list=uv_list) 

#메인 영역
if __name__ == "__main__":
    app.run(debug=True)