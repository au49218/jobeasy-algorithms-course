# Hacker Rank Python: Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem
#
# Given the names and grades for each student in a class of
# students, store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade. Note: If
# there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a
# new line.


def list_nested(history_students):

    history_students.sort()
    N = len(history_students)

    grades_list = []
    for i in range(N):
        grades_list.append(history_students[i][1])
    grades_list.sort()
    min_grade = min(grades_list)
    grades_list_temp = grades_list[:]
    for i in range(len(grades_list)):
        if grades_list[i] == min_grade:
            grades_list_temp.pop(0)
        else:
            pass

    lowest2nd_names_list = []
    for i in range(N):
        if history_students[i][1] == grades_list_temp[0]:
            lowest2nd_names_list.append(history_students[i][0])

    for name in lowest2nd_names_list:
        print(name)


history_students_grades = [["Alpha", 5], ["Beta", 8],
                           ["Chi", 11], ["Delta", 15],
                           ["Epsilon", 8]]

list_nested(history_students_grades)

