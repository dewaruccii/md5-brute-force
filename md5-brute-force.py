import hashlib
import os
from comment.comment import *
import datetime


def hash(param):
    hs = hashlib.md5(param.encode()).hexdigest()
    return hs


def _attack(word, md5):
    ftime = datetime.datetime.now()
    words = open(word, 'r')
    i = 1
    for w in words:
        hs = hash(w.rstrip())
        i = i + 1
        if(hs == md5):
            print("Found Password = -> " + LightGreen(md5) + " -> " + Success(w))
            print("Percobaan ke = " + str(i))
            stime = datetime.datetime.now()
            print("Waktu yang di butuhkan = {}".format(stime - ftime))
            exit()
        print(Error(hs))


def cekWordList(path):
    if(os.path.isfile(path)):
        return True
    else:
        return False


def menu():
    ls = input("Your list Password : ")
    if not (cekWordList(ls)):
        print("Word File Not Found!")
        return menu()
    h = input("MD5 : ")
    return _attack(ls, h)


if __name__ == "__main__":
    menu()
