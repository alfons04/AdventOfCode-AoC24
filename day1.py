import numpy as np

input = np.loadtxt(fname="input/input_day1.txt")

#--- part 1 -----

print(input)
left_side_list = []
right_side_list = []

for pair in input:
    for j in range(2):
        if(j==0):
           left_side_list.append(int(pair[j]))
        else:
            right_side_list.append(int(pair[j]))
        
left_side_list.sort()
right_side_list.sort()

diff = 0

for index in range(len(left_side_list)):
    diff += np.absolute(left_side_list[index] - right_side_list[index])

print(diff)

#--- part 1 -----


similarity_score = 0

for element in left_side_list:
    amount = right_side_list.count(element)
    similarity_score += (element*amount)

print(similarity_score)

        
