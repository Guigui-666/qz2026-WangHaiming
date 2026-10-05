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
         for user in self.users:
            if user["id"] == user_id:
                return user
        return None
def update_age(self, user_id, new_age):                  # 修改指定id用户的年龄
        user = self.get_user(user_id)
        if user != None:
            user["age"] = new_age
            return True
        return False

    def remove_user(self, user_id):                          # 删除指定id的用户
        i = 0
        for user in self.users:
            if user["id"] == user_id:
                del self.users[i]
                return True
            i = i + 1
        return False

    def list_users(self):                                    # 返回全部用户列表
        return self.users
         def save_to_json(self, filepath):                        # 将用户数据保存到json文件
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False)

    def load_from_json(self, filepath):                       # 从json读取数据，覆盖当前用户
        with open(filepath, "r", encoding="utf-8") as f:
            self.users = json.load(f)
        
        if len(self.users) > 0:                              #更新最大id，保证新增id连续
            id_list = []
            for u in self.users:
                id_list.append(u["id"])
            self.max_id = max(id_list)
        else:
            self.max_id = 0
if __name__ == "__main__":
    pass
    
