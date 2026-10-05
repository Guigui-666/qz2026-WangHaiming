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
                try:                                       #尝试将JSON文件信息转化为Python字符串
                    data = json.loads(line)
                    level = data["level"]                      #将level和user信息提取出来
                    user = data["user"]
                    message = data["message"]
                except (json.JSONDecodeError, KeyError):   #如遇到JSON格式错误或键不存在，进行下一轮循环
                    continue
                result["total"] += 1                       #成功读取一行信息，数据总数加一
                
                if level in result["by_level"]:            #如果level已经出现在结果中by_level字典中，则在其原次数上加一；如果是第一次出现，则次数为一
                    result["by_level"][level] += 1
                else:
                    result["by_level"][level] = 1
                if user in result["by_user"]:              #如果user已经出现在结果中by_level字典中，则在其原次数上加一；如果是第一次出现，则次数为一
                    result["by_user"][user] += 1
                else:
                    result["by_user"][user] = 1
                if level == "ERROR":
                    result["last_error"] = message
    except FileNotFoundError:                              #如果无法找到该文件，则暂不处理
        pass
    return result

if __name__ == "__main__":                                 #脚本入口
    result = analyze_log("app.jsonl")
    print(result)
    
    
