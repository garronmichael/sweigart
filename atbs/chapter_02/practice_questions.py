# 1. True False

# 2. and or not

"""
3.
True and True --> True
True and False --> False
False and True --> False
False and False --> False

True or True --> True
True or False --> True
False or True --> True
False or False --> False

not True --> False
not False --> True
"""

"""
4. 
False
False
True
False
False
True
"""

# 5. > < <= >= == !=

# 6. == is the equal operator while = is the assignment operator

# 7. A condition is an expression that evaluates to a Boolean value. One use case is flow control

# 8.
spam = 0
if spam == 10:
    print('eggs') # block 1
    if spam > 5:
        print('bacon') # block 2
    else:
        print('ham') # block 3
    print('spam') # block 1
print('Done')

# 9.
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')