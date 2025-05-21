

def solution(N):

    binary = bin(N)[2:]
    print(binary)

    left = 0
    right = 0
    max_length = 0
    while right < len(binary):

        while right < len(binary) and binary[right] == '1' and left < right:
            left += 1
            max_length = max(max_length, right - left)
            
            if left == right:
                right+=1
        
        right+=1

    print(max_length)

if __name__ == '__main__':
    solution(1041)