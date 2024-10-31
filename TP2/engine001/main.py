from animation import (f , animator)

def main():
    animator(x = [0,10], t = [0,3], path = "data/animation.gif", f = f)

if __name__=="__main__":
    main()