shopping_list = ["apples", "bananas", 3, 4.5, 3]
print(shopping_list)

to_do_list = ["math_homework", "research for biology", "clean the room", "fun"]
first_item = to_do_list[0]
second_item = to_do_list[1]
third_item = to_do_list[2]
fourth_item = to_do_list[3]

print(first_item)
print(second_item)
print(third_item)
print(fourth_item)

#add data
shopping_list.append("3")
print(shopping_list)

shopping_list.insert(2, "oranges")
print(shopping_list)

#remove data
to_do_list.remove("research for biology")
print(to_do_list)

del to_do_list[2]
print(to_do_list)

#updating data
to_do_list[0] = "physics homework"
print(to_do_list)