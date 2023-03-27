depth = int(input("Enter the depth of the well: "))
daily_climbed = int(input("Enter the daily distance climbed by the snail: "))
night_climbed = int(input("Enter the night distance slide down by the snail: "))
while daily_climbed <= night_climbed:
    print("No sorry, the daily distance has to be bigger than the night distance, enter them again!")
    daily_climbed = int(input("Enter the daily distance climbed by the snail: "))
    night_climbed = int(input("Enter the night distance slide down by the snail: "))
i = 0
a = 0
while a < depth:
    i += 1
    a += daily_climbed
    if a > depth:
        break
    a -= night_climbed
print('-    The snail will exit in', i, 'days.')
