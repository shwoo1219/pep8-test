# noqa-free file: intentional PEP8 violations to trigger CI failure
import os, sys  # E401: multiple imports on one line

x=42  # E225: missing whitespace around operator

def foo(a,b):  # E231: missing whitespace after ','
  return a+b  # E111: indentation not a multiple of 4, E225: no spaces around +

very_long_variable_name = "this line is deliberately over eighty characters long to trigger E501"
