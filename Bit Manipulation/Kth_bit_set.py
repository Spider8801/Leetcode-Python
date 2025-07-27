def check_kth_bit(num:int ,k:int)->bool:
    return bool(num&(1<<k)!=0) #don't use == operator here as it has higher precedence than bitwise AND and OR operation
    
def main():
    print(check_kth_bit(7,2))    

if __name__=="__main__":
    main()
