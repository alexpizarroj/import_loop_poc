print('{}: Being imported'.format(__name__))

import import_loop_poc.cyclic_package.module1

print('{}: Defining function2'.format(__name__))
def function2():
    print('Hello, World!')
    import_loop_poc.cyclic_package.module1.function3()
print('{}: Defined function2'.format(__name__))

print('{}: Imported'.format(__name__))
