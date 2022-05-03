def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_desing = unprinted_designs.pop()
        print(f"Printing model: {current_desing}")
        completed_models.append(current_desing)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

#8.9 - 8.11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_messages(messages):
    for message in messages:
        print(message.title())

def show_sent_messages(sent_messages):
    for sent_message in sent_messages:
        print(sent_message.title())

messages = ['hello', 'sup', 'ok', 'fine', 'nice job']
sent_messages = []

send_messages(messages[:], sent_messages)
show_messages(messages)
show_sent_messages(sent_messages)


