count = 1

while count <= 5:
    print("Iteration: ", count)
    count += 1

#break
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target found!")
        break

#continue
scores = [27, 30, 55, 78, 62, 92, 34]
for score in scores:
    if score < 50:
        continue
    print(score)

