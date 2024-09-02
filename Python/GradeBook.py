last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculus', 'poetry', 'history']

scores = [98, 97, 85, 88]
subjects.append('computer science')
scores.append(100)

gradebook = list(zip(subjects, scores))

gradebook.append(('visual arts', 93))

print(list(gradebook))
print(type(gradebook))

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

