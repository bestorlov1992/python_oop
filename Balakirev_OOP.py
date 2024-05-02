# import consts
# from accessify import private, protected
# from string import ascii_letters


# class Point:
#     "Point class"
#     color = "red"
#     circle = 2
#     __instance = None
#     __test_var = 1
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#     shared_attr = {"name": "thread1", "data": {}, "id": 1}

#     def __new__(cls, *args, **kwargs) -> None:
#         cls.__instance = super().__new__(cls)
#         # if cls.__instance is None:
#         #     cls.__instance = super().__new__(cls)
#         return cls.__instance

#     def __del__(self) -> None:
#         Point.__instance = None

#     def __init__(self, x: int = 0, y: int = 0) -> None:
#         self.__x = self.__y = 0
#         self.__dict__ = self.shared_attr
#         if (
#             self.validate(x)
#             and self.validate(y)
#             and self.__check_coords(x)
#             and self.__check_coords(y)
#         ):
#             self.__x = x
#             self.__y = y

#     def __del__(self) -> None:
#         pass

#     @classmethod
#     def validate(cls, arg) -> None:
#         return cls.MIN_COORDS <= arg <= cls.MAX_COORDS

#     @private
#     @classmethod
#     def __check_coords(cls: object, x: int) -> bool:
#         return type(x) in (int, float)

#     def set_coords(self, x: int, y: int) -> None:
#         if self.__check_coords(x) and self.__check_coords(y):
#             self.__x = x
#             self.__y = y
#         raise ValueError("x, y must be int or float")

#     def get_coords(self) -> (int, int):
#         return (self.__x, self.__y)

#     @staticmethod
#     def mult_x_y(x: int, y: int) -> int:
#         return x * y

#     @classmethod
#     def set_bount(cls, bound: int) -> None:
#         cls.MIN_COORDS = bound

#     def __getattribute__(self, __name: str) -> None:
#         # print(__name)
#         # # print("getting atribute in magic method getattribute")
#         # else:
#         return object.__getattribute__(self, __name)

#     def __setattr__(self, __name: str, __value) -> None:
#         if __name == "z":
#             raise ValueError("z is not apropriated")
#         else:
#             object.__setattr__(self, __name, __value)
#             # pass
#             # self.__dict__[__name] = __value

#     def __getattr__(self, __name):
#         # print("attr does't exist")
#         return False

#     def __delattr__(self, __name: str) -> None:
#         print("deleting attr " + __name)
#         object.__delattr__(self, __name)

#     @property
#     def test_var(self) -> int:
#         return self.__test_var

#     @test_var.setter
#     def test_var(self, test_var: int) -> None:
#         self.__test_var = test_var

#     @test_var.deleter
#     def test_var(self) -> None:
#         del self.__test_var

#     # test_var = property(get_test_var, set_test_var)
#     # a = property()


# class Person:
#     S_RUS = "абвгджзиклмнопрстуфшщэюя-"
#     S_RUS_UPPER = S_RUS.upper()

#     def __init__(self, fio: str, old: int, ps: str, weight: float) -> None:
#         self.fio = fio
#         self.old = old
#         self.passport = ps
#         self.weight = weight

#     @classmethod
#     def verify_fio(cls, fio: str) -> None:
#         if type(fio) is not str:
#             raise TypeError("Fio must be string")
#         l_fio = fio.split()
#         if len(l_fio) != 3:
#             raise ValueError("Fio must contain 3 word")
#         letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
#         # if not all(map(lambda x: len(x) > 0 and all(map(lambda c: c in letters, x)), l_fio)):
#         #     raise ValueError("Only alphabetic")
#         for s in l_fio:
#             if len(s.strip(letters)) != 0:
#                 raise ValueError('Only alphabetic')
#     @classmethod
#     def verify_old(cls, old):
#         if type(old) is not int or old < 14 or old > 120:
#             raise TypeError('Old must be int and in (14-120 years')
#     @classmethod
#     def verify_weight(cls, weight):
#         if type(weight) is not float or weight < 20:
#             raise TypeError('weight must be float and in (20 and more years')
#     @classmethod
#     def verify_passport(cls, ps):
#         if type(ps) is not str:
#            raise TypeError("Passport must be string")
#         l_ps = ps.split()
#         if len(l_ps) != 2 or len(l_ps[0]) != 4 or len(l_ps[1]) != 6:
#             raise ValueError("Passport format is xxxx xxxxxx")
#         if not all(map(lambda x: x.isdigit(), l_ps)):
#             raise TypeError("Passport must contains digits")
#     @property
#     def fio(self) -> str:
#         return ' '.join(self.__fio)
#     @fio.setter
#     def fio(self, fio: str) -> None:
#         self.verify_fio(fio)
#         self.__fio = fio.split()
#     @property
#     def old(self) -> int:
#         return self.__old
#     @old.setter
#     def old(self, old: int) -> None:
#         self.verify_old(old)
#         self.__old = old
#     @property
#     def passport(self) -> str:
#         return self.__passport
#     @passport.setter
#     def passport(self, ps: str) -> None:
#         self.verify_passport(ps)
#         self.__passport = ps
#     @property
#     def weight(self) -> float:
#         return self.__weight
#     @weight.setter
#     def weight(self, weight: float) -> None:
#         self.verify_weight(weight)
#         self.__weight = weight


# class Descr_coord:
#     @classmethod
#     def verify_coord(cls, coor):
#         if type(coor) is not int:
#             raise TypeError("coord must be int")

#     def __set_name__(self, owner, name):
#         print("__set_name__")
#         self.name = "_" + name

#     def __get__(self, instance, owner):
#         print("__get__")
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         print("__set__")
#         self.verify_coord(value)
#         return setattr(instance, self.name, value)

# class Test:
#     def __set_name__(self, owner, name):
#         self.name = '_x'
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

# class Point3D:
#     x = Descr_coord()
#     y = Descr_coord()
#     z = Descr_coord()
#     tt = Test()
#     def __init__(self, x, y, z) -> None:
#         print("__init__")
#         self.x = x
#         self.y = y
#         self.z = z

# Функтор - класс, в котором есть дандер __call__, то есть объекты этого класса
# мы можем вызвыть через ()
# class Counter:
#     def __init__(self, *args, **kwargs) -> None:
#         self.__count = 0
#     def __call__(self, a = None, b = None, c = None, *args, **kwargs):
#         if a is not None:
#             self.__count += a
#             return self.__count


# class Derivate:
#     def __init__(self, func, *args, **kwargs) -> None:
#         self.__func = func
#     def __call__(self, x, dx = 0.0001, *args, **kwargs):
#         return (self.__func(x + dx) - self.__func(x)) / dx
# @Derivate
# def dx(x):
#     return x*x


# class Coords:
#     def __init__(self, *args) -> None:
#         self._coords = args

#     def __repr__(self) -> str:
#         return f"{self.__class__} : {self.name}"

#     def __str__(self) -> str:
#         return self.__class__
#     def __len__(self):
#         return len(self._coords)
#     def __abs__(self):
#         return list(map(abs, self._coords))


class Clock:
    __DAY = 86_400

    def __init__(self, sec: int) -> None:
        if not isinstance(sec, int):
            raise TypeError("seconds must be int")
        self.__sc = sec % self.__DAY

    def get_time(self):
        s = self.__sc % 60
        m = (self.__sc // 60) % 60
        h = (self.__sc // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(s)}:{self.__get_formated(m)}"
    @classmethod
    def __get_formated(self, t):
        return str(t).rjust(2, '0')
tm = Clock(4000)
print(tm.get_time())
