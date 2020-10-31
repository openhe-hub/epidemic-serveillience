from net.download import downloadData
from utils.analyzer import analyze
from utils.logger import logOnBoost
if __name__ == "__main__":
    logOnBoost()
    downloadData()
    analyze()
    
