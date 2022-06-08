'''
Xuan Guo
CS 5001, Fall 2020

This program gets the course number from the student and check if student can
select the course they entered.
'''


def main():

    course_id = input('Enter a course number: ').upper().replace(' ', '')
    is_valid_course = course_id == 'X101' or course_id == 'X102' or\
        course_id == 'B500' or course_id == 'B525' or course_id == 'B701'
    no_prerequest_course = course_id == 'X101' or course_id == 'X102'

    if not is_valid_course:
        print('Invalid course number')
    elif no_prerequest_course:
        print('You have successfully registered for {}'.format(course_id))
    else:
        grade_x101 = input('What grade did you get for X101? ').lower()
        grade_x102 = input('What grade did you get for X102? ').lower()
        is_grade_satisfy = (grade_x101 == 'a' or grade_x101 == 'b') and\
            (grade_x102 == 'a' or grade_x102 == 'b' or grade_x102 == 'c')
        if is_grade_satisfy:
            print(
                'You meet all the prerequisites and have successfully',
                'registered for {}'.format(course_id)
                )
        else:
            print('You do not meet the prerequisites for {}'.format(course_id))


if __name__ == '__main__':
    main()
