def singleton(cls):
    instances = {}

    def getinstance(*args):
        key = (cls, args)
        if key not in instances:
            instances[key] = cls(*args)
        return instances[key]
    return getinstance


@singleton
class Figure(object):

    def __init__(self, sides):
        self.sides = sides


print(id(Figure(1)))
print(id(Figure(1)))
print(id(Figure(2)))
print(id(Figure(2)))
