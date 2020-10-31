import json
from utils.logger import logAfterAnalyze, logBeforeAnalyze
from utils.value import originDict, getTime, generatedDict


def output(generatedData):
    outputFile = open(f"{generatedDict}{getTime()}.json",
                      "w", encoding="utf-8")
    jsonStr = json.dump(generatedData,outputFile,ensure_ascii=False)
    outputFile.close()

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
        "area": []
    }

    for province in data["areaTree"][0]["children"]:
        # area data in dict
        areaData = {
            "name": province["name"],
            "today": {
                "confirm": province["today"]["confirm"],
            },
            "total": {
                "nowConfirm": province["total"]["nowConfirm"],
                "confirm": province["total"]["confirm"],
                "dead": province["total"]["dead"],
                "deadRate": province["total"]["deadRate"],
                "heal": province["total"]["heal"],
                "healRate": province["total"]["healRate"],
            }
        }
        generatedData["area"].append(areaData)
    file.close()
    output(generatedData)
    logAfterAnalyze()
