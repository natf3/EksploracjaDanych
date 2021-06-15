import re
text1 = 'When Mr. Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton'

result1 = re.split("\s", text1)
print(result1)

result2 = re.sub("\s", "-", text1)
print(result2)

result3 = re.findall("\d+", text1)
print(result3)

result4 = re.search('\AWhen', text1)

if result4:
  print("pattern found")
else:
  print("pattern not found")

for match in re.finditer("Bilbo Baggins", text1):
    s = match.start()
    e = match.end()
    print('String match "%s" at %d:%d' % (text1[s:e], s, e))

result5 = re.match( r'(.*) of (.*?) .*', text1, re.M|re.I)

if result5:
   print("result5.group() : ", result5.group())
   print("result5.group(1) : ", result5.group(1))
   print("result5.group(2) : ", result5.group(2))
else:
   print("Nothing found")

result6 = re.escape(text1)
print(result6)

text2 = "abc123"
result7 = re.fullmatch('^abc\d+$', text2)
print(result7)
