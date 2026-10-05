import json                                                #导入json
def analyze_log(filepath: str) -> dict:                    
    result = {                                             #规定结果返回格式
    "total":0,
    "by_level":{},
    "by_user":{},
    "last_error":None
    }
return result

if __name__ == "__main__":                                 #脚本入口
    result = analyze_log("app.jsonl")
    print(result)
