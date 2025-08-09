#!/usr/bin/env python3
"""A minimal text-based Windows 98 simulator."""

import sys
import time

def boot_screen():
    print("Booting Windows 98...")
    for i in range(1, 6):
        sys.stdout.write(f"Loading system files: {i*20}%\r")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\nWelcome to Windows 98!\n")

def show_start_menu():
    options = {
        "1": "My Computer",
        "2": "Control Panel",
        "3": "Shut Down"
    }
    while True:
        print("Start Menu")
        for key, value in options.items():
            print(f" {key}. {value}")
        choice = input("Select an option: ")
        if choice == "1":
            print("""Opening My Computer...
C:\\
 - Documents
 - Program Files
""")
        elif choice == "2":
            print("""Opening Control Panel...
Use this area to adjust system settings.
""")
        elif choice == "3":
            print("Shutting down...")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    boot_screen()
    show_start_menu()
