def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    # a = deque([])
    a = []
    count = 0

    for i in range(len(pushed)):
        # a.appendleft(pushed[i])
        a.insert(0, pushed[i])
        while(a and a[0] == popped[count]):
            a.pop(0)
            count += 1
    return not a
        
        
        