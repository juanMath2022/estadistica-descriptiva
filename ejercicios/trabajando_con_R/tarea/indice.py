letters = [chr(l) for l in range(ord('A'),ord('I')) ]
print(letters)

letters_index = [i+1 for i in range(len(letters))]    
print(letters_index)

if 0 % 2 == 0:
    print('par')