import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print('Ask a yes or no question')
input('>')
message = random.choice(messages)
print(message)