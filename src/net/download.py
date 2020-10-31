import json
import time
import requests
from utils.logger import logAfterDownLoad, logBeforeDownLoad
from utils.value import url,originDict,getTime


def downloadData():
    logBeforeDownLoad()
    data = json.loads(requests.get(url).json()['data'])
    file = open(f"{originDict}{getTime()}.json", "w", encoding="utf-8")
    json.dump(data, file, ensure_ascii=False)
    file.close()
    logAfterDownLoad()
    
