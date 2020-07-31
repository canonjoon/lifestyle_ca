import requests
import xmltodict
import json

#깃허브 푸시는 origin2 로 작업진행.

#http://apis.data.go.kr/1360000/LivingWthrIdxService/getUVIdx
# serviceKey=mJyLI50asz7Qv7PlHdjciQEMK2dW7AvSUP07dFSHJeMkzRCSAcnVgramtTjyOYjm%2FZLruxESJUEvW6UBcf6VSA%3D%3D 디코딩전
# pageNo=1
# numOfRows=10
# dataType=XML
# areaNo=
# time=2020073006

#url='http://fow.kr/find/{}'.format(넣고 싶은 텍스트)

#자외선 지수 조회로 변경.

def get_uv_data(areaNo,time):
    url ="http://apis.data.go.kr/1360000/LivingWthrIdxService/getUVIdx"
    parms ={
        'serviceKey':"mJyLI50asz7Qv7PlHdjciQEMK2dW7AvSUP07dFSHJeMkzRCSAcnVgramtTjyOYjm/ZLruxESJUEvW6UBcf6VSA==",
        'pageNo':'1',
        'numOfRows':'10',
        'dataType':'XML',
        'areaNo' :areaNo, #지역 코드,서울 1100000000
        'time':str(time)+'06',
    }

    try:
        res=requests.get(url, params=parms)
        #print(res.url)
        #print(res.text)
    except ValueError:
        print("데이터 포탈에 연결이 되지 않습니다... 잠시후 시도해 보세요")

    #xml to dict
    dict_data =xmltodict.parse(res.text)
    #print(dict_data)

    #dict -> json
    json_data = json.dumps(dict_data)
    #print(json_data)

    #json -> dict

    dict_data = json.loads(json_data)
    #print(dict_data['response']['header']['resultCode'])
    #print(dict_data['response']['body']['items'])

    uv_td = dict_data['response']['body']['items']['item']['today']
    #print(uv_data)
    uv_tm = dict_data['response']['body']['items']['item']['tomorrow']
    uv_dtm = dict_data['response']['body']['items']['item']['theDayAfterTomorrow']
    


    return uv_td,uv_tm,uv_dtm

#테스트용
if __name__ == "__main__":
    print(get_uv_data(2600000000,20200729))