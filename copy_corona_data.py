import requests
import xmltodict
import json

url ="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

parms ={
    'serviceKey':"mJyLI50asz7Qv7PlHdjciQEMK2dW7AvSUP07dFSHJeMkzRCSAcnVgramtTjyOYjm/ZLruxESJUEvW6UBcf6VSA==",
    'pageNo':'1',
    'numOfRows':'10',
    'startCreateDt':'20200710',
    'endCreateDt':'20200710'
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
print(dict_data['response']['header']['resultCode'])
print(dict_data['response']['body']['items'])

