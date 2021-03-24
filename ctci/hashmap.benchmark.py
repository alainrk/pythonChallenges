import math
from hashmap import HashMap

# MAP_LENGTH = 10485
MAP_LENGTH = 1048576
INSERTED_ELEMENTS = math.floor(MAP_LENGTH / 1)
hm = HashMap(MAP_LENGTH)
for i in range(INSERTED_ELEMENTS):
  hm.add(str(i), 666)

conflictPercentage = hm.conflicts/MAP_LENGTH

print('\nHashmap array length:', MAP_LENGTH)
print('Elements inserted:', INSERTED_ELEMENTS)
print(f'Conflicts: {hm.conflicts} ({conflictPercentage:.2%})\n')