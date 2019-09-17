messages = ["Message 1", "Message 2", "Message 3"]
sent_messages = []


def show_messages(messages_to_show):
    print("Showing messages:")
    for message in messages_to_show:
        print(message)


def send_messages(messages_to_send):
    print("Sending messages:")
    for message in messages_to_send:
        print(message)
        sent_messages.append(message)
        messages.remove(message)


send_messages(messages)
show_messages(messages)
