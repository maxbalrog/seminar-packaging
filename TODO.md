# TODO

Discuss definitions of package, module, import (`dir(module)`,
`module.__path__`).

## Imports
1. Different ways to import a package.
2. When import happens, all code from imported module is executed,
   check out `__name__` variable.
3. `__init__` module and definition of local variables inside it.

## sys.path hacks and why they are bad
1. Discuss `sys.path` and how it's working.
2. `sys.path.append('.' or '..')` binds you to a particular directory from which the script could be executed.
3. The order of directories in `sys.path` matters, could be fixed by `sys.path.insert` (you could rewrite default library with your own and imported module would depend on its path position within `sys.path`).

## Packaging
1. `pyproject.toml` file and repo structure.
2. pip editable install.