"""Silly little program to calculate my grades in Coursera's
Programming for Everybody (Python)
__author__ = 'clamytoe'
from bs4 import BeautifulSoup
"""
# global variable to hold all of the grades
class_grades = dict()


def parse_quiz():
    """Used to parse the quiz html page"""
    global student, class_grades
    quiz = list()

    try:
        quiz_html = BeautifulSoup(open('quiz.html'), 'html5lib')
    except:
        html_doc = raw_input('Enter name for your quiz page: ')
        quiz_html = BeautifulSoup(open(html_doc))

    # get the student's name
    for a_tag in quiz_html.find_all('a'):
        if len(a_tag.attrs) > 0:
            if 'data-user-id' in a_tag.attrs:
                student = a_tag.getText('data-user-id')

    # gather quiz scores
    for table in quiz_html.find_all('table'):
        for row in table.find_all('tr', class_='course-quiz-item-score'):
            for span in row.find_all('td'):
                for info in span.find_all('span'):
                    line = info.text.split('Explanation')[0].strip()
                    if len(line) > 0:
                        score = line.split(' / ')
                        quiz.append(float(score[0]))

    class_grades['quiz'] = quiz[:]


def parse_assignments():
    """Used to parse the assignments page"""
    global class_grades
    assignment = list()

    try:
        index_html = BeautifulSoup(open('assignments.html'), 'html5lib')
    except:
        html_doc = raw_input('Enter name for your assignments page: ')
        index_html = BeautifulSoup(open(html_doc))

    # get the path and filename for the iframe page
    iframes = list()
    for attributes in index_html.find_all('iframe'):
        iframes.append(attributes.attrs['src'])

    iframe_html = iframes[0]

    try:
        assignments_html = BeautifulSoup(open(iframe_html), 'html5lib')
    except:
        print "Was not able to find " + iframe_html + "."
        print "Please make sure to save the complete web page. and try again."
        quit()

    for row in assignments_html.table.find_all('tr'):
        for data in row.find_all('td'):
            info = data.text
            if '.' in info and ':' not in info:
                assignment.append(float(info) / 10)

    class_grades['assignment'] = assignment[:]


def parse_exam():
    """Used to parse the exam page"""
    global class_grades

    try:
        exam_html = BeautifulSoup(open('exam.html'), 'html5lib')
    except:
        html_doc = raw_input('Enter name for your exam page: ')
        exam_html = BeautifulSoup(open(html_doc))
    exam_info = list()
    for row in exam_html.table.find_all('tr'):
        for data in row.find_all('td'):
            for info in data.find_all('span'):
                tmp = info.text.split('Explanation')
                exam_info.append(tmp[0].split(' / '))

    highest_grade = 0
    for entry in exam_info:
        if len(entry) > 1:
            if entry[0] > highest_grade:
                highest_grade = float(entry[0])

    class_grades['exam'] = [highest_grade]


def get_total(key):
    """Adds up the grades for each section and returns the total"""
    tot = 0
    for score in class_grades[key]:
        tot += score
    return tot


def generate_report():
    """Generates the report and displays it on the screen"""
    global student
    parse_quiz()
    parse_assignments()
    parse_exam()
    # grades = {
    #     'quiz': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    #     'assignment': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    #     'exam': [20]
    # }

    quiz_total = get_total('quiz')
    assignment_total = get_total('assignment')
    final_exam = get_total('exam')
    total = quiz_total + assignment_total +final_exam

    print "=================="
    print " ", student
    print "=================="
    print "     Quizzes:", quiz_total
    print " Assignments:", assignment_total
    print "  Final Exam:", final_exam
    print "------------------"
    print " Total Grade:", total

    if total > 233:
        print "\nYou passed with distinction!"
    elif total > 195:
        print "\nCongratulations, you passed."
    else:
        print "\nYou can always take up sewing..."


if __name__ == "__main__":
    generate_report()