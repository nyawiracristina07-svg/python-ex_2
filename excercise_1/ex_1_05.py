# a)
x = 3
if x > 2:
    print("big") #SyntaxError: expected ':'

# b)
y = 4
if y == 4:
    print("four") # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# c)
z = 0
if z == 0:
   print("zero") #IndentationError: expected an indented block after 'if' statement on line 13