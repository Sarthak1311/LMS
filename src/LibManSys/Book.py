import mysql.connector
from datetime import date
from src.logger import logging
from src.exception import CustomException
import sys
class Book:
    def __init__(self):
        pass

    def connect_db(self):
        logging.info("stableshing connection ")
        return mysql.connector.connect(
            host ="localhost",
            user ="root",
            password = "",
            db = "LMS"
        )
    def add(self,Book_name,Book_author,Book_Type,n):
        logging.info("adding the book in the table ")
        try:
            conn =self.connect_db()
            cursor = conn.cursor()

            query = "INSERT INTO BOOKS(name,Author,Type,NoOfAvailable) VALUES (%s,%s,%s,%s)"
            Val = (Book_name,Book_author,Book_Type,n)

            cursor.execute(query ,Val)
            conn.commit()

            logging.info("book added into the tables ")

        except Exception as e:
            raise CustomException(e,sys)
        
        finally :
            cursor.close()
            conn.close()


    def remove(self,bookname):
        logging.info("removing value from a table")
        try:
            conn =self.connect_db()
            cursor = conn.cursor()

            query = "Delete from BOOKS where name =%s"
            Val = (bookname,)

            cursor.execute(query ,Val)
            conn.commit()

            logging.info("book remove from the tables ")

        except Exception as e:
            raise CustomException(e,sys)
        
        finally :
            cursor.close()
            conn.close()



    
