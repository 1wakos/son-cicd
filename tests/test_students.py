import pytest
from src.students import Students
from src.presence import Presence
from src.students_data import Data

# 3. operacje na studentach

def test_add():

    #Given:
    student1 = Data('Julia', 'Ciapala', Presence.absent)
    student2 = Data('Kasia', 'Liczydlo', Presence.present)
    student3 = Data('Ola', 'Nowak', Presence.present)

    #When:
    Students.add_student(student1)
    Students.add_student(student2)
    Students.add_student(student3)

    #Then:
    assert len(Students.students) == 3

def test_add_error():

    # Given:
    student1 = Data('Julia', 'Ciapala', Presence.absent)

    #When & Then:
    with pytest.raises(Exception):
        assert Students.add_student(student1)

# 4. operacje na obecnosci

def test_edit_attendance():

    #Given:
    student1 = Data('Julia', 'Ciapala', Presence.absent)

    #When:
    Students.edit_presence(student1, Presence.present)

    #Then:
    assert Students.students[0]['presence'] == Presence.present

def test_edit_attendance_same():
    # jesli chcemy edytowac na ta sama to dostaniemy wyjatek
    
    #Given & When:
    student1 = Data('Julia', 'Ciapala', Presence.present)
    
    #Then:
    with pytest.raises(Exception):
        Students.edit_presence(student1, Presence.present)

# 1. zapisywanie do pliku

def test_export_to_txt():
    Students.students.clear()

    student1 = Data('Julia', 'Ciapala', Presence.absent)
    student2 = Data('Kasia', 'Liczydlo', Presence.present)

    Students.add_student(student1)
    Students.add_student(student2)

    # When:
    path = 'students.txt'
    Students.export_to_txt(path)

    # Then:

    with open(path, 'r') as file:
        lines = file.readlines()

    assert len(lines) == 2
    assert 'Julia' in lines[0] and 'Ciapala' in lines[0] and 'absent' in lines[0]
    assert 'Kasia' in lines[1] and 'Liczydlo' in lines[1] and 'present' in lines[1]

    # os.remove(path)

# 2. wczytywanie z pliku

def test_import_from_txt():
    path = 'students.txt'

    # Given:
    Students.students.clear()

    # When:
    Students.import_from_txt(path)

    # Then:
    assert len(Students.students) == 2
    assert Students.students[0]['name'] == 'Julia'
    assert Students.students[0]['surname'] == 'Ciapala'
    assert Students.students[0]['presence'] == Presence.absent

    assert Students.students[1]['name'] == 'Kasia'
    assert Students.students[1]['surname'] == 'Liczydlo'
    assert Students.students[1]['presence'] == Presence.present
    

    # os.remove(path)