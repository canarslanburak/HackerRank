#name=["Harry","Berry","Tina","Akriti","Harsh"]
#score=[37.21,37.21,37.2,41,39]

#name=["Prashant","Pallavi","Dheeraj","Shivam"]
#score=[32,36,39,40]

#name=["Sona","Mona","Mini","Rita"]
#score=[-25.001,-25.0001,-25.000,-25.0]

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort()  #[['Akriti', 41], ['Berry', 37.21], ['Harry', 37.21], ['Harsh', 39], ['Tina', 37.2]]
s_punt = sorted(set(score for name, score in students))[1]
print('\n'.join(sorted(name for name, score in students if score == s_punt)))