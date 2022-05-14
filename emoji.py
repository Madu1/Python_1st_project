def print_emoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


msg = input(">")
print(print_emoji(msg))
