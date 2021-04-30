print('{}: Being imported'.format(__name__))

import import_loop_poc.cyclic_package.module2

print('{}: Defining function1'.format(__name__))
def function1():
    import_loop_poc.cyclic_package.module2.function2()
print('{}: Defined function1'.format(__name__))

print('{}: Defining function3'.format(__name__))
def function3():
    print('Goodbye, World!')
print('{}: Defined function3'.format(__name__))

print('{}: Imported'.format(__name__))
