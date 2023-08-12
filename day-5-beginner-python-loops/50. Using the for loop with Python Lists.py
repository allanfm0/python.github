# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

students_score = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(highest_score)