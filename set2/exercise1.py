"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# this line is a variable with "some_words" being the variable and the list of words being the value
# it will write "what does this line do?" 
some_words = ["what", "does", "this", "line", "do", "?"]

# the "in" keyword will check if the word "word" is present in the list of some_words above
#it will return a boolean.
#it will return "False" because the word "word" is not present in the list of some_words above
for word in some_words:
    print(word)

# it will cycle through each list item. "x" loks to mean cycle through each item
# what
# does
# this 
# line
# do
#?
for x in some_words:
    print(x)

#this wil print "what does this line do?" 
#because "some_words" contains a list of those words
print(some_words)

# lens counts the number of items in a list.
# the list "some_words" has 6 items so is therefore greater than 3
#this will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# this will print platform information eg Linux
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
