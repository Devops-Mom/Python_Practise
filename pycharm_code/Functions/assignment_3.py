# Master Yoda speaks a sentence in a different order.
# Let's say you want to convert a sentence to Yoda’s speech.
# Write a function named master_yoda which will take a string as input and return the output after reversing the words of the sentence.
#
# input: "Welcome to Home"
# output: "Home to Welcome"
def master_yoda(sen):
    words = sen.split(' ')
    terminator = ""

    if words[-1].endswith('.') or words[-1].endswith('?'):
        terminator = words[-1][-1]
        words[-1] = words[-1][:-1]

    words.reverse()

    new_sen = " ".join(words)
    new_sen += terminator

    return new_sen



print(master_yoda("Welcome to Home"))
print(master_yoda("How are you today?"))

