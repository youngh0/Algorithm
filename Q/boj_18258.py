import sys
input = sys.stdin.readline

commands = int(input())

arr = []
push_pointer = 0
pop_pointer = 0

def q(command_line):
    global push_pointer
    global pop_pointer
    command = command_line[0]

    if command == "push":
        push_pointer += 1
        num = command_line[1]
        arr.append(num)
    elif command == "pop":
        if is_empty():
            print(-1)
        else:
            print(arr[pop_pointer])
            pop_pointer += 1
    elif command == "size":
        print(push_pointer-pop_pointer)
    elif command == "empty":
        if is_empty():
            print(1)
        else:
            print(0)
    elif command == "front":
        if is_empty():
            print(-1)
        else:
            print(arr[pop_pointer])
    elif command == "back":
        if is_empty():
            print(-1)
        else:
            print(arr[push_pointer-1])
def is_empty():
    return push_pointer == pop_pointer
for _ in range(commands):
    command_line = input().split()
    q(command_line)
