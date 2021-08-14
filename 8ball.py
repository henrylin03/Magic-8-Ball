import random

print("""
      
Hi, I'm Magic 8-Ball — it's a pleasure to meet you!
        ______
    ,dP9CGG8888@b,
  ,IP  _   Y88888@@b,
 dIi  (_)   G888888@b
dCII  (_)   G888888@@b
GCCIi     ,GG888888@@@
GGCCCCCCCGGG8888888@@@
GGGGCCCGGGG8888888@@@@
Y8GGGGGG888888888@@@@P
 Y8888888888888@@@@@P
 `Y888888888@@@@@@@P'
    `@@@@@@@@@@@P'
        """)


name = input("And what is your name?  ")

if name != "":
    print("\nFantastic, nice to meet you, """ + name + "!")

while True:
    ## input for question
    question = input("\nNow, feel free to ask me a yes-no question, and I will reveal the answer...  ")

    ## generating possible answers
    answers = ["It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    ## responding
    if question != "":
        if name == "":
            print("\nQuestion: " + question)
        else:
            print("\n" + name + " asks: " + question)
        print("Answer: " + answers[random.randint(1, len(answers))])
    continue