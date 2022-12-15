import requests
import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

encoding = 'h9EMgEqNQe%2FpkgtZ3GSuF3JRkmpH7mVbBwyQlpkI8iM68JmNq%2Fd%2BlCwXQi8Tbam2eFEswznPPY4GnEtqs2rNMg%3D%3D'
decoding = 'h9EMgEqNQe/pkgtZ3GSuF3JRkmpH7mVbBwyQlpkI8iM68JmNq/d+lCwXQi8Tbam2eFEswznPPY4GnEtqs2rNMg=='
    
endpoint ="http://openapi.airport.co.kr/service/rest/AirportParkingCongestion/airportParkingCongestionRT"
url = f"{endpoint}?schAirportCode=GMP&serviceKey={encoding}&numOfRows=10&pageNo=1"

result = requests.get(url)
soup = BeautifulSoup(result.text,"lxml")
print(soup)

