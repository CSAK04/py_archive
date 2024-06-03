import pickle

with open("t.dat",'wb') as t:
    while True:
        t = input("BOOK TITLE:")
        p = input("BOOK PRICE:")
        d = {"t":t,"p":p}
        pickle.dump(d,t)
        c = input("do you want to continue(y/n):")
        if c in "nN":
            break
    
