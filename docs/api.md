# API Documentation

This project provides a tiny, well-documented "Hello, World!" utility that can be used as either a Python module or a command-line tool.

## Module: `src.hello`

### Overview

The module centres on a single `HelloGreeter` data class, a helper function `say_hello`, and a CLI-friendly `main` entry point.

### Public API

#### `HelloGreeter`

- **Purpose**: Compose greeting messages with a customizable leading phrase.
- **Constructor Parameters**
  - `greeting: str = "Hello"` — Opening word or phrase to begin the greeting.
- **Methods**
  - `greet(name: str = "World") -> str`  
    Returns a full greeting such as `"Hello, World!"`.

**Usage Example**

```python
from src.hello import HelloGreeter

greeter = HelloGreeter(greeting="Привет")
message = greeter.greet("мир")
print(message)  # Привет, мир!
```

#### `say_hello`

- **Signature**: `say_hello(name: str = "World") -> str`
- **Description**: Convenience function that returns a greeting using the default `HelloGreeter`.

**Usage Example**

```python
from src.hello import say_hello

print(say_hello())          # Hello, World!
print(say_hello("Cursor"))  # Hello, Cursor!
```

#### `main`

- **Signature**: `main() -> None`
- **Description**: Command-line entry point that prints a greeting based on provided arguments.

**CLI Examples**

```bash
python -m src.hello
# Hello, World!

python -m src.hello Cursor
# Hello, Cursor!

python -m src.hello Cursor --greeting Bonjour
# Bonjour, Cursor!
```

## Development Notes

- `say_hello` and `HelloGreeter.greet` are pure functions; they can be unit tested without touching I/O.
- `main` is thin and delegates all logic to `HelloGreeter`, easing future expansion (e.g., localisation, rich output formatting).
