from flask import Flask, render_template, request
import life_data
import uv_text


from datetime import date, timedelta

#앱 생성
app = Flask(__name__)

#url라우터
@app.route('/')
def index():

    
    city=request.args.get('city')


    city_num = ""
    if city==None : city='Seoul'
    if city =='Seoul':
        city_num=1100000000
        city='서울'
    if city =='Busan':
        city_num=2600000000
        city='부산'
    if city =='Daejeon':
        city_num=3000000000
        city='대전'
    if city =='Gwangju':
        city_num=2900000000
        city='광주'
    if city =='Jeju':
        city_num=5000000000
        city='제주'


    #오늘 날짜 추출
    now = date.today()
    now_str=now.strftime("%Y%m%d")
    yes=now-timedelta(1)
    yes_str=yes.strftime("%Y%m%d")
    

    data = life_data.get_uv_data(city_num,now_str)
    if not data[0] :
        now_str=yes_str
    data = life_data.get_uv_data(city_num,now_str)

    uv_list = uv_text.uv_list(data[0],data[1],data[2])
    
        

    return render_template('index.html',data=data, now=now_str,uv_list=uv_list,city=city) 

#메인 영역
if __name__ == "__main__":
    app.run(debug=True) 