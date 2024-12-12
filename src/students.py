from src.presence import Presence
from src.exceptions import attendanceException
from src.students_data import Data

class Students:
    students = []

    def add_student(Data):

        if len(Data.name)<3 or len(Data.name)<3:
            raise(ValueError)
        else:
            student_data = {
            'name': Data.name,
            'surname': Data.surname,
            'presence': Data.presence
        }
        Students.students.append(student_data)

    def edit_presence(Data, new_presence: Presence):
        for student_data in Students.students:
            if student_data['name'] == Data.name and student_data['surname'] == Data.surname:
                if student_data['presence'] != new_presence:
                    student_data['presence'] = new_presence
                    break
                else:
                    raise attendanceException(f'The current student has been already marked as {new_presence}')

    def export_to_txt(path:str):
        with open(path, 'w') as f:
            for student in Students.students:
                f.write(f'{student['name']},{student['surname']},{student['presence']}\n')

    def import_from_txt(path:str):

        try:
        
            with open(path, 'r') as file:

                for line in file.readlines():
                    data = line.split(',')
                    
                    student = Data(data[0], data[1], getattr(Presence, data[2].split('.')[1].strip()))

                    Students.students.append({
                        'name': student.name,
                        'surname': student.surname,
                        'presence': student.presence
                    })

        except FileNotFoundError as e:
            raise FileNotFoundError(f"File doesn't exist at {path}")