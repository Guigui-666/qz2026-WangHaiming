import json                                                #导入json
def analyze_log(filepath: str) -> dict:                    
    result = {                                             #规定结果返回格式
    "total":0,
    "by_level":{},
    "by_user":{},
    "last_error":None
    }
     try:                                                   #尝试读取文件
        with open(filepath,"r",encoding="utf-8") as f:     #读取文件
            for line in f:                                 #for循环逐一读取
                line = line.strip()
                if not line:                               #遇到空白行进行下一轮循环
                    continue
 except FileNotFoundError:                              #如果无法找到该文件，则暂不处理
        pass
return result

if __name__ == "__main__":                                 #脚本入口
    result = analyze_log("app.jsonl")
    print(result)
