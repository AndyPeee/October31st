import time
import random
def sleep():
    random_num = random.randint(0,10)
    time.sleep(int(random_num))
    print("BOO!")
def trick_or_treat():
    word = random.choice("Trick","Treat")
    print(word)


sleep()


trick_or_treat()

