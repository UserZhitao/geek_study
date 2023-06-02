import time

class ParentClass1:
    def __init__(self):
        print('ParentClass1 init')

    def parent_method(self):
        print('ParentClass1 method')

class ParentClass2:
    def __init__(self):
        print('ParentClass2 init')

    def parent_method(self):
        print('ParentClass2 method')

class ChildClass(ParentClass1, ParentClass2):
    def __init__(self):
        ParentClass1.__init__(self)  # 调用第一个父类的构造方法
        ParentClass2.__init__(self)  # 调用第二个父类的构造方法

    def child_method(self):
        super().parent_method()  # 按照 MRO 调用下一个类的方法

# 创建子类实例并调用方法
child = ChildClass()
child.child_method()



# # clock装饰器
# def clock(func):
#     def clocked(*args, **kwargs):
#         print("arg:", args,kwargs)
#         print(len(args),' ',args[-1])
#         # 起始时间
#         start = time.time()
#         # 程序执行
#         func(*args, **kwargs)
#         # 结束时间
#         end = time.time()
#         # 输出
#         print(func.__name__, end - start)
#     return clocked
#
# # @clock
# def clock_test(name,test2):
#     print('装饰器……')
#     print(name)
#     time.sleep(5)
# list1 = [1,2,3]
# test2 = {'a':1,'b':2}
# clock(clock_test)(list1,test2=test2)