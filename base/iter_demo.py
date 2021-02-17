#!/usr/bin/python
# coding=utf-8


class NumberIter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


numberIter = NumberIter()
iter_ = iter(numberIter)

print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))

print("\n\n\n")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
