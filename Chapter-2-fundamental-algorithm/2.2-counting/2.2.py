'''
Given a set of n students examination marks (in the range 0 to 100) make a count of the number 
of students that passed the examination. A pass is awarded for all marks of 50 and above.

'''


def count_passed_students(marks):
    count = 0

    for mark in marks:
        if mark >= 50:
            count += 1

    return count


marks = [75, 60, 45, 85, 30, 55, 88, 65]

passed_students = count_passed_students(marks)

print('Number of students who passed : ', passed_students)
