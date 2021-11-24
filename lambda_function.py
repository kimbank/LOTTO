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
    lottoDBList = makingLottoDBList()
    while True:
        makingLottoNumberTemp = makingLottoNumber()
        
        if makingLottoNumberTemp not in lottoDBList:
            break

    return {
        'statusCode': 200,
        'body': json.dumps(makingLottoNumberTemp)
    }