
num_cases = int(input())

for case in range(num_cases):

    text = input().strip()
    
    hidden_message = ''
    
    words = text.split()
    for word in words:
        hidden_message += word[0]

    print(hidden_message)