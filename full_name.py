first_name = 'ada'
last_name = 'lovelace'
#The f-string should be used like: f' then {} then {} then '
full_name = f'{first_name} {last_name}'
#for contactnating messages: VARIABLE then ( then f' then WRITE YOUR CRAP then {} then WRITE MORE CRAP OR A EXCLAMATION OR FULL STOP then ' then )
#funny thing is: these parentheses you put below do nothing. keep them for reference
message = (f'Hello, {full_name.title()}!')
print(message)

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

print("Language: \n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language =  favorite_language.strip()
print(favorite_language)