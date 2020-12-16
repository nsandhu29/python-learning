from dataclasses import dataclass


# The frozen parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)

# Attempting to change immutable class
# obj.value1 = "Value 345"
# print(obj.value1)

obj.some_func(20)
