set1 = {'F', 'Y', 'E', 'I', 'O'}
set2 = {'E', 'W', 'O', 'A', 'T', 'C'}

union = set1.intersection(set2)
totalguests = list(union)

print("Total guests are: ", len(totalguests))
print("Guests Lists: ", totalguests)
