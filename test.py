from datetime import date, timedelta
import corona_data

#20200728-오늘
now = date.today()
now_str=now.strftime("%Y%m%d%H")
print(now.strftime("%Y%m%d%H"))

data = corona_data.get_corona_data('20200729','20200729')
#없으면 어제 날짜로 요청.
if not data :
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    print(yesterday_str)

    data = corona_data.get_corona_data(yesterday_str,yesterday_str)

    #print(data)

def uv_list(data1,data2,data3):
    uv_list=""
    uv_list2=""
    uv_list3=""
    data_int1 =int(data1)
    data_int2 =int(data2)
    data_int3 =int(data3)

    if data_int1 >10 :
        uv_list = "위험"
    if data_int1 <11 and data_int1>7 :
        uv_list = "아주 높음"
    if  data_int1<8 and data_int1>5 :
        uv_list = "높음"
    if  data_int1<6 :
        uv_list = "안전함"


    if data_int2 >10 :
        uv_list2 = "위험"
    if data_int2 <11 and data_int2>7 :
        uv_list2 = "아주 높음"
    if  data_int2<8 and data_int2>5 :
        uv_list2 = "높음"
    if  data_int2<6 :
        uv_list2 = "안전함"

    

    if data_int3 >10 :
        uv_list3 = "위험"
    if data_int3 <11 and data_int3>7 :
        uv_list3 = "아주 높음"
    if  data_int3<8 and data_int3>5 :
        uv_list3 = "높음"
    if  data_int3<6 :
        uv_list3 = "안전함"


    return uv_list,uv_list2,uv_list3


