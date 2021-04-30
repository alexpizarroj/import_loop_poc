from pprint import pprint as pp
import sys


def main():
    try:
        import import_loop_poc.cyclic_package
    except AttributeError as e:
        print("An error occurred - execution stopped: {!r}".format(e))
        print("")
        print("Modules currently imported:")
        modules_currently_imported = {
            mod_name: mod
            for mod_name, mod in sys.modules.items()
            if mod_name.startswith("import_loop_poc")
        }
        pp(modules_currently_imported)
        module_symbols = {mod_name: dir(mod) for mod_name, mod in modules_currently_imported.items()}
        print("Module symbols")
        pp(module_symbols)
        print("")
        raise


if __name__ == "__main__":
    main()
