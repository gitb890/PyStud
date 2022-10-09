from enum import Enum

class UserType(int,Enum):
    """
在定义枚举类型时，如果同时继承一些基础类型，比如int、str，
枚举类型就能同时充当该基础类型使用。比如在这里，UserType 就可以当作int 使用
    """
    # vip用户
    VIP = 3
    # 普通用户
    BANNED = 13
