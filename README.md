<h1 align="center"> 🔨Stack🔨 </h1>

<p align="center">
  <a><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/></a>
  <a><img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/></a>
  <a><img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white"/></a>
  <a><img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=AmazonAWS&logoColor=white"/></a>
</p>
</br>
<h1 align="center"> 
  <a href="https://lotto.goldbank.dev" target="blank">LOTTO.GOLDBANK.DEV</a>
</h1>

</br></br></br></br></br>

# 1. lotto API

</br>

## 1-1. lotto.csv
역대 로또 당첨 번호

> https://dhlottery.co.kr/gameResult.do?method=byWin

</br>

## 1-2. lambda_function.py

**1)** 1 ~ 45 랜덤 번호 6개 생성

**2)** *lotto.csv* 에 1)의 조합이 있을 경우 번호 재 조합

**3)** *lotto.csv* 에 1)의 조합이 없을 경우 **1**의 번호 조합 

```python

import random
import json


def makingLottoDBList():
  lottoDBList = []
  lottoDBListIndexCount = 0

  lottoDBLines = open("lotto.csv", 'r')
  lottoDBLinesTemp = lottoDBLines.readlines()
  for lottoDBLineTemp in lottoDBLinesTemp:
      lottoDBLineTemp = lottoDBLineTemp.strip()
      lottoDBList.append(list(map(int, lottoDBLineTemp.split("\t"))))
      lottoDBList[lottoDBListIndexCount].pop()
      lottoDBListIndexCount += 1
  lottoDBLines.close()
  return lottoDBList


def makingLottoNumber():
  lottoNumber = []
  while True:
    lottoNumberRandom = random.randrange(1, 46)
    if len(lottoNumber) == 6: 
      break
    elif lottoNumberRandom not in lottoNumber: 
      lottoNumber.append(lottoNumberRandom)
  lottoNumber.sort()

  return lottoNumber


def lambda_handler(event, context):
  makingLottoNumberTemp = makingLottoNumber()
  lottoDBList = makingLottoDBList()
  while True:
      if makingLottoNumberTemp not in lottoDBList:
        # print(makingLottoNumberTemp)
        break
      makingLottoNumberTemp = makingLottoNumber()
      
  n1 = "%d" %makingLottoNumberTemp[0]
  n2 = "%d" %makingLottoNumberTemp[1]
  n3 = "%d" %makingLottoNumberTemp[2]
  n4 = "%d" %makingLottoNumberTemp[3]
  n5 = "%d" %makingLottoNumberTemp[4]
  n6 = "%d" %makingLottoNumberTemp[5]
  
  data = {
    'n1': n1,
    'n2': n2,
    'n3': n3,
    'n4': n4,
    'n5': n5,
    'n6': n6
  }
  
  return {
    'statusCode': 200,
    'headers': {'Access-Control-Allow-Origin': '*'},
    'body': json.dumps(data)
  }

```


</br></br>

# 2. AWS Lambda

Test Lambda REST API test link

> https://skp7t6j64m.execute-api.ap-northeast-2.amazonaws.com/2021-11-24/lotto

</br></br>

# 3. HTML UI

> https://pit-and-pat.tistory.com/6

위 블로그의 *html* 디자인 포멧을 사용하였습니다.

</br></br>
