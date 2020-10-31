from utils.value import url,getTime

def logOnBoost():
    print("Welcome to EPIDEMIC SURVEILLANCE PROGRAM.")
    print("This software is developed in 2020-10 by openhe.")
    print("Other team workers:Zhou XinYuan,Zhang ShuYi,Wang Hui.")
    print("Our tutor teacher:Wang DingYang.")
def logOnFinished():
    print("OK.Now you can open the picture at http://127.0.0.1:5500/src/view/index.html")
def logBeforeDownLoad():
    print(f"[INFO]:collecting epidemic data from {url}...")
def logAfterDownLoad():
    print(f"[INFO]:download epidemic data of {getTime()} finished.")
def logBeforeAnalyze():
    print(f"[INFO]:analyzing epidemic data...")
def logAfterAnalyze():
    print(f"[INFO]:analyzing epidemic data finished")
