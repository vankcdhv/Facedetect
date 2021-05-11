import mysql.connector


class PeopleDB:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user='root',
            password='123456',
            database='face_detect'
        )

    def add(self, people):
        mycursor = self.__mydb.cursor()

        sql = "SELECT * FROM People WHERE ID = " + str(people.getID())
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        isRecordExisted = 0
        for row in myresult:
            isRecordExisted = 1
        if(isRecordExisted == 1):
            sql = "UPDATE People SET Name = %s, Gender = %s, Age = %s WHERE ID = %s"
            val = (people.getName(), people.getGender(), people.getAge(), people.getID())
            mycursor.execute(sql, val)
            self.__mydb.commit()
            print(mycursor.rowcount, "record updated.")
        else:
            sql = "INSERT INTO People (id, name, gender, age) VALUES (%s, %s, %s, %s)"
            val = (people.getID(), people.getName(), people.getGender(), people.getAge())
            mycursor.execute(sql, val)
            self.__mydb.commit()
            print(mycursor.rowcount, "record inserted.")
    def getByID(self, id):
        mycursor = self.__mydb.cursor()
        sql = "SELECT * FROM People WHERE ID = " + str(id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        profile = None
        for row in myresult:
            profile = row
        return profile
