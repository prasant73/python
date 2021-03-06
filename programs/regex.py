import re
text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha haha

MetaCharacters (needs to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and then ring it to an end"

pattern = re.compile(r"abc")
# pattern = re.compile(r"\.") # to test fo a special character, enter a backslas before it
pattern = re.compile(r"coreyms\.com")

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
