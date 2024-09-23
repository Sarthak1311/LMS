import mysql.connector
from datetime import date
from src.logger import logging
from src.exception import CustomException
import sys
class Book:
    def __init__(self):
        pass

    def _connect_db(self):
        logging.info("stableshing connection ")
        return mysql.connector.connect(
            host ="localhost",
            user ="root",
            password = "",
            db = "LMS"
        )
    def add(self,Book_name,Book_author,Book_Type,no_of_books):
        logging.info("adding the book in the table ")
        Book_name = Book_name.lower()
        Book_author = Book_author.lower()
        Book_Type = Book_Type.lower()
        try:
            conn =self._connect_db()
            cursor = conn.cursor()

            query = "INSERT INTO BOOKS(name,Author,Type,NoOfAvailable) VALUES (%s,%s,%s,%s)"
            Val = (Book_name,Book_author,Book_Type,no_of_books)

            cursor.execute(query ,Val)
            conn.commit()

            logging.info("book added into the tables ")

        except Exception as e:
            raise CustomException(e,sys)
        
        finally :
            cursor.close()
            conn.close()


    def remove(self,bookname):
        bookname = bookname.lower()
        logging.info("removing value from a table")
        try:
            conn =self._connect_db()
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

    def search(self, search_term):
        search_term = search_term.lower()
        logging.info(f"Searching for book with term: {search_term}")
        try:
            conn = self._connect_db()
            cursor = conn.cursor()

            query = "SELECT * FROM BOOKS WHERE name LIKE %s OR Author LIKE %s"
            val = (f"%{search_term}%", f"%{search_term}%")

            cursor.execute(query, val)
            results = cursor.fetchall()

            for row in results:
                print(row)  # or return the results
            logging.info("Search completed.")

        except Exception as e:
            raise CustomException(e, sys)
        
        finally:
            cursor.close()
            conn.close()

    def listAlltheBook(self):

        logging.info("listing all the book names")

        try:
            conn = self._connect_db()
            cursor = conn.cursor()

            query = "select name from books"
            cursor.execute(query)
            listOfName = cursor.fetchall()

            for i,name in enumerate(listOfName,start=1):
                print(f"{i}. {name[0]}")
            
        except Exception as e:
            raise CustomException(e,sys)
        finally:
            cursor.close()
            conn.close()

    def searchbyBooktype(self,book_type):
        book_type = book_type.lower()

        logging.info("searching by book_type")
        try:
            conn = self._connect_db()
            cursor = conn.cursor()

            query = "select name from books where Type = %s"
            val  = (book_type,)
            cursor.execute(query,val)
            listOfName = cursor.fetchall()

            for i , name in enumerate(listOfName,start=1):
                print(f"{i}. {name[0]}")
            
        except Exception as e:
            raise CustomException(e,sys)
        finally:
            cursor.close()
            conn.close()




    
