from datetime import datetime, timedelta
import logging
import mysql.connector
from src.exception import CustomException
import sys

class Patron:
    def __init__(self):
        pass

    def connect_db(self):
        logging.info("Establishing connection with MySQL")
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="LMS"
        )

    def add(self, name, book_issue, issue_date):
        logging.info("Adding information of patron")
        try:
            conn = self.connect_db()
            cursor = conn.cursor()

            fetquery = "SELECT BookID FROM books WHERE name = %s"
            value = (book_issue,)
            cursor.execute(fetquery, value)
            bookid = cursor.fetchone()

            if bookid is None:
                raise ValueError(f"No book found with name {book_issue}")


            try:
                issue_date_obj = datetime.strptime(issue_date, '%Y-%m-%d')  
            except ValueError:
                raise ValueError(f"Invalid date format for issue_date: {issue_date}. Expected format: YYYY-MM-DD")

            
            return_date = issue_date_obj + timedelta(days=20)  


            return_date_str = return_date.strftime('%Y-%m-%d')


            query = "INSERT INTO patron(name, BookID, issue_date, return_date) VALUES (%s, %s, %s, %s)"
            Val = (name, bookid[0], issue_date_obj.strftime('%Y-%m-%d'), return_date_str)  

            cursor.execute(query, Val)
            conn.commit()

            logging.info("Patron added to the database")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise CustomException(e, sys)
        
        finally:
            cursor.close()
            conn.close()

    def patronInfo(self,name):

        try:
            logging.info("retrieving the information")
            conn = self.connect_db()
            cursor = conn.cursor()

            query  = "select * from patron where name = %s"
            value = (name,)

            cursor.execute(query,value)
            fetched_values = cursor.fetchall()
            # print(fetched_values[0][1])

            bookid = fetched_values[0][2]
            query1 = "select name from books where BookID = %s"
            val = (bookid,)
            cursor.execute(query1,val)
            nameofbook = cursor.fetchone()

            print(f"ID of the patron :{fetched_values[0][0]}")
            print(f"Name of the patron :{fetched_values[0][1]}")
            print(f"Book issued :{nameofbook[0]}")
            print(f"issue date of book :{fetched_values[0][3]}")
            print(f"return date of book :{fetched_values[0][4]}")


            
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise CustomException(e,sys)
        
        finally:
            cursor.close()
            conn.close()


