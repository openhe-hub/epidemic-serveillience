import json
from utils.logger import logAfterAnalyze, logBeforeAnalyze
from utils.value import originDict, getTime, generatedDict, viewDict


def output(generatedData):
    outputFile = open(f"{generatedDict}{getTime()}.json",
                      "w", encoding="utf-8")
    jsonStr = json.dump(generatedData, outputFile, ensure_ascii=False)
    outputFile.close()

    viewFile = open(f"{viewDict}{getTime()}.json",
                    "w", encoding="utf-8")
    jsonStr = json.dump(generatedData, viewFile, ensure_ascii=False)
    viewFile.close()


def analyze():
    logBeforeAnalyze()
    file = open(f"{originDict}{getTime()}.json", "r", encoding='utf-8')
    data = json.loads(file.read())

    # total data in dict
    generatedData = {
        "date": data["lastUpdateTime"],
        "total": {
            "confirm": data["chinaTotal"]["confirm"],
            "heal": data["chinaTotal"]["heal"],
            "dead": data["chinaTotal"]["dead"],
            "nowConfirm": data["chinaTotal"]["nowConfirm"],
            "change": {
                "confirm": data["chinaAdd"]["confirm"],
                "heal": data["chinaAdd"]["heal"],
                "dead": data["chinaAdd"]["dead"],
            }
        },
        "name":[],
        "value":[]
    }

    for province in data["areaTree"][0]["children"]:
        # area data in dict
        generatedData["name"].append(province["name"])
        generatedData["value"].append(province["total"]["confirm"])
    file.close()
    output(generatedData)
    logAfterAnalyze()
