import psycopg2

# function for printing all students
def getAllStudents(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM students")
    
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()

# function for adding students to the database
def addStudent(connection):
    cur = connection.cursor()

    firstName = input("Enter the first name: ")
    lastName = input("Enter the last name: ")
    email = input("Enter the email: ")
    enrollmentDate = input("Enter the enrollment date (YYYY-MM-DD): ")

    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        (firstName, lastName, email, enrollmentDate)
    )

    connection.commit()

    cur.close()

    print("Student added")

# function for updating student email
def updateStudentEmail(connection):
    cur = connection.cursor()
    studentId = int(input("Enter the student ID: "))
    newEmail = input("Enter the new email address: ")

    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (newEmail, studentId)
    )

    connection.commit()
    cur.close()

    print("Student updated")

# function for deleting students
def deleteStudent(connection):
    cur = connection.cursor()
    studentId = int(input("Enter the student ID: "))

    cur.execute("DELETE FROM students WHERE student_id = %s", (studentId,))

    connection.commit()
    cur.close()

    print("Student deleted")

# I used the psycopg library here to connect to my database, you need to update the parameters to fit your database server
postgresConnection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Iman@1112", port=5432)

# creating a while loop which will serve as my application
while True:
    print("Select an option:\n \n")
    print("Select 1 to print Students\n")
    print("Select 2 to add a student\n")
    print("Select 3 to update student email\n")
    print("select 4 to delete a student\n")
    print("Select -1 to quit")

    selection = int(input("Select Option: "))

    if(selection == -1):
        break
    elif(selection == 1):
        getAllStudents(postgresConnection)
    elif(selection == 2):
        addStudent(postgresConnection)
    elif(selection == 3):
        updateStudentEmail(postgresConnection)
    elif(selection == 4):
        deleteStudent(postgresConnection)

postgresConnection.close()

          
