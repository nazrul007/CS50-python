import cowsay
import sys

def main():
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])
        cowsay.trex("hello, " + sys.argv[1])

if (__name__=="__main__"):
    main()