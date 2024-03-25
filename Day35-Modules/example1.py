import nisc_module
#! Now a new directory is created as name __pycache__.
#! __pycache__ is a directory that is created by the Python interpreter when it imports a module. It contains the compiled bytecode of the module, which can be used to speed up subsequent imports of the same module.

result= nisc_module.pi
print(result)

print()

sqrt=nisc_module.square(3)
print(sqrt)

print()


cube=nisc_module.cube(3)
print(cube)


print()

name=nisc_module.name("SpongeBob")
print(name)

