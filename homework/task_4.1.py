import sqlite3

# запрос <L
conn = sqlite3.connect('teachers.db')
c = conn.cursor()

while True:
    # запрос ID
    student_id = input("Enter the student ID (or press Enter to exit): ")

    # Check if the user wants to exit
    if not student_id:
        break

    # запрос из БД
    c.execute("""
    SELECT s.Student_Id, s.Student_Name, s.School_Id, sc.School_Name
    FROM Students s
    JOIN School sc ON s.School_Id = sc.School_Id
    WHERE s.Student_Id = ?
    """, (student_id,))

    # вывод
    result = c.fetchone()
    if result:
        print(f"ID Студента: {result[0]}")
        print(f"Имя студента: {result[1]}")
        print(f"ID школы: {result[2]}")
        print(f"Название школы: {result[3]}")
    else:
        print("Студент с таким ID не найден.")

# финализация
conn.close()
