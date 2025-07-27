def swap_nums(a:int, b:int)-> any:
    a=a^b
    b=a^b
    a=a^b
    return a , b

def main():
    a,b=swap_nums(2,3)
    print(f"{a} and {b}")

if __name__=="__main__":
    main()