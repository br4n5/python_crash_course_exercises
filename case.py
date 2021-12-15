name='Eric'
personal_message = f'Hello {name}, would you like to learn anything new today?'
print(personal_message)

first_name = 'bruno'
second_name = 'bedeschi de paula'
last_name = 'ribeiro'
full_name = f'{first_name} {second_name} {last_name}'
#I put double appostrophe here to emulate how a machine would "speak" to somebody.
welcome_message = f"""Welcome back, {full_name.title()}, to the World's top place in the world!"""
print (welcome_message)

name = 'SuSaNa'
print (name.upper())
print (name.lower())
print (name.title())

famous_person = ' Malcom X '
#isn't using lstrip and rstrip with strip waste of time? why not just use strip?
famous_person.lstrip()
famous_person.rstrip()
famous_person = famous_person.strip()
message = '\t"Education is the passport to the future, \n\tfor tomorrow belongs to those who prepare for it today".'
famous_person_message = (f'{message} \n\t{famous_person}')
print(famous_person_message)