# Check if an Integer is Divisible By Five

def divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False


def test_divisible():
    print("test started")
    if divisible_by_five(5) != True:
         print("error")
    elif divisible_by_five(-33) != False:
        print("error2")
    elif divisible_by_five(0) != True:
        print("error3")