import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

endpoint ="http://openapi.airport.co.kr/service/rest/AirportParkingCongestion/airportParkingCongestionRT"
encoding = 'h9EMgEqNQe%2FpkgtZ3GSuF3JRkmpH7mVbBwyQlpkI8iM68JmNq%2Fd%2BlCwXQi8Tbam2eFEswznPPY4GnEtqs2rNMg%3D%3D'
decoding = 'h9EMgEqNQe/pkgtZ3GSuF3JRkmpH7mVbBwyQlpkI8iM68JmNq/d+lCwXQi8Tbam2eFEswznPPY4GnEtqs2rNMg=='
    
# 공항코드
# GMP  김포국제공항
# PUS  김해국제공항
# CJU  제주국제공항
# TAE  대구국제공항
# KWJ  광주공항

print('원하시는 공항의 코드를 입력해주시오 :')
airport_code = input()


url = f"{endpoint}?schAirportCode={airport_code}&serviceKey={encoding}&numOfRows=10&pageNo=1"

result = requests.get(url)
soup = BeautifulSoup(result.text,"lxml")
items = soup.find_all("item")


parking_able_max = 0
result_airport_name = ''
total = 0
congetion = []

for item in items:
    parking_in = item.find('parkingOccupiedSpace').get_text() # 현재 주차되어져있는 대수
    parking_total = item.find('parkingTotalSpace').get_text() # 주차장 총 가능한 주차대수
    parking_name = item.find('parkingAirportCodeName').get_text() # 주차장 이름
    parking_con = item.find('parkingCongestion').get_text() # 혼잡도 (%)

    parking_able_max = parking_total - parking_in #현재 주차가능한 대수

    if parking_able_max > total:
        #최종 결과 변수 초기화
        result_airport_name = '' 
        congetion = []

        # 최종 결과값 입력
        result_airport_name = parking_name # 가장 여유로운 주차장 이름
        total = parking_able_max # 주차 가능 대수
        congetion = parking_con  # 혼잡도



print(f"현재 가장 여유있는 주차장은 {result_airport_name} 이며 주차가 가능한 대수는 {total}대 가능합니다. 혼잡도 : {congetion}")




    
    







