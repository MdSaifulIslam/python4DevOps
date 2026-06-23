# Python Built-ins & Exceptions — Q&A Notes

A Q&A reference based on study sessions covering Python's `builtins` module and exception hierarchy.

---

## Q1: What's in the `built-in-exceptions.ipynb` notebook?

The notebook explores Python's exception hierarchy using `inspect` + `builtins` to print the tree of all classes inheriting from `Exception`.

### Key Exception Families

| Family | What it covers |
|---|---|
| `OSError` | Files, permissions, sockets, paths |
| `LookupError` | `IndexError`, `KeyError` |
| `ArithmeticError` | `ZeroDivisionError`, `OverflowError`, `FloatingPointError` |
| `ImportError` | `ModuleNotFoundError` |
| `RuntimeError` | `RecursionError`, `NotImplementedError` |
| `ValueError` / `TypeError` | Bad value vs. wrong type |
| `Warning` | Deprecations, syntax warnings, etc. |

### Key Concepts

- **`OSError` family** — Catch specific subclasses (`FileNotFoundError`, `PermissionError`, `TimeoutError`) when you want different recovery logic per case.
- **`KeyError`** — Missing dict key. Use `.get(key, default)` or `if key in dict` to avoid it.
- **`IndexError`** — List/tuple index out of range. Prevent with bounds checks or plain `for item in seq:`.
- **`ValueError` vs `TypeError`**
  - `ValueError` = right type, wrong value (`int("abc")`)
  - `TypeError` = wrong type entirely (`"a" + 3`)
- **`AttributeError`** — Accessing something that doesn't exist on an object. Often caused by a `None` or a typo.
- **`ImportError` / `ModuleNotFoundError`** — Module can't be found. Usually a missing package or wrong virtual env.

### Core Advice

> Always catch the **narrowest** exception class you can handle — catching `Exception` broadly hides the real cause of bugs.

---

## Q2: Are there exceptions outside of `Exception`?

Yes. Python's full hierarchy starts from `BaseException`, which has a few important ones **not** under `Exception`:

```
BaseException
├── Exception          ← everything in the notebook lives here
├── SystemExit         ← raised by sys.exit()
├── KeyboardInterrupt  ← raised when user presses Ctrl+C
└── GeneratorExit      ← raised when a generator is closed
```

### Why they're separate from `Exception`

- **`SystemExit`** — Triggered by `sys.exit()`. Intentionally not under `Exception` so that `except Exception` doesn't accidentally swallow a deliberate program exit.
- **`KeyboardInterrupt`** — Triggered by `Ctrl+C`. Same reason — you don't want a bare `except Exception` to block the user from stopping a script.
- **`GeneratorExit`** — Raised inside a generator when `.close()` is called on it.

### Why this matters in DevOps scripts

```python
# This will accidentally catch SystemExit and KeyboardInterrupt
except BaseException:   # ← too broad, almost never do this
    pass

# This is safe — lets Ctrl+C and sys.exit() through
except Exception:
    pass
```

### What about `int`-related errors?

There's no `IntError`. Integer-related errors fall under:
- `ArithmeticError` → `ZeroDivisionError`, `OverflowError`
- `ValueError` → `int("abc")`

---

## Q3: What else is in `builtins` besides exceptions?

The `builtins` module contains everything available **without any import**. Three main categories:

### Built-in Types

```python
bool, int, float, complex          # numbers
str, bytes, bytearray              # text / binary
list, tuple, set, frozenset        # collections
dict                               # mapping
range, slice                       # sequences
type, object                       # base types
memoryview
```

### Built-in Functions

```python
# I/O
print(), input(), open(), help(), breakpoint()

# Type conversion
int(), str(), float(), bool(), list(), dict(), set(), tuple()
bin(), hex(), oct(), chr(), ord(), ascii(), repr(), format()

# Iteration & sequences
len(), range(), enumerate(), zip(), map(), filter(), sorted(), reversed()
all(), any(), iter(), next()
aiter(), anext()                   # async versions

# Introspection
type(), isinstance(), issubclass(), callable()
hasattr(), getattr(), setattr(), delattr()
dir(), vars(), locals(), globals(), id()

# Math
abs(), round(), min(), max(), sum(), pow(), divmod()

# Code execution
eval(), exec(), compile(), __import__(), __build_class__()

# Others
repr(), hash()
```

### Built-in Constants

```python
True, False, None
NotImplemented
Ellipsis        # the ... literal
__debug__
```

### Jupyter/IPython Extras (only in notebooks)

These appear when running in Jupyter but **won't exist** in plain `.py` scripts:

```python
display, get_ipython, execfile, runfile
__IPYTHON__
```

---

## Q4: Key takeaway about `builtins`

`int`, `str`, `list` etc. are **not** special keywords — they are just objects living in `builtins`. That's why you can technically reassign them (but should never):

```python
int = "oops"   # valid Python, but breaks everything
```

---

## How to Inspect Builtins Yourself

```python
import builtins

# See everything
print(dir(builtins))

# Only the exceptions
import inspect
for name, obj in vars(builtins).items():
    if inspect.isclass(obj) and issubclass(obj, Exception):
        print(name)
```

### The tree-printing function from the notebook

```python
import inspect, builtins

def show_err_tree(base, level=0, max_depth=1):
    if level > max_depth:
        return
    for name, obj in vars(builtins).items():
        if inspect.isclass(obj) and issubclass(obj, base) and obj is not base:
            print("\t" * level + f" - {name}")
            show_err_tree(obj, level + 1, max_depth)

show_err_tree(Exception, max_depth=4)
```
