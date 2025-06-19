def main():
    emoji = input("How are we feeling today? ")
    emoji = convert(emoji)
    print(emoji)

def convert(emoji):
    if ":)" in emoji:
        emoji = emoji.replace(":)", "🙂")
    if ":(" in emoji:           
        emoji = emoji.replace(":(", "🙁")
    return emoji


    
main()

    