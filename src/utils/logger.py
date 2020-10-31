from utils.value import url,getTime

def logOnBoost():
    print("Welcome to EPIDEMIC SURVEILLANCE PROGRAM.")
    print("This software is developed in 2020-10 by openhe.")
def logBeforeDownLoad():
    print(f"[INFO]:collecting epidemic data from {url}...")
def logAfterDownLoad():
    print(f"[INFO]:download epidemic data of {getTime()} finished.")
def logBeforeAnalyze():
    print(f"[INFO]:analyzing epidemic data...")
def logAfterAnalyze():
    print(f"[INFO]:analyzing epidemic data finished")
