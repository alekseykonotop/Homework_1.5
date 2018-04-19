dict_of_students = {
    100101: {
        'first_name': 'Михаил', 'last_name': 'Волков', 'sex': 'male', 'experience': True,
        'regular_score': [7, 6, 7, 8, 6], 'exam_score': 9
    },
    100102: {
        'first_name': 'Екатерина', 'last_name': 'Михайлова', 'sex': 'female', 'experience': False,
        'regular_score': [6, 5, 7, 6, 7], 'exam_score': 9
    },
    100103: {
        'first_name': 'Никита', 'last_name': 'Радионов', 'sex': 'male', 'experience': True,
        'regular_score': [4, 3, 5, 6, 7], 'exam_score': 6
    },
    100104: {
        'first_name': 'Марина', 'last_name': 'Онищенко', 'sex': 'female', 'experience': False,
        'regular_score': [7, 6, 8, 7, 7], 'exam_score': 9
    },
    100105: {
        'first_name': 'Сергей', 'last_name': 'Белокуров', 'sex': 'male', 'experience': True,
        'regular_score': [7, 9, 7, 8, 6], 'exam_score': 8
    },
    100106: {
        'first_name': 'Сергей', 'last_name': 'Белокуров', 'sex': 'male', 'experience': False,
        'regular_score': [6, 5, 7, 8, 7], 'exam_score': 7
    }
}


def mark_average_count_in_group(mark_type):
    marks_sum = 0
    marks_count = 0
    for student in dict_of_students.values():
        if mark_type == 'дз':
            marks_count += len(student['regular_score'])
            marks_sum += sum(student['regular_score'])
        elif mark_type == 'экз':
            marks_count += 1
            marks_sum += student['exam_score']
        else:
            print('Неверный тип оценки, повторите ввод.')
            break
    if marks_count == 0:
        print('Подсчет невозможен.')
    else:
        print(('Средняя оценка по {} в группе: {}\n').format(mark_type, round(marks_sum / marks_count, 2)))


# mark_average_count_in_group(input("Введите тип работы (дз/экз):").lower())

def mark_average_count_in_group_gender_of_student(sex_type, mark_type):
    marks_sum = 0
    marks_count = 0
    for student in dict_of_students.values():
        if sex_type == 'муж' and mark_type == 'дз':
            if student['sex'] == 'male':
                marks_count += len(student['regular_score'])
                marks_sum += sum(student['regular_score'])
        elif sex_type == 'жен' and mark_type == 'дз':
            if student['sex'] == 'female':
                marks_count += len(student['regular_score'])
                marks_sum += sum(student['regular_score'])
        elif sex_type == 'муж' and mark_type == 'экз':
            if student['sex'] == 'male':
                marks_count += 1
                marks_sum += student['exam_score']
        elif sex_type == 'жен' and mark_type == 'экз':
            if student['sex'] == 'female':
                marks_count += 1
                marks_sum += student['exam_score']
    if marks_count == 0:
        print('Подсчет невозможен.')
    else:
        print(
            ('Средняя оценка по {} по {} в группе {}\n').format(sex_type, mark_type, round(marks_sum / marks_count, 2)))


def run_mark_average_count_in_group_gender_of_student():
    sex_type = input('Введите пол студента (муж/жен)').lower()
    mark_type = input('Введите тип работы (дз/экз):').lower()
    mark_average_count_in_group_gender_of_student(sex_type, mark_type)


# run_mark_average_count_in_group_gender_of_student()


def mark_average_count_in_group_based_on_experience(experience_value, mark_type):
    marks_sum = 0
    marks_count = 0
    for student in dict_of_students.values():
        if experience_value == 'с опытом' and mark_type == 'дз':
            if student['experience'] == True:
                marks_count += len(student['regular_score'])
                marks_sum += sum(student['regular_score'])

        elif experience_value == 'без опыта' and mark_type == 'дз':
            if student['experience']:
                continue
            else:
                marks_count += len(student['regular_score'])
                marks_sum += sum(student['regular_score'])

        elif experience_value == 'с опытом' and mark_type == 'экз':
            if student['experience'] == True:
                marks_count += 1
                marks_sum += student['exam_score']

        else:  # т.е. когда выполняется 2 усл.student['experience'] == 'без опыта' and mark_type == 'экз':
            if student['experience']:
                continue
            else:
                marks_count += 1
                marks_sum += student['exam_score']

    if marks_count == 0:
        print('Подсчет невозможен.')
    else:
        print(('Средняя оценка студентов {} по {} в группе {}\n').format(experience_value, mark_type,
                                                                         round(marks_sum / marks_count, 2)))


def run_mark_average_count_in_group_based_on_experience():
    experience_value = input('Выберите наличие опыта (с опытом/без опыта)').lower()
    mark_type = input('Введите тип работы (дз/экз):').lower()
    mark_average_count_in_group_based_on_experience(experience_value, mark_type)


# run_mark_average_count_in_group_based_on_experience()


# Получить интегральную оценку по каждому

# def get_integral_score():
#   d = {}
#   for number, student in dict_of_students.items():
#     student_data = []
#     integral_score = 0
#     integral_score = ((sum(student['regular_score'])/len(student['regular_score'])) * 0.6 + student['exam_score'] * 0.4)
#     student_data.append(student['last_name'])
#     student_data.append(student['first_name'])
#     student_data.append(round(integral_score, 2))
#     d[number] = student_data
#   return d

# print(('Интегральная оценка студента {} {} равна {}').format(student['last_name'],  student['first_name'], round(integral_score, 2)))

def get_integral_score():
    d = {}
    for number, student in dict_of_students.items():
        student_data = 0
        integral_score = 0
        integral_score = (
                    (sum(student['regular_score']) / len(student['regular_score'])) * 0.6 + student['exam_score'] * 0.4)
        student_data = round(integral_score, 2)
        d[number] = student_data
    return d


print('список интегральных оценок \n', get_integral_score())

def max_integral_score():
    dict_with_integral_score = get_integral_score()
    inverse = [(value, key) for key, value in dict_with_integral_score.items()]
    print(('Лучший студент: {} {} с интегральной оценкой {}\n').format(dict_of_students[max(inverse)[1]]['last_name'],
                                                                       dict_of_students[max(inverse)[1]]['first_name'],
                                                                       max(inverse)[0]))
    return


# max_integral_score()


def main_def():
    while True:
        user_choice = input('''Выберите действие:
type - узнать среднюю оценку за ДЗ или экзамен; 
gender - узнать среднюю оценку за ДЗ или экзамен с учетом пола студента;
experience - узнать среднюю оценку за ДЗ или экзамен с учетом опыта студента;
best - определить лучшего студента;
q - выход
Введите ваш выбор тут: \n''').lower()
        if user_choice == 'type':
            mark_average_count_in_group(input("Введите тип работы (дз/экз):").lower())
        elif user_choice == 'gender':
            run_mark_average_count_in_group_gender_of_student()
        elif user_choice == 'experience':
            run_mark_average_count_in_group_based_on_experience()
        elif user_choice == 'best':
            max_integral_score()
        elif user_choice == 'q':
            print('Прорамма завершена')
            break
        else:
            print('Ошибка ввода, пожалуйста повторите.')


# main_def()
