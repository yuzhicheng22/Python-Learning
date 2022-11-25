def print_two(*args):
    args1, args2 = args
    print(f"args1:{args1}, args2:{args2}")

def print_two_aigin(args1, args2):
    print(f"args1:{args1}, args2:{args2}")

def print_one(args1):
    print(f"args1:{args1}")

def print_none():
    print("I got nothin'.")

print_two("zhicheng", "yu")
print_two_aigin("john", "snow")
print_one("jack")
print_none()