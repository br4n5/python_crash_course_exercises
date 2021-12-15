cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
numbers = [0,3,1,2]
numbers.sort()
print(numbers)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
numbers = [0,3,1,2]
numbers.sort(reverse=True)
print(numbers)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)
print('\nAnd here is the sorted list:')
print(sorted(cars))
print('\nAnd here is the reverse alphabetical sorted list:')
cars.sort(reverse=True) #guess is better to forget about SORT since it changes the list FOREVER???
print(cars)
print(len(cars))

print('\tfrom here, exercise')

places = ['seoul', 'taj mahal', 'avatar mountains', 'tokyo', 'highlands', ]
print('original_list')
print(places)
print('this is a sorted list')
print(sorted(places))
print('this is a reversed sorted list')
sorted_places = sorted(places,reverse=True)
print(sorted_places)
print("this is to confirm the list hasn't changed")
print(list)