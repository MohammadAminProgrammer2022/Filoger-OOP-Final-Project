from person import *


class User(Person):
    user_id_cls_att = 1000
    def __init__(self, reservations):
        self.reservations = reservations
        self.__user_id = self.set_id()
        
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, new_id):
        self.__user_id = new_id
        
    @classmethod
    def set_id(cls):
        cls.user_id_cls_att += 1
        num = cls.user_id_cls_att
        return 'U' + str(num)


if __name__ == "__main__":
    u1 = User('reserve')
    print(u1.user_id)
    u2 = User('erwr')
    print(u2.user_id)