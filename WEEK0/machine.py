emoticon = " ... :( "
def main (): 
    global emoticon
    say("Is anyone there?" + emoticon)

def say(message):
    input(message + "... ")
    emoticon = "\U0001F60D"  # Smiling face with heart-eyes emoji
    print("\U0001F4AC") 
    print("...")  # Envelope with arrow
    print("Voice message sent") 
    print("Oh, and by the way, I love you! " + emoticon)
    print("\U0001F49C\U0001F49C\U0001F49C")  # Purple heart emoji
    return message

main()