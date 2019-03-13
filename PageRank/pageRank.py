import numpy as np
import sys

def pageRank(M):
    



def main():
    no_of_pages = int(input("Number Of Pages:"))
    Link = []
    for i in range(no_of_pages):
        l = []
        for j in range(no_of_pages):
            try:
                l.append(int(input()))
            except:
                print("You are Adding Element More than the No of pages.")
                sys.exit(1)
                
        Link.append(l)
    M = np.array(Link)
    pageRank(M)




    



if __name__ == '__main__':
    main()
