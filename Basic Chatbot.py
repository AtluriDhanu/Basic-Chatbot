def chatbot():
    print('***** BASIC CHATBOT *****')
    print("Type 'Bye' to Exit")

    while True:
        user_input = input('You: ').lower()

        if user_input == 'hello':
            print('Bot: Hi!')

        elif user_input == 'how are you?':
            print('Bot: I am fine!')

        elif user_input == 'bye':
            print('Bot: GoodBye!')
            break

        else:
            print("Bot: Sorry, I don't understand")

chatbot()
