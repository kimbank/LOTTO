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
