#!/usr/bin/env python3
"""A minimal text-based Windows 98 simulator.

This version adds a handful of simple "applications" such as Notepad
and a calculator to make the environment feel a little more like a
usable desktop.

It also includes some light ASCII-art styling and optional colors so
the interface looks a little closer to the classic operating system."""

import os
import sys
import time

try:  # Optional terminal colors
    from colorama import Fore, Style, init
    init(autoreset=True)
except Exception:  # pragma: no cover - color is purely cosmetic
    class _Dummy:
        def __getattr__(self, name):
            return ""

    Fore = Style = _Dummy()


def boot_screen():
    logo = r"""
 __        ___           _                  _  _   _  
 \ \      / (_)_ __   __| | _____      ____| || | | | 
  \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / _` || | | | 
   \ V  V / | | | | | (_| |  __/\ V  V / (_| || |_| | 
    \_/\_/  |_|_| |_|\__,_|\___| \_/\_/ \__,_|\___/|_|
"""
    print(Fore.CYAN + Style.BRIGHT + logo + Style.RESET_ALL)
    print("Booting Windows 98...")
    for i in range(1, 6):
        sys.stdout.write(f"Loading system files: {i*20}%\r")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\nWelcome to Windows 98!\n")


def my_computer():
    """Display the contents of a directory."""
    path = input("Enter directory path (default current): ") or "."
    try:
        for entry in os.listdir(path):
            print(f" - {entry}")
    except FileNotFoundError:
        print("Directory not found.")
    print()


def notepad():
    """Very small text editor that writes a file."""
    filename = input("File to edit: ") or "untitled.txt"
    print("Enter text. A single '.' on its own line saves and exits.")
    lines = []
    while True:
        line = input()
        if line == ".":
            break
        lines.append(line)
    with open(filename, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"Saved {filename}\n")


def calculator():
    """Evaluate a basic arithmetic expression."""
    expr = input("Expression: ")
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        print(f"Result: {result}\n")
    except Exception as exc:
        print(f"Error: {exc}\n")


def control_panel():
    """Placeholder for system settings."""
    print("Opening Control Panel...")
    print("No configurable settings in this simulation yet.\n")


def show_start_menu():
    options = {
        "1": ("My Computer", my_computer),
        "2": ("Notepad", notepad),
        "3": ("Calculator", calculator),
        "4": ("Control Panel", control_panel),
        "5": ("Shut Down", None),
    }

    width = 26
    border = "+" + "-" * width + "+"

    while True:
        print(Fore.WHITE + border)
        title = " Start Menu "
        print(Fore.WHITE + "|" + Style.BRIGHT + title.center(width) + Style.RESET_ALL + Fore.WHITE + "|")
        print(Fore.WHITE + border)
        for key, (label, _) in options.items():
            print(Fore.WHITE + f"| {key}. {label:<{width-4}}|")
        print(Fore.WHITE + border + Style.RESET_ALL)
        choice = input("Select an option: ")
        if choice == "5":
            print("Shutting down...")
            break
        action = options.get(choice)
        if action:
            action[1]()
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    boot_screen()
    show_start_menu()

