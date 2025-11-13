# improved-octo-spoon

Simple "Hello, World!" utility with both a Python API and a CLI interface.

## Quick Start

```bash
python -m src.hello
```

Pass a custom name or greeting:

```bash
python -m src.hello Cursor --greeting Bonjour
```

## Python Usage

```python
from src.hello import say_hello, HelloGreeter

print(say_hello())              # Hello, World!
print(say_hello("Cursor"))      # Hello, Cursor!

greeter = HelloGreeter("Hi")
print(greeter.greet("team"))    # Hi, team!
```

## Documentation

Detailed API reference lives in `docs/api.md`.