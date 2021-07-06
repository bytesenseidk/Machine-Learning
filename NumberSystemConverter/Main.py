import os
import sys
import time
import keyboard
from BinaryToDecimal import BinaryToDecimal
from DecimalToBinary import DecimalToBinary
from DecimalToHex import DecimalToHex
from HexToDecimal import HexToDecimal


base_menu = str("""
    [ Number System Converter ]
[0] Exit
[1] Binary
[2] Hexadecimal
""")


def base_selection():
    bases = {
        "0": sys.exit,
        "1": binary,
        "2": hexadecimal
    }
    while True:
        os.system("cls")
        print(base_menu)
        print("[ Base Selection ]")
        try:
            choice = str(int(input("  >> ")))
            if -1 > int(choice) > 2:
                print("Please enter a number between 0 and 2")
                time.sleep(2)
                continue
        except TypeError:
            print("Please enter a number")
            time.sleep(2)
            continue
        method = bases[choice]
        return method()
        

def binary():
    methods = {"0": base_selection,
               "1": BinaryToDecimal,
               "2": DecimalToBinary}
    while True:
        os.system("cls")
        print("[ Binary Convertion ]\n\n[0] Back\n[1] Convert Binary\n[2] Convert Decimal\n")
        try:
            print("[ Base Selection ]")
            choice = str(int(input("  >> ")))
            if -1 > int(choice) > 2:
                print("Please enter a number between 0 and 2")
                time.sleep(2)
                continue
        except TypeError:
            print("Please enter a number")
            time.sleep(2)
            continue
        
        method = methods[choice]
        
        if method == base_selection:
            return base_selection()
        
        elif method == BinaryToDecimal:
            while True:
                os.system("cls")
                print("[ Binary to Decimal Convertion ]\nEnter Binary:")
                try:
                    convert_me = str(input("  >> "))
                except:
                    print("Enter a binary string please..")
                    time.sleep(2)
                    continue
                os.system("cls")
                print(f"\nResult: {BinaryToDecimal(convert_me)}")
                return continue_or_stop()
        
        elif method == DecimalToBinary:
            while True:
                os.system("cls")
                print("[ Decimal to Binary Convertion ]\nEnter Decimal:")
                try:
                    convert_me = str(input("  >> "))
                except:
                    print("Enter a numerical string please..")
                    time.sleep(2)
                    continue
                os.system("cls")
                print(f"\nResult: {DecimalToBinary(convert_me)}")
                return continue_or_stop()


def hexadecimal():
    methods = {"0": base_selection,
               "1": HexToDecimal,
               "2": DecimalToHex}
    while True:
        os.system("cls")
        print("[ Hexadecimal Convertion ]\n\n[0] Back\n[1] Convert Hexadecimal\n[2] Convert Decimal\n")
        try:
            print("[ Base Selection ]")
            choice = str(int(input("  >> ")))
            if -1 > int(choice) > 2:
                print("Please enter a number between 0 and 2")
                time.sleep(2)
                continue
        except TypeError:
            print("Please enter a number")
            time.sleep(2)
            continue
        
        method = methods[choice]
        
        if method == base_selection:
            return base_selection()
        
        elif method == HexToDecimal:
            while True:
                os.system("cls")
                print("[ Hexadecimal to Decimal Convertion ]\nEnter Hexadecimal:")
                try:
                    convert_me = str(input("  >> "))
                except:
                    print("Enter a hexadecimal string please..")
                    time.sleep(2)
                    continue
                os.system("cls")
                print(f"\nResult: {HexToDecimal(convert_me)}")
                return continue_or_stop()
        
        elif method == DecimalToHex:
            while True:
                os.system("cls")
                print("[ Decimal to Hexadecimal Convertion ]\nEnter Decimal:")
                try:
                    convert_me = str(input("  >> "))
                except:
                    print("Enter a numerical string please..")
                    time.sleep(2)
                    continue
                os.system("cls")
                print(f"\nResult: {DecimalToHex(convert_me)}")
                return continue_or_stop()
    
    
def continue_or_stop():
    try:
        print("\nConvertion Complete...\n\n"
                "Press Space to continue\n"
                "Press Escape to exit\n")
        while True:
            if keyboard.is_pressed("space"):
                base_selection()
            elif keyboard.is_pressed("escape"):
                break
    except:
        while True:
            if keyboard.is_pressed("space"):
                base_selection()
            elif keyboard.is_pressed("escape"):
                break

                
if __name__ == "__main__":
    base_selection()
