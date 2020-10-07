my_score = int(input("Enter your score:"))
if my_score <= 59:
    print("Your grade is Unsatisfactory")
elif my_score <= 64:
    print("Your grade is Marginal")
elif my_score <= 75:
    print("Your grade is Satisfactory")
elif my_score <= 84:
    print("Your grade is Good")
elif my_score <= 94:
    print("Your grade is Very good")
elif my_score <= 100:
    print("Your grade is excellent")    
else:
    print("This score doesn't exist") 