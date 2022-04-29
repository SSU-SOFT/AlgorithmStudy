# Web

## HTML
- XML 형태로 웹 페이지의 구조를 표현
  - Beautiful Soup등 XMLparser로 해석 가능
- 다운 받은 HTML 파일을 웹 브라우저가 해석 & 화면 표시

```
>>> import requests
>>> from bs4 import BeautifulSoup
>>> URL = 'https://sports.news.naver.com/index'
>>> response = requests.get(URL)
>>> soup = BeautifulSoup(
...     response.text,
...     'html.parser'
... )
>>> headline = soup.find(name='ul', attrs={})
>>> headline = soup.find(name='ul', attrs={'class':'today_list'})
>>> for title in headline.find_all(name='strong', attrs={'class':'title'}):
...     print(title.string)
```
> [NBA PO] '피닉스 나와!' 댈러스, 접전 끝에 유타 꺾고 2R 진출<br/>
'음주운전 삼진아웃' 강정호, KBO리그 못뛴다. 키움 계약 승인불허 [공식발표]<br/>
‘조성원 사퇴’ LG, 조상현 신임 감독 선임<br/>
'결국 쏟아진 눈물'...04년생 아들의 프로 데뷔에 아버지 '오열'<br/>
'타구에 직격' 노경은, 손가락 골절로 전치 4주 진단..SSG 큰 타격<br/>
‘헤벌쭉’ 동료 아내에게 흑심 품었던 토트넘 공격수<br/>

-> Scrapy Library를 사용하면 더 효과적?