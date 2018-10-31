import time
import random

def sleep():
    random_num = random.randint(0,10)
    time.sleep(int(random_num))
    print("BOO!")


def trick_or_treat():
    word = random.choice(["Trick","Treat"])
    print(word)


def string(sentence):
    full_sentence = ("spooky " + str(sentence))
    print(full_sentence)
sleep()
trick_or_treat()
string(sentence=input("what sentence do you want? "))