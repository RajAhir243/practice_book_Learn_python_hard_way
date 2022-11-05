def print_two(*args):
    args1,args2 = args
    print("args1: %r,args2: %r"%(args1,args2))

def print_two_again(args1,args2):
    print("args1: %r,args2: %r"%(args1,args2))

def print_one(args1):
    print("args1: %r"%(args1))

def print_none():
    print("I got nothin")

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("First")
print_none()