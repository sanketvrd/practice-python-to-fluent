#list compresion

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



new_list = [each for each in a if each % 2 == 0]

print(new_list)