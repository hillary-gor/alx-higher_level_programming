#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Chikezi", "Success")
say_my_name("Succy", "Nice")
say_my_name("Succy")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
