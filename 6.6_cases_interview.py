favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
list_interview = ['jen', 'phil', 'vadim', 'sasha', 'timur']

for name in list_interview:
 if name in favorite_languages.keys():
  print("Thank you for interview", name.title(), "!")
 else:
  print("Are you want to participate", name.title(), "?")