import json

class UserManager:
    def __init__(self):
        self.users = []                                      # 存放所有用户数据
        self.max_id = 0                                      # 记录当前最大用户id
