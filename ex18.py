def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_def_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "Nothing to print"

print_two("Anshuman", "Padhi")
print_def_again("Anshuman", "Padhi")
print_one("Anshuman")
print_none()
