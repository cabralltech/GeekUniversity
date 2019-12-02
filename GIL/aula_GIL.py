import sys

a = []
b = a
print(sys.getrefcount(a))
b = None
print(sys.getrefcount(a))