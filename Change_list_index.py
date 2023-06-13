# I change this position using index / pop / insert
# but I can do it using sort function
# when developed a game then follow a proper data structure 

hotbot = [
    'Gun',
    'Knife',
    'Power',
    'Sword',
    'Battle_field'
]
index = hotbot.index('Sword')
item = hotbot.pop(index)
place = hotbot.insert(0, item)
print(hotbot)

# ----------------------------

#hotbot = [
    # 'B',
    # 'C',
    # 'D',
    # 'A',
    # 'E'
#]
# place = hotbot.sort()
# print(hotbot)
