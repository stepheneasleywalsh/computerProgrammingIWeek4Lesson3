name = input("What is your name?")
print("Hello", name)
friends = int(input("How many friends do you have?"))
chocolates = int(input("How many chocolates do you have?"))
share = chocolates//friends
remainder = chocolates%friends
print("You should give",share,"chocolates(s) to each friend and you will have",remainder,"left for you.")
quit()