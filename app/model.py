from app.extension import execute_read_query, execute_write_query

def fun_1():
    query = "select student_id as id, Roll_number as roll_no, Name as name, course_name as course from ankul"
    res = execute_read_query(query)
    return res

def fun_2(id, roll_no, name, course):
    query = """INSERT INTO ankul (student_id, Name, course_name, Roll_number) 
           VALUES ('{student_id}', '{Name}', '{course_name}', '{Roll_number}')""".format(student_id = id, Name = name, course_name= course, Roll_number=roll_no)
    res = execute_write_query(query)
    return

def fun_3():
    return

def fun_4():
    return