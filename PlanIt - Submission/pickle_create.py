import pickle

m = [0, 0, 0, 0, 0, 0, 0, 0, 0]
t = [0, 0, 0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0, 0, 0]
th = [0, 0, 0, 0, 0, 0, 0, 0, 0]
f = [0, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0, 0, 0, 0, 0]
su = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# List = time you sleep written as hours before 12, time you wake up written as hours after 12,
# school, dinner, a1, a2, a3, a4, a5

file = open('Days\Monday.pickle', 'wb')
file2 = open('Days\Tuesday.pickle', 'wb')
file3= open('Days\Wednesday.pickle', 'wb')
file4 = open('Days\Thursday.pickle', 'wb')
file5 = open('Days\Friday.pickle', 'wb')
file6 = open('Days\Saturday.pickle', 'wb')
file7 = open('Days\Sunday.pickle', 'wb')

pickle.dump(m, file)
pickle.dump(t, file2)
pickle.dump(w, file3)
pickle.dump(th, file4)
pickle.dump(f, file5)
pickle.dump(s, file6)
pickle.dump(su, file7)

file.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()

with open('Homework\\Monday.pickle', 'wb') as file:
    hw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name', 'Assignment Name']
    pickle.dump(hw, file)

with open('used_before.pickle', 'wb') as file:
    pickle.dump([0], file)