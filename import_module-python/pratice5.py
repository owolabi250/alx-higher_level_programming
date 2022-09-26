#!/usr/bin/python3
import hidden_4
for name in dir(hidden_4):
    # if name[0] != "_" and name[1] != "_":
    #     print(name)


    if name[0] == "_" and name[1] == "_":
        continue
    print(name)


    # if name[:2] != "__":
    #     print(name)


    # if "__" not in name:
    #     print(name)