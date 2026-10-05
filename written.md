选择题 + 简答题
永久链接：选择题 + 简答题
本文件包含所有选择题与简答题，请在你的仓库中于本文件作答。硬性要求：本文件所有题目均必须完成，未完成的题目不进入部门筛选流程。
一、选择题（每题 2 分，共 10 题，满分 20 分）
Permalink： 一、选择题（每题 2 分，共 10 题，满分 20 分）
说明：单选，将答案写在本节末尾的「答案」行中，格式如 。1. A  2. B  3. C ...
1. 依次执行以下代码，输出是什么？
def f(x, lst=
[]):
    lst.append(x
)
    return lst

a = f(1
)
b = f(2
)
print(b)
复制代码到剪贴板
◦ A.[2]
◦ B.[1, 2]
◦ C.[1]
◦ D.TypeError: 'list' object is not callable
2. 依次执行以下代码，输出是什么？
a = [1, 2, 3
]
b = a
c = a.copy
()
a.append(4
)
print(b, c)
复制代码到剪贴板
◦ A.[1, 2, 3, 4]  [1, 2, 3, 4]
◦ B.[1, 2, 3, 4]  [1, 2, 3]
◦ C.[1, 2, 3]  [1, 2, 3, 4]
◦ D.[1, 2, 3]  [1, 2, 3]
3. 依次执行以下代码，输出是什么？
try
:
    x = 1 / 0
except ZeroDivisionError
:
    print("A"
)
else
:
    print("B"
)
finally
:
    print("C")
复制代码到剪贴板
◦ A. 只输出C
◦ B. 输出 和AC
◦ C. 输出 和BC
◦ D. 输出 、 和ABC
4. 依次执行以下代码，输出是什么？
s = " hello "
print(len(s
))
print(len(s.strip()))
复制代码到剪贴板
◦ A.7  7
◦ B.7  5
◦ C.5  5
◦ D.5  7
5. 以下代码的执行结果是？
for i in range(5
):
    if i == 3
:
        break
else
:
    print("done"
)
print("end")
Copy code to clipboard
◦ A. 输出 和 doneend
◦ B. 只输出 end
◦ C. 只输出 done
◦ D. 什么都不输出
6. 依次执行以下代码，输出是什么？
class Animal
:
    def __init__(self, name
):
        self.name = name

    def speak(self
):
        print("..."
)

class Dog(Animal
):
    def speak(self
):
        print(f"{self.name}: woof"
)

d = Dog("Rex"
)
d.speak()
Copy code to clipboard
◦ A. ...
◦ B. Rex: woof
◦ C. 输出两行： 和 ...Rex: woof
◦ D. AttributeError: 'Dog' object has no attribute '__init__'
7. 以下代码中， 的值是什么？d
d = {"a": 1, "b": 2
}
d = {k: v for k, v in d.items() if v > 1
}
print(d)
Copy code to clipboard
◦ A. {'a': 1, 'b': 2}
◦ B. {'b': 2}
◦ C. {1: 'a', 2: 'b'}
◦ D. SyntaxError: invalid syntax
8. 依次执行以下代码，输出是什么？
import json
s = json.dumps({"name": "张三", "age": 18
})
print(type(s))
Copy code to clipboard
◦ A. <class 'dict'>
◦ B. <class 'str'>
◦ C. <class 'bytes'>
◦ D. TypeError: dump() missing 1 required positional argument: 'fp'
9. 依次执行以下代码，输出是什么？
def f(x
):
    return x + 1

f(5
)
print(f(5))
Copy code to clipboard
◦ A. 输出两行： 和 None6
◦ B. 只输出 6
◦ C. 只输出 None
◦ D. 输出 两次6
10. 以下代码中， 和 的区别是什么？user.get("city")user["city"]
user = {"name": "张三", "age": 18}
Copy code to clipboard
◦ A. 没有区别，两者行为完全一致
◦ B. 返回默认值 ， 抛出 get()None[]KeyError
◦ C. 抛出 ， 返回 get()KeyError[]None
◦ D. 只能用于字符串键， 可以用于任意键get()[]
答案
Permalink: 答案
（在此填写，格式：）1. B  2. B  3. B  4. B  5. B  6. B  7. B  8. B  9. B  10. B
￼
二、简答题（每题 10 分，共 3 题，满分 30 分）
Permalink: 二、简答题（每题 10 分，共 3 题，满分 30 分）
说明：直接在本文件对应题目下方作答，支持代码块。
第 1 题：浅拷贝与深拷贝
Permalink: 第 1 题：浅拷贝与深拷贝
以下代码中，、、 三者之间的关系是什么？执行 后， 和 分别变成什么？请解释原因。abca[0].append(99)bc
a = [[1, 2], [3, 4
]]
b = a.copy
()
import copy
c = copy.deepcopy(a)
Copy code to clipboard
（1）abc之间的关系：b是对a的浅拷贝，b有新的外层列表，但是子列表[1,2][3,4]与a 共享；c是对a的深拷贝，不仅有新的外层列表，内层的子列表也是全新的独立对象。 （2）b.[1,2,99][3,4],由于b和a共享子列表，所以在a中第一个子列表末尾加入99后，b也随之改变； c.[1,2][3,4],由于c是a的深拷贝，c的子列表独立不受a的子列表变化影响，所以c与原来的a一样。
第 2 题：字典与列表的综合应用
Permalink: 第 2 题：字典与列表的综合应用
以下代码模拟"从日志中提取用户信息"，请回答：
logs =
 [
    {
"user": "张三", "action": "login", "level": "INFO"
},
    {
"user": "李四", "action": "logout", "level": "INFO"
},
    {
"user": "张三", "action": "error", "level": "ERROR"
},
    {
"user": "王五", "action": "login", "level": "INFO"
},
    {
"user": "李四", "action": "error", "level": "ERROR"
},
]
Copy code to clipboard
1. 写出表达式，找出所有 为 的日志（返回字典列表）。level"ERROR"
2. 写出表达式，统计每个用户出现了几次（返回字典，键为用户名，值为次数）。
3. 解释为什么第 2 问不能直接用 得到结果，需要什么遍历结构？len(logs)
1.[日志中项目对项目，如果“level”] == “ERROR”] 2.来自收藏导入计数器 Counter（log[“user”]用于登录日志） 3.len（logs）用于获取日志列表一共有多少条记录，而不能区分不同用户的记录次数。需要用到for循环遍历，循环每一条日志，提取user用户名进行统计。
第 3 题：异常处理设计
Permalink： 第 3 题：异常处理设计
Day_10 中你写过 函数：能转就返回整数，不能转就返回 。safe_int(s)None
现在请你设计一个 函数：safe_divide(a, b)
• 输入两个字符串 和ab
• 尝试将它们转为数字并计算a / b
• 如果转换失败（）或除数为零（），返回ValueErrorZeroDivisionErrorNone
• 否则返回商（）float
请写出函数代码，并说明：为什么这里用 比先用 判断再计算更好？try/exceptif
防守safe_divide（A，B）： 试试： num_a = float（a） num_b = float（b） 返回num_a / num_b 除了（ValueError， ZeroDivisionError）： 返回 无
为什么try/except更好？ try/except是先尝试执行，捕获异常，if更复杂，且无法包含所有错误情况，不如try/except简单明了。
