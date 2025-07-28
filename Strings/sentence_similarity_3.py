import collections


def areSentencesSimilar( sentence1: str, sentence2: str) -> bool:
    words1= sentence1.split()
    words2= sentence2.split()

    words1_len=len(words1)
    words2_len=len(words2)
        
    if words1_len>words2_len:
        words1,words2= words2, words1

    words1_deque= collections.deque(words1)
    words2_deque= collections.deque(words2)

    while words1_deque and words1_deque[0] == words2_deque[0]:
        words1_deque.popleft() 
        words2_deque.popleft() 

    while words1_deque and words1_deque[-1] == words2_deque[-1]:
        words1_deque.pop() 
        words2_deque.pop()

    return not words1_deque

def main():
    print(f"{areSentencesSimilar('annabelle','annabelle')}")

if __name__=="__main__":
    main()
