#Convert a list and tuple into arrays
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

list_array = np.array(my_list)
tuple_array = np.array(my_tuple)

print("List to Array:", list_array)
print("Tuple to Array:", tuple_array)
