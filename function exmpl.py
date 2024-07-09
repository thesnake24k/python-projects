def greet():
    print("if you love me let me go")


greet()


# ---------------------------------------------------------------------
def greet_name(name):
    print(f"if you love me let me go {name}")


greet_name("baka")


# -------------------------------------------
def gree_with(name, location):
    print(f"hi {name} your location is in {location}")


gree_with("yurika", "japan")
gree_with(location="Los angeles", name="Oussama")


# ------------------------------*args---------------------------------------------------------
def add(*args):
    # args going to be a tuple (..,..,..)
    res = 0
    for nu in args:
        res += nu
    return res


n = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(n)


# -------------------**kwargs--------------------------
def cal(nb, **kwargs):
    # kwargs going to be a dictionary item {.:.,.:. }
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    nb += kwargs["add"]
    nb += kwargs["multiply"]
    print(nb)


cal(12, add=12, multiply=2)


# --------------------------------kwargs Class----------------
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="volswagen", model="Golf")
print(my_car.model,my_car.make)
