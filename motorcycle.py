motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('speed donkey')
print(motorcycles)
donkeycycles = ['jumento', 'burro', 'super donkey']
donkeycycles.insert(0,'duckdonkey')
print(donkeycycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
del motorcycles[1]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
#in pop you can leave empty for the last position in the list or use 0,1,2...
#for the sake of not messing with yourself, better ALWAYS use index
motorcycles = motorcycles.pop()
print(f'The last motorcycle I owned was a {motorcycles.title()}.')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f'\nA {too_expensive.title()} is just too f* expensive.')