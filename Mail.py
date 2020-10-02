import ezgmail
unread_threads = ezgmail.unread()
print(ezgmail.summary(unread_threads))

for thread in unread_threads:
    print(f" Thread snippet: {thread.snippet}")
    for message in thread.messages:
        print(f"message: {message.body}")