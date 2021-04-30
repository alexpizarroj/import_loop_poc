print('{}: Being imported'.format(__name__))

import import_loop_poc.cyclic_package.module1

print('{}: Executing function1'.format(__name__))
import_loop_poc.cyclic_package.module1.function1()
print('{}: Executed function1'.format(__name__))

print('{}: Imported'.format(__name__))
