test_case = int(input())

for _ in range(test_case):
    key_logger = list(input())
    left = []
    right = []

    for log in key_logger:
        if log == '<':
            if left:
                right.append(left.pop())
        elif log == ">":
            if right:
                left.append(right.pop())
        elif log == "-":
            if left:
                left.pop()
        else:
            left.append(log)
    print("".join(left) + "".join(reversed(right)))