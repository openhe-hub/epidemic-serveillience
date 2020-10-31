import time

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
originDict = 'D:\\python\\project\\epidemic-serveillance\\resources\\origin\\'
generatedDict = 'D:\\python\\project\\epidemic-serveillance\\resources\\generated\\'

def getTime():
    t = time.strftime("%Y-%m-%d", time.localtime())
    return t