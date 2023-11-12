class Frange:
    def __init__(self, *args):
        arg_number = len(args)
        if arg_number == 1:
            self.start = 0.0
            self.end = float(args[0])
            self.step = 1.0
        elif arg_number == 2:
            self.start = float(args[0])
            self.end = float(args[1])
            self.step = 1.0
        elif arg_number == 3:
            self.start = float(args[0])
            self.end = float(args[1])
            self.step = float(args[2])

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.current < self.end or self.step < 0 and self.current > self.end:
            self.result = self.current
            self.current += self.step
            return self.result
        else:
            raise StopIteration

f = Frange(0, 100, 3.5)
for i in f:
    print(i)

assert list(Frange(5)) == [0, 1, 2, 3, 4]
assert list(Frange(2, 5)) == [2, 3, 4]
assert list(Frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(Frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(Frange(1, 5)) == [1, 2, 3, 4]
assert list(Frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(Frange(0, 0)) == []
assert list(Frange(100, 0)) == []

print('SUCCESS!')
