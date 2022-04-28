import directory.functions
print(directory.functions.add(1, 2))

import directory.functions as func
print(func.add(1,2))

from directory import functions
print(functions.add(1,2))

from directory.functions import add
print(add(1,2))

from directory.functions import *
print(add(1, CONSTANT))