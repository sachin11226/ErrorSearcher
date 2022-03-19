# ErrorSearcher
Search error on webbrowser
# Installation
```bash
pip install ErrorSearcher
```
# How to use 
```bash
from ErrorSearcher import  detect
detect(__file__)
```
Just write these line on top of program file which is throwing an error and the program will search the error on your default browser
# Example 
This will work 
```bash
from ErrorSearcher import detect
detect(__file__)

def subtract(a,b):
    return a-b

er=subtract('abx',"vas")
print(er)
```
This will not
```bash
def subtract(a,b):
    return a-b

er=subtract('abx',"vas")
print(er)

from ErrorSearcher import detect
detect(__file__)
