#a = 5
a = 9 # a is not 8 and at least one is true 
b = 10

if a < 8 and b > 8:
    print ("Both are true.")
if a > 8 or b > 8:
    print("At least one is true.")
if a != 8:
    print("a is not 8.")


#SyntaxWarning: "is not" with 'int' literal. Did you mean "!="
# is not is used to compare values of different objects and prefferentially not used with intergers
# we use the =! operator to compare int
