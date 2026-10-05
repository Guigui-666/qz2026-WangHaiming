import json

class UserManager:
    def __init__(self):
        self.users = []                                      # 存放所有用户数据
        self.max_id = 0                                      # 记录当前最大用户id
         def add_user(self, name, age):                           # 添加用户，自动分配id
        self.max_id = self.max_id + 1
        new_user = {
            "id": self.max_id,
            "name": name,
            "age": age
        }
        self.users.append(new_user)
        return new_user

    def get_user(self, user_id):                             # 根据id查找用户
