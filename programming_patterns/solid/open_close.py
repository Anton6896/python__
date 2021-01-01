"""
solid design principles (Robert C Martin)
1. srp -> singel responsibility for object
2. ocp -> open close principeles
3.
4.
5.
"""
# ocp -> open for extention close for modification
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# ========================================================================


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.size = size
        self.color = color

    def __str__(self):
        return self.name


class Specifications:
    # Specification is Enterprice pattern !
    # than working under the OCP .
    # Base class
    def is_satisfied(self, item: Product):
        pass

    # redefine and , or
    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return AndSpecification(self, other)


class Filter:
    # Base class
    def filter(self, item: Product, spec: Specifications):
        pass

# ========================================================================


class ColorSpecification(Specifications):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return self.color == item.color


class SizeSpecification(Specifications):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return self.size == item.size


class AndSpecification(Specifications):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        # all check all value (size , color ...) if true return it
        return all(map(
            lambda x: x.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items: list, spec: Specifications) -> list:
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":

    green_spec = ColorSpecification(Color.GREEN)
    red_spec = ColorSpecification(Color.RED)
    small_spec = SizeSpecification(Size.SMALL)
    large_spec = SizeSpecification(Size.LARGE)

    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.RED, Size.LARGE)

    my_products = (apple, tree, house)

    bf = BetterFilter()

    print("green products :" , end=" ")
    for p in bf.filter(my_products, green_spec):
        print(p, end=" ,")

    print("\nlarge size :", end=" ")
    for p in bf.filter(my_products, large_spec):
        print(p, end=" , ")

    # print("large and green : ")
    # large_green = AndSpecification(
    #     SizeSpecification(Size.LARGE),
    #     ColorSpecification(Color.GREEN)
    # )

    # redefine __and__ <=> & , __or__ at Specification class
    large_green = large_spec & green_spec
    samall_or_red = small_spec or red_spec

    print("\nlarge and green : ", end=" ")
    for p in bf.filter(my_products, large_green):
        print(p, end=" , ")

    print("\nsmall or red : ", end=" ")
    for p in bf.filter(my_products, samall_or_red):
        print(p, end=" , ")

    print()
