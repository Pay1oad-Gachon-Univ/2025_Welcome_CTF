with open('./flag', 'r', encoding='utf-8') as file:
    FLAG = file.read()

i = 0
while 1:
    if i == len(FLAG):
        break
    char = input(f'index {i}: ')
    if char == FLAG[i]:
        print('correct')
        i += 1
    else:
        print(ord(char) < ord(FLAG[i]))

print('what was the flag?')