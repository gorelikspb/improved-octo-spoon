"""Hello World utilities and CLI entry point."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

DEFAULT_GREETING = "Hello"


@dataclass
class HelloGreeter:
    """Generate greeting messages.

    Parameters
    ----------
    greeting:
        Leading word or phrase to begin the greeting with. Defaults to ``"Hello"``.
    """

    greeting: str = DEFAULT_GREETING

    def greet(self, name: str = "World") -> str:
        """Compose a greeting for the provided ``name``.

        Parameters
        ----------
        name:
            Target of the greeting. Defaults to ``"World"``.

        Returns
        -------
        str
            Completed greeting, for example ``"Hello, World!"``.
        """

        return f"{self.greeting}, {name}!"


def say_hello(name: str = "World") -> str:
    """Return a greeting for the supplied ``name``."""

    return HelloGreeter().greet(name)


def main() -> None:
    """Print a greeting to standard output based on CLI arguments."""

    parser = argparse.ArgumentParser(description="Print a customizable greeting.")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet.")
    parser.add_argument(
        "--greeting",
        default=DEFAULT_GREETING,
        help="Greeting word or phrase to use (default: Hello).",
    )
    args = parser.parse_args()

    greeter = HelloGreeter(greeting=args.greeting)
    print(greeter.greet(args.name))


if __name__ == "__main__":
    main()
