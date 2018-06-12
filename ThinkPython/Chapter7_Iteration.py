import math
# [Qns 1: Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.
# It should continue until the user enters 'done', and then return the value of the last expression it evaluated.]


def eval_loop():
    isDone = False
    while isDone == False:
        quest = input("Tell me what you want to calculate :")
        if str(quest).lower() != "done":
            print(eval(quest))
            last_quest = eval(quest)
        else:
            isDone == True
            print("Im done.. exited")
            print("Your last quest result was:", last_quest)


eval_loop()
