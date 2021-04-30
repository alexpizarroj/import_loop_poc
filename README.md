# Import Loop Proof of Concept

Run this with:

```
python3.5 -m import_loop_poc.main
```

And you'll get output similar to this:
```
import_loop_poc.cyclic_package: Being imported
import_loop_poc.cyclic_package.module1: Being imported
import_loop_poc.cyclic_package.module2: Being imported
import_loop_poc.cyclic_package.module2: Defining function2
import_loop_poc.cyclic_package.module2: Defined function2
import_loop_poc.cyclic_package.module2: Imported
import_loop_poc.cyclic_package.module1: Defining function1
import_loop_poc.cyclic_package.module1: Defined function1
import_loop_poc.cyclic_package.module1: Defining function3
import_loop_poc.cyclic_package.module1: Defined function3
import_loop_poc.cyclic_package.module1: Imported
import_loop_poc.cyclic_package: Executing function1
An error occurred - execution stopped: AttributeError("module 'import_loop_poc' has no attribute 'cyclic_package'",)

Modules currently imported:
{'import_loop_poc': <module 'import_loop_poc' from '/Users/apizarro/tmp/import_loop_poc/import_loop_poc/__init__.py'>,
 'import_loop_poc.cyclic_package.module1': <module 'import_loop_poc.cyclic_package.module1' from '/Users/apizarro/tmp/import_loop_poc/import_loop_poc/cyclic_package/module1.py'>,
 'import_loop_poc.cyclic_package.module2': <module 'import_loop_poc.cyclic_package.module2' from '/Users/apizarro/tmp/import_loop_poc/import_loop_poc/cyclic_package/module2.py'>}
Module symbols
{'import_loop_poc': ['__builtins__',
                     '__cached__',
                     '__doc__',
                     '__file__',
                     '__loader__',
                     '__name__',
                     '__package__',
                     '__path__',
                     '__spec__'],
 'import_loop_poc.cyclic_package.module1': ['__builtins__',
                                            '__cached__',
                                            '__doc__',
                                            '__file__',
                                            '__loader__',
                                            '__name__',
                                            '__package__',
                                            '__spec__',
                                            'function1',
                                            'function3',
                                            'import_loop_poc'],
 'import_loop_poc.cyclic_package.module2': ['__builtins__',
                                            '__cached__',
                                            '__doc__',
                                            '__file__',
                                            '__loader__',
                                            '__name__',
                                            '__package__',
                                            '__spec__',
                                            'function2',
                                            'import_loop_poc']}

Traceback (most recent call last):
  File "/Users/apizarro/.pyenv/versions/3.5.10/lib/python3.5/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/Users/apizarro/.pyenv/versions/3.5.10/lib/python3.5/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/Users/apizarro/tmp/import_loop_poc/import_loop_poc/main.py", line 26, in <module>
    main()
  File "/Users/apizarro/tmp/import_loop_poc/import_loop_poc/main.py", line 7, in main
    import import_loop_poc.cyclic_package
  File "/Users/apizarro/tmp/import_loop_poc/import_loop_poc/cyclic_package/__init__.py", line 6, in <module>
    import_loop_poc.cyclic_package.module1.function1()
AttributeError: module 'import_loop_poc' has no attribute 'cyclic_package'
```