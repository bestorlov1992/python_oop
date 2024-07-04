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
# class Operation_desc:
#     __operations = {"add": "+", "sub": "-", "mul": "*", "truediv": "/"}

#     def __set_name__(self, owner, name: str):
#         name = name.strip("_")
#         if name.startswith("r"):
#             self.prefix = 1
#             name = name[1:]
#         else:
#             self.prefix = 0
#         self.__name = name

#     def __get__(self, instance, owner) -> object:
#         def wrap(x: object):
#             if type(x) is type(instance):
#                 x = x.sc
#             elif type(x) is not int:
#                 raise ArithmeticError("right operand must be int or like self")
#             op = self.__class__.__operations[self.__name]
#             new_sec = self.get_res_op(op, instance.sc, x)
#             return owner(new_sec)
#         return wrap

#     def get_res_op(self, op, n1, n2) -> int:
#         if self.prefix:
#             n1, n2 = n2, n1
#         return int(eval(f"{n1}{op}{n2}"))


# class Clock:
#     # __truediv__ /
#     # __floordiv__ //
#     # __mod__ %
#     __DAY = 86_400
#     __add__ = Operation_desc()
#     __sub__ = Operation_desc()
#     __mul__ = Operation_desc()
#     __truediv__ = Operation_desc()
#     __radd__ = Operation_desc()
#     __rsub__ = Operation_desc()
#     __rmul__ = Operation_desc()
#     __rtruediv__ = Operation_desc()

#     def __init__(self, sec: int) -> None:
#         if not isinstance(sec, int):
#             raise TypeError("seconds must be int")
#         self.__sc = sec % self.__DAY

#     @property
#     def sc(self):
#         return self.__sc

#     @sc.setter
#     def sc(self, sec):
#         self.__sc = sec

#     def __str__(self) -> str:
#         return str(self.__sc)

#     def get_time(self):
#         s = self.__sc % 60
#         m = (self.__sc // 60) % 60
#         h = (self.__sc // 3600) % 24
#         return f"{self.__get_formated(h)}:{self.__get_formated(s)}:{self.__get_formated(m)}"

#     @classmethod
#     def __get_formated(self, t):
#         return str(t).rjust(2, '0')

#     @classmethod
#     def __verify_date(cls, other: object) -> int:
#         if not isinstance(other, (int, cls)):
#             raise TypeError(f'right value must be int or {cls}')
#         if type(other) is cls:
#             other = other.__sc
#         return other

#     def __eq__(self, __o: object) -> bool:
#         return self.__sc == self.__verify_date(__o)

#     def __lt__(self, __o: object) -> bool:
#         return self.__sc < self.__verify_date(__o)

#     def __gt__(self, __o: object) -> bool:
#         return self.__sc > self.__verify_date(__o)

#     def __ge__(self, __o: object) -> bool:
#         return self.__sc >= self.__verify_date(__o)

#     def __le__(self, __o: object) -> bool:
#         return self.__sc <= self.__verify_date(__o)


# class Point:
#     def __init__(self, x, y, colors) -> None:
#         self.colors = list(colors)
#         self.x = x
#         self.y = y

#     def __eq__(self, __o: object) -> bool:
#         return 1

#     def __hash__(self) -> int:
#         return hash((self.x, self.y))

#     def __len__(self) -> int:
#         print("__len__")
#         return 0

#     def __bool__(self) -> bool:
#         print("__bool__")
#         return True

#     def __getitem__(self, item) -> object:
#         if not isinstance(item, int):
#             raise TypeError("item nust be int")
#         if 0 <= item < len(self.colors):
#             return self.colors[item]
#         raise IndexError(f"index must be betwen {0} and {len(self.colors)}")

#     def __setitem__(self, item, val):
#         if not isinstance(item, int):
#             raise TypeError("item nust be int")
#         if 0 <= item < len(self.colors):
#             self.colors[item] = val
#         else:
#             offset = item + 1 - len(self.colors)
#             self.colors.extend([None] * offset)
#             self.colors.append(val)
#     def __delitem__(self, item):
#         if not isinstance(item, int):
#             raise TypeError("item nust be int")
#         if 0 <= item < len(self.colors):
#             del self.colors[item]
#             return None
#         raise IndexError(f"index must be betwen {0} and {len(self.colors)}")

# class FRange:
#     def __init__(self, start: float = 0.0, stop: float = 0.0, step: float = 1.0) -> None:
#         self.start = start
#         self.stop = stop
#         self.step = step


#     def __next__(self):
#         print("next")
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#     def __iter__(self):
#         print("iter")
#         self.value = self.start - self.step
#         return self
#     def __eq__(self, __o: object) -> bool:
#         print("eq")
#         return False
# class Geom:
#     def get_pr(self):
#         raise NotImplementedError("Method must be implemented in offspring (descendand) class")

