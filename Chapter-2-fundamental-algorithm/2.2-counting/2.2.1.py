'''
Modify the algorithm above so that marks are read until an end-of-file is encountered. For this set of marks determine the total number of marks, the number of passes and the percentage pass rate.

''' 

def count_passed_students(marks):
    total_marks = 0
    passes = 0

    for mark in marks:
        total_marks += 1
        if mark >= 50:
            passes += 1

    pass_rate = (passes / total_marks) * 100
    return total_marks, passes, pass_rate


# initialize empty list to store marks
marks = []

# read marks
while True:
    mark_input = input('Enter a mark (or press Enter to finish) : ')
    if not mark_input:
        print('\nEnter marks obtained by students.\n')
    try:
        mark = int(mark_input)
        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print('Invalid mark. Please enter a mark between 0 and 100')
    except ValueError:
        print('Invalid input. Please enter a valid integer mark.')


total_marks, passes, pass_rate = count_passed_students(marks)

print('Total number of marks(students) : ', total_marks)
print('Number of passed students : ', passes)
print('Pass rate (%) : ', pass_rate)
