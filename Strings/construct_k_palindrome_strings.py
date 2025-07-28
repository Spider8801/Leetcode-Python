import collections


def canConstruct(s: str, k: int) -> bool:
    str_len=len(s)
    if str_len<k:
        return False
    if str_len==k:
        return True

    char_dict=collections.defaultdict(int)
    odd_count =0
    for c in s:
        char_dict[c]+=1

    for frequency in char_dict.values():
        if frequency %2==1:
            odd_count +=1
    if odd_count>k:
        return False
    return True

def main():
    print(f"{canConstruct('annabelle',2)}")

if __name__=="__main__":
    main()