# class Rect(Geom):
#     def __init__(self, w, h) -> None:
#        self.w = w
#        self.h = h
#     def get_pr(self):
#         return 2 * (self.w + self.h)


# class Square(Geom):
#     def __init__(self, a) -> None:
#        self.a = a
#     def get_pr(self):
#         return 4 * self.a


# rc1 = Rect(1, 2)
# rc2 = Rect(3, 4)
# sq1 = Square(5)
# sq2 = Square(7)

# geom = [rc1, rc2, sq1, sq2]
# sq1.get_pr()


# class Point2D:
#     __slots__ = ('x', 'y', '__length')

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5

#     @property
#     def length(self):
#         return self.__length

#     @length.setter
#     def length(self, length):
#         self.__lenght = length


# class Point3D(Point2D):
#     __slots__ = ('z',)

#     def __init__(self, x, y, z) -> None:
#         self.x = x
#         self.y = y
#         self.z = z
# import traceback as tb
# import logging

# def func1():
#     # print('func1')
#     try:
#         func2()
#     except:
#         # Can do like this
#         print(tb.format_exc())
#         # or like this with logging
#         logging.exception('text from logger')

# def func2():
#     # print('func2')
#     1/0

# class ExceptionSendData (Exception):
#     '''Class exception for send data'''
#     def __init__(self, *args: object) -> None:
#         self.message = args[0] if args else None
#     def __str__(self) -> str:
#         return f'Error: {self.message}'


# a = 10
# b = a
# try:
#     pass
# except ExceptionSendData as ex:
#     print("in ex")
# finally:
#     pass
#     # print('in finally')

# raise ExceptionSendData('text for exception')

# class DefenderVector:
#     def __init__(self, v) -> None:
#         self.__v = v

#     def __enter__(self):
#         self.__temp = self.__v.copy()
#         return self.__temp

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         if exc_type is None:
#             self.__v[:] = self.__temp
#         return True

# v1 = [1, 2, 3]
# v2 = [2, 4]

# with DefenderVector(v1) as dv:
#     for i, v in enumerate(dv):
#         dv[i] += v2[i]

# a = 10


# class Women:
#     b = a
#     title = 'object for column title'
#     photo = 'object for column photo'
#     ordering = 'object for column ordering'

#     def __init__(self, user, psw) -> None:
#         self._user = user
#         self._psw = psw
#         self.meta = self.Meta(user + '@' + psw)

#     class Meta:
#         ordering = ['id']
#         def __init__(self, access) -> None:
#             self.access = access
# class A1:
#     do1 = lambda self, x: x + x
#     def do():
#         pass
# class A2: ...

# def test(self):
#     pass
# Point = type('Point', (A1, A2), {'MAX_COORD': 100, 'MIN_COORD': 300, 'method_t' : test})

# def create_class_point(name, bases, attrs: dict):
#     attrs.update({'MAX_COORD': 100, 'MIN_COORD': 300})
#     return type(name, bases, attrs)

# class Meta(type):
#     def __init__(cls, name, bases, attrs):
#         super().__init__(name, bases, attrs)
#         cls.MAX_COORD = 100
#         cls.MIN_COORD = 200


# class Point(metaclass=Meta):
#     def get_coords(self):
#         return (0, 0)
# class Meta(type):
#     def create_local_attrs(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value

#     def __init__(cls, name, base, attrs):
#         cls.class_attrs = attrs
#         cls.__init__ = Meta.create_local_attrs


# class Women(metaclass=Meta):
#     title = 'title'
#     content = 'contend'
#     photo = 'photo'


# import pprint
# import dataclasses


# class GoodsMethodFactory:
#     @staticmethod
#     def get_init_mesure():
#         return [0, 0, 0]


# @dataclasses.dataclass
# class Thing:
#     current_uid = 0
#     uid: int = dataclasses.field(init=False)
#     descr: str = ""
#     weight: int = None
#     price: int = None

#     def __post_init__(self):
#         type(self).current_uid += 1
#         self.uid = type(self).current_uid


# @dataclasses.dataclass
# class SubThing(Thing):
#     title: str = ""
#     author: str = ""
#     weight: float = 0
#     price: float = 0
#     mesure: list = dataclasses.field(
#         default_factory=GoodsMethodFactory.get_init_mesure)

#     def __post_init__(self):
#         super().__post_init__()


# th = Thing(1)
# print(th)

# sth = SubThing('t_descr', 7.7, 199.90, 't_title', 'Sam Smith')
# print(sth)

# T_Data = dataclasses.make_dataclass('T_Data', [('model', str), ('price'), ('max_speed', int, dataclasses.field(default=0))
#                                                ], namespace={'get_max_speed': lambda self: self.max_speed}
#                                     )
# td = T_Data('cabrio', 1_000_000)
# print(td.get_max_speed())
