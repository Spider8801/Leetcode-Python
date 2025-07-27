def binaryGap(n: int) -> int:
    current_one_index=-1
    max_distance=0
    current_index=0

    while n>0:

        if (n&1)==1:
            
            if (current_one_index !=-1):
                distance=current_index-current_one_index
                max_distance=max(distance, max_distance)

            current_one_index=current_index
        current_index+=1

        n=n>>1

    return max_distance

def main():
    print(f"{binaryGap(7)} is the distance for the number 7")


if __name__=="__main__":
    main()
    