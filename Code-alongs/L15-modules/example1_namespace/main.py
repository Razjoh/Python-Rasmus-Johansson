import os,sys

os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

# import code from another module is executed when imported
import module1


# note __name__ is module1 when ran from outside of module1.py
# when module1 is run -> __name__ = "__main__" 


print(f"\n{'='*30}end main{'='*30}")