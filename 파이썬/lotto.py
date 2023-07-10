# import random

# candidate_number = [x+1 for x in range(45)]
# random.shuffle(candidate_number)

# print(candidate_number[:6])


import random

candidate_number = [x+1 for x in range(45)]


print(random.sample(candidate_number, k=6))
