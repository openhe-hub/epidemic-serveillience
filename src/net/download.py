import json
import time
import requests
import sys
sys.path.append("..")

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
outDict = 'D:\\python\\project\\epidemic-serveillance\\resources\\'

def downloadData():
    print(f"[INFO]:collecting epidemic data from {url}...")
    data = json.loads(requests.get(url).json()['data'])
    t = time.strftime("%Y-%m-%d", time.localtime())
    file = open(f"{outDict}{t}.json", 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False)
    file.close()
    print(f"[INFO]:download epidemic data of {t} finished.")
