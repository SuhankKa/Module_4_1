# А как делить?

def divide(first, second):
    if second != 0:
        answer = int(first) / int(second)
        print(answer)
        return answer

    else:
        from math import inf 
        print(inf)
        return inf
