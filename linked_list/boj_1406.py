import sys
input = sys.stdin.readline

cursor_left = list(input().rstrip())
cursor_right = []

command_number = int(input())

for _ in range(command_number):
    commands = input().split()
    command = commands[0]

    if command == 'L':
        if cursor_left:
            cursor_right.append(cursor_left.pop())
    elif command == 'D':
        if cursor_right:
            cursor_left.append(cursor_right.pop())
    elif command == 'B':
        if cursor_left:
            cursor_left.pop()
    elif command == 'P':
        input_string = commands[1]
        cursor_left.append(input_string)

print("".join(cursor_left) + "".join(list(reversed(cursor_right))))

