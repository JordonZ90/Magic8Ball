import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0, len(messages) -1)])
# This expression will produce a random number to use for the index regardless of the size of 'messages'
# You'll get a random number between 0 and the value of len(messages)

