import requests
import xmltodict
import json

def get_corona_data(startCreateDt,endCreateDt):
    #서비스키는 디코딩해서 대입.
    url ="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    parms ={
        'serviceKey':"mJyLI50asz7Qv7PlHdjciQEMK2dW7AvSUP07dFSHJeMkzRCSAcnVgramtTjyOYjm/ZLruxESJUEvW6UBcf6VSA==",
        'pageNo':'1',
        'numOfRows':'10',
        'startCreateDt':startCreateDt,
        'endCreateDt':endCreateDt
    }

    res=requests.get(url, params=parms)
    #print(res.url)
    #print(res.text)

    #xml to dict
    dict_data =xmltodict.parse(res.text)
    #print(dict_data)

    #dict -> json
    json_data = json.dumps(dict_data)
    #print(json_data)

    #json -> dict
    dict_data = json.loads(json_data)
    #print(dict_data['response']['header']['resultCode'])
    #print(dict_data['response']['body']['items']['item'])

    #토탈 카운터로 에러 상황 확인.
    totalCount = dict_data['response']['body']['totalCount']
    if totalCount =="0":
        return False

    #지역정보 리스트
    area_data =dict_data['response']['body']['items']['item']
    area_data.reverse()
    #print(area_data)

    return area_data