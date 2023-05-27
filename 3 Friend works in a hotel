friend_one = []
friend_two = []
friend_three = []

for i in range(15, 150):
    if i % 3 == 0:
      friend_one.append(i)
    if i % 5 == 0:
      friend_two.append(i)
    if i % 8 == 0:
      friend_three.append(i)
      
print("1st friend I are  working:", friend_one)   
print("2nd Friend II are working:", friend_two) 
print("3rd Friend III are working:", friend_three) 

_calculate_together_works = []

for j in friend_one:
    if j in friend_two and j in friend_three:
        _calculate_together_works.append(j)
        
print("All friend are working:", _calculate_together_works)  

# Answer: 
# 1st friend I are  working: [15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147]
# 2nd Friend II are working: [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
# 3rd Friend III are working: [16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144]
# All friend are working: [120]
