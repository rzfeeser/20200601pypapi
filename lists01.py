#!/usr/bin/python3

def main():
    # create a list and load some stuff in it
    zlist = []

    # this goes at the end of the empty list (pos 0)
    zlist.append("we are learning")

    # this goes at the end of the list (pos 1)
    zlist.append("python")

    # this goes at the end of the list (pos 2)
    zlist.append("restful api design")

    # show the entire list on the screen
    print(zlist)

    # just print the word python
    print(zlist[1])

if __name__ == "__main__":
    main()
