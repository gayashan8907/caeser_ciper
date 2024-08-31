from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
play = True
def encoding(text,j):
    for a in text:
        for i in range(26):
            if alphabet[i]==a:
                x =i+j
                list.append(alphabet[x])
    return list
def decoding(text,j):
    for a in text:
        for i in range(26):
            if alphabet[i]==a:
                x =i-j
                list.append(alphabet[x])
    return list


while play:
    list = []
    user_input = input("Type 'encode' to encrypt,'decode' to decrypt:\n").lower()
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if shift>26:
        shift = shift%26
    if user_input == 'encode':
        encode = encoding(message, shift)
        print(f"Here is the result : {encode}")
    elif user_input == 'decode':
        decode = decoding(message, shift)
        print(f"Here is the result : {decode}")
    play_again = input("Type 'yes' to play again,other wise type 'no' :").lower()
    if play_again == 'no':
        play=False
        break
