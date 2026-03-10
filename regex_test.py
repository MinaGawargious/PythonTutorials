import re
# Regular expressions are very powerful to search for text patterns inside text

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

snippets = r"""

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""

sentence = 'Start a sentence and then bring it to an end'

# A raw string in Python is a string prefixed with an r, and it tells Python NOT to use \ as an escape character and just read it literally. Important for regex since we want to treat strings literally for regex to interpret and not have Python do anything to them first
print("\tTab")
print(r"\tTab") # LITERALLY \tTab. Like an actual \, actual t, T, a, b

# re.compile() allows us to separate out patterns into variable and reuse pattern in multiple searches
pattern = re.compile(r"abc")
matches = pattern.finditer(text_to_search) # finditer returns an iterator that contains all matches
for match in matches:
    print(match) # <re.Match object; span=(1, 4), match='abc'>
    print(text_to_search[match.span()[0]:match.span()[1]])
    
pattern = re.compile(r".") # The dot is a special character/wildcard in regex that matches any character. To match some literal characters, like . we need to escape it. This goes for all the metacharacters in the metacharacter section
pattern = re.compile(r"\.")
matches = pattern.finditer(text_to_search)
for match in matches:
    print("literal dot:", match)
    
pattern = re.compile(r"coreyms\.com") # coreyms.com
matches = pattern.finditer(text_to_search)
for match in matches:
    print("coreyms.com:", match)
    
pattern = re.compile(r"\d") # digit 0-9
matches = pattern.finditer(text_to_search)
for match in matches:
    print("Digit 0-9 \d:", match)
    
pattern = re.compile(r"\D") # NOT a digit. Pattern is capital = NOT lowercase
matches = pattern.finditer(text_to_search)
for match in matches:
    print("Not a digit \D:", match)
    
pattern = re.compile(r"\w") # word character a-z, A-Z, 0-9, _
matches = pattern.finditer(text_to_search)
for match in matches:
    print("word character \w:", match)
    
pattern = re.compile(r"\W") # NOT a word character
matches = pattern.finditer(text_to_search)
for match in matches:
    print("word character \W:", match)
    
pattern = re.compile(r"\s") # whitespace (space, tab, newline)
matches = pattern.finditer(text_to_search)
for match in matches:
    print("word character \s:", match)
    
pattern = re.compile(r"\S") # NOT whitespace
matches = pattern.finditer(text_to_search)
for match in matches:
    print("word character \S:", match)
    
# We can also use anchors \b \B ^ $. These don't match characters, but rather invisible positions before or after characters. We use in conjunction with other patterns when searching


pattern = re.compile(r"\bHa") # \b means word boundary. Indiciated by whitespace or non-alphanumeric character (not a-zA-Z0-9). Matches first 2 Ha's in Ha HaHa
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"\bHa:", match)
    
pattern = re.compile(r"\BHa") # \B means NOT a word boundary.
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"\BHa:", match) # Matches 3rd Ha in Ha HaHa
    
pattern = re.compile(r"^Start") # ^ means beginning of a String
matches = pattern.finditer(sentence)
for match in matches:
    print(r"\^Start:", match) # Matches "Start" in sentence
    
pattern = re.compile(r"^sentence") # ^ means beginning of a String
matches = pattern.finditer(sentence)
for match in matches:
    print(r"\^sentence:", match) # No matches. "sentence" appears in the sentence variable, but not at the start
    
pattern = re.compile(r"end$") # $ means beginning of a string
matches = pattern.finditer(sentence)
for match in matches:
    print(r"end$:", match) # Matches "end" in sentence
    
pattern = re.compile(r"sentence$") # $ means end of a string
matches = pattern.finditer(sentence)
for match in matches:
    print(r"sentence$:", match) # No matches. "sentence" appears in the sentence variable, but not at the end
    
pattern = re.compile(r"\d\d\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"3 numbers", match) # Very important note: In 123456789, we matched 123, 456, 789. NOT 123, 234, 345, 456, 567, 678, 789. So this is a non-greedy search. TODO: look into greedy search in regex
    
# PHONE NUMBER SEARCH    

pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"Phone number:", match)
    
with open("regex_test_data.txt", "r") as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(r"Phone number in regex_test_data.txt:", match)
        
# The above pattern matches phone numbers with any character between the digits. To match characters with only - or . between characters, we do this:
pattern = re.compile(r"\d\d\d[.-]\d\d\d[.-]\d\d\d\d") # square brackets indicate character set. No need to escape dot apparently, but we CAN if we wanted. This character set matches 1 character that is either a - or a . and it does NOT match 2 characters
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"Phone number improved:", match)
    
# Within character set, the - is a special character. When at beginning or end, it's a literal -, but when put between characters, it can specify a range, like a-z
pattern = re.compile(r"[1-5a-zA-Z]")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"1-5a-zA-Z:", match)
    
# Another special character in character set is ^. Outside character set, it indicates beginning of string. Inside character set, it indicates NOT and negates the set
pattern = re.compile(r"[^1-5a-zA-Z]") # opposite of above. NOT 1-5a-zA-Z
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"^a-zA-Z:", match)
    
# Another special character in character set is ^. Outside character set, it indicates beginning of string. Inside character set, it indicates NOT and negates the set

# Back to the phone number example, we can use quantifiers to specify quantity. * means any number (0 or more), + means 1 or more, ? means exists or not (0 or 1), {n} means match n times, and {n, m} means match [n, m] times
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d") # old
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"phone number old:", match)
    
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"phone number new:", match)
    
# Now let's match names, like Mr. Schafer or Mr Smith
pattern = re.compile(r"Mr\.?\s[A-Z]\w*") # Match Mr or Mr. followed by a space, a capital letter, then any letter
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"Mr Names:", match)
    
# This does not match the Ms or Mrs names. To do that, use a group, which allow us to match multiple different patterns
pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*") # The group matches r OR s OR rs (the pipe is the or like in any language)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(r"All Names:", match)
    
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r"[\w.-]+@[\w-]+\.\w+")
matches = pattern.finditer(emails)
for match in matches:
    print(r"Emails:", match)
    
# Using groups:
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# We want google.com, coreyms.com, youtube.com, nasa.gov etc, without the preceding stuff
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)
for match in matches:
    print(match)
    print(rf"Whole domain {match.group(0)}, www. if it exists {match.group(1)}, domain name {match.group(2)}, and top-level domain name {match.group(3)}") # group 0 is everything we captured
    
# we can also use backreferences to reference our captured group
subbed_urls = pattern.sub(r"\2\3", urls) # Use group 2 and 3, which are match.group(2) and match.group(3)
print(f"{urls} -> {subbed_urls}")

# So far, we've been using finditer to get an iterator of matches with extra info and functionality, like <re.Match object; span=(1, 23), match='https://www.google.com'>
# But we can use other methods. Example, findall to return list of all matches. If we use groups, findall will return a tuple of the groups, NOT th full match

pattern = re.compile(r"[\w.-]+@[\w-]+\.\w+")
matches = pattern.findall(emails)
for match in matches:
    print(r"Emails:", match) # No groups = return matched String

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.findall(urls)
for match in matches:
    print(match) # Tuple of groups
    
# The match method checks the beginning of the string
pattern = re.compile(r"Start") # ^ means beginning of a String
match = pattern.match(sentence)
print(r"Start:", match) # Matches "Start" at start of in sentence

pattern = re.compile(r"end") # ^ means beginning of a String
match = pattern.match(sentence)
print(r"end:", match) # "end" is in sentence, just not at beginning so we return None

# To search within ENTIRE string, use search

pattern = re.compile(r"end") # ^ means beginning of a String
match = pattern.search(sentence)
print(r"end:", match) # "end" is in sentence, so search finds it. It only returns first match

# Lastly, we can use flags to make our lives easier in Python:
# If we wanted to match Start, but any character can be uppercase or lowercase, we'd have to do [Ss][Tt][Aa][Rr][Tt]. Instead, we can use flags
pattern = re.compile(r"start", re.IGNORECASE) # we could also use re.I
match = pattern.search(sentence)
print(r"re.IGNORECASE start", match)

# There is also a multiline flag that lets us use ^ and $ to match beginning and end of each line in multiline string vs. beginning or end of string

# Summary: finditer is most useful since match object is useful. findall returns array of matched strings, or array of tuples of matched GROUPS if we use groups. match matches at beginning of string, and search matches anywhere but only one instance. We also have flags to make our lives easier, like IGNORECASE

