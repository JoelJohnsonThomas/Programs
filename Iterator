class TopTen:
    def __init__(self):
        self.num = 1  # setting the initial number

    def __iter__(self):  # this function prints the object
        return self

    def __next__(self):  # this funcion prints the next objects
        if self.num <= 10:  # setting the final value to 10
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration  # the only to iteration in order to avoid repetition


nums = TopTen()
print(next(nums))
for i in nums:
    print(i)
