# part 1
def my_name(name):
 print(f"my name is {name}")

my_name("Fatima")

# part 2
def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal("pizza","orange juice")

#part 3

def cube(number):
    return number ** 3


def by_three(num):
    if num  % 3 == 0:
        return cube(num) 
    else:
        return False


print(by_three(7))