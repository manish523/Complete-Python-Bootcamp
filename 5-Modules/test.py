from package.maths import *
import package.subpackages.mult as subPack

print(addition(2, 3))
print(subtraction(10, 4))
print(multiplication(5, 6))
print(subPack.multiply(addition(2, 3), subtraction(10, 4)))

