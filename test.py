from datetime import date, timedelta
import corona_data

#20200728-오늘
now = date.today()
now_str=now.strftime("%Y%m%d")
#print(now.strftime("%Y%m%d"))

data = corona_data.get_corona_data('20200729','20200729')
#없으면 어제 날짜로 요청.
if not data :
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    print(yesterday_str)

    data = corona_data.get_corona_data(yesterday_str,yesterday_str)

    print(data)