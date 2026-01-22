my_foods = ["apple", "banana", "cherry"]

# for food in my_foods:
#     for food2 in my_foods:
#         if food == food2:
#             print(f"Skipping duplicate food: {food}")
#             continue
#         print(f"Cooking {food} with {food2}")


class CountTo:
    def __init__(self, max_value, step):
        self.max = max_value
        self.step = step

    def __iter__(self):
        return self# CountToIterator(self.max, self.step)


class CountToIterator:
    def __init__(self, max_value, step):
        self.max = max_value
        self.current = 1
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += self.step
            return val
        else:
            raise StopIteration


counter = CountToIterator(10, 4)

for count in counter:
    for count2 in counter:
        print(f"Count: {count} and {count2}")
