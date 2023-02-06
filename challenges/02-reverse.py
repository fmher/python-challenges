# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

string = 'hello'
string_list = ['bye-bye', 'neat']
alt_string = 'byee'

string = list(string)
string.reverse()


# print(''.join(string_list))
# print(list(string))     # converts to a list hello to => ['h', 'e', 'l', 'l', 'o']
# print(''.join(string))

string_list = ''.join(string_list)
string_list = list(string_list)
string_list.reverse()

print(alt_string[::-1])

