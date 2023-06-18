# Slice notation on a list 
# We can add items/values/elements using index number
# Do not use insert() function
# If we used built-in functions it's takes more memory which is not helpful for program runtime

to_list = ["a", "c", 1, 2, 3]
new_items = "b"
to_list[1:1] = new_items

# to_list.insert(1, new_items)

print(to_list)
