#!/usr/bin/env python3
"""Secure, customizable password generator. Uses only Python's standard library."""

import secrets
import string
import sys

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/|~"


def ask_yes_no(prompt, default=True):
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        answer = input(prompt + suffix).strip().lower()
        if not answer:
            return default
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def ask_integer(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Enter a number between {minimum} and {maximum}.")


def remove_ambiguous(characters):
    ambiguous = set("Il1O0")
    return "".join(char for char in characters if char not in ambiguous)


def generate_password(length, groups):
    """Generate a password with at least one character from each selected group."""
    if not groups:
        raise ValueError("At least one character group must be selected.")
    if length < len(groups):
        raise ValueError("Length is too short for the selected character groups.")

    pool = "".join(groups)
    result = [secrets.choice(group) for group in groups]
    result.extend(secrets.choice(pool) for _ in range(length - len(result)))
    secrets.SystemRandom().shuffle(result)
    return "".join(result)


def main():
    print("=" * 58)
    print("                 SECURE PASSWORD GENERATOR")
    print("=" * 58)
    print("Generate strong passwords locally on your computer.\n")

    while True:
        length = ask_integer("Password length (8-128): ", 8, 128)

        print("\nSelect character groups:")
        use_letters = ask_yes_no("Include letters (A-Z, a-z)?", True)
        use_numbers = ask_yes_no("Include numbers (0-9)?", True)
        use_symbols = ask_yes_no("Include symbols (!@#$...)?", True)
        avoid_ambiguous = ask_yes_no(
            "Avoid ambiguous characters (I, l, 1, O, 0)?", False
        )

        groups = []
        if use_letters:
            groups.append(LETTERS)
        if use_numbers:
            groups.append(NUMBERS)
        if use_symbols:
            groups.append(SYMBOLS)

        if avoid_ambiguous:
            groups = [remove_ambiguous(group) for group in groups]

        if not groups:
            print("\nError: Select at least one character group.\n")
            continue
        if length < len(groups):
            print("\nError: Password length is too short for the selected groups.\n")
            continue

        count = ask_integer("\nNumber of passwords to generate (1-20): ", 1, 20)

        print("\n" + "-" * 58)
        print(f"GENERATED PASSWORDS ({count})")
        print("-" * 58)
        for number in range(1, count + 1):
            print(f"{number:>2}. {generate_password(length, groups)}")
        print("-" * 58)
        print("Security tip: Use a unique password for every account.")
        print("Store passwords in a trusted password manager.\n")

        if not ask_yes_no("Generate another batch?", False):
            print("\nThank you for using Secure Password Generator.")
            break
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram stopped by user.")
        sys.exit(0)
