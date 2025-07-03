from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10


if __name__ == "__main__":
    print(" #1 - Top 5 students by average grade:")
    for row in select_1():
        print(row)

    print("\n #2 - Top student for subject 1:")
    print(select_2(subject_id=1))

    print("\n #3 - Average grade per group for subject 1:")
    for row in select_3(subject_id=1):
        print(row)

    print("\n #4 - Average grade across all grades:")
    print(select_4())

    print("\n #5 - Courses taught by teacher 2:")
    print(select_5(teacher_id=2))

    print("\n #6 - Students in group 1:")
    print(select_6(group_id=1))

    print("\n #7 - Grades for students in group 1 for subject 1:")
    for row in select_7(group_id=1, subject_id=1):
        print(row)

    print("\n #8 - Average grade given by teacher 2:")
    print(select_8(teacher_id=2))

    print("\n #9 - Subjects attended by student 1:")
    print(select_9(student_id=1))

    print("\n #10 - Subjects for student 1 taught by teacher 2:")
    print(select_10(student_id=1, teacher_id=2))