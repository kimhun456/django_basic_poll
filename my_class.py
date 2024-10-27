class MyClass:
    public_var = 1        # 공개 변수
    _protected_var = 2    # 내부 사용 변수 (약한 private)
    __private_var = 3     # 강한 private 의도 (이름 맹글링 적용)

    def __init__(self):
        self.instance_public = 4
        self._instance_protected = 5
        self.__instance_private = 6

obj = MyClass()

print(obj.public_var)            # 가능: 1
print(obj._protected_var)        # 가능하지만 권장되지 않음: 2
print(obj._MyClass__private_var) # 가능하지만 매우 권장되지 않음: 3

print(obj.instance_public)       # 가능: 4
print(obj._instance_protected)   # 가능하지만 권장되지 않음: 5
print(obj._MyClass__instance_private) # 가능하지만 매우 권장되지 않음: 6