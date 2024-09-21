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


            query = "INSERT INTO patron(name, BookID, issue_date, return_date,bookreturned) VALUES (%s, %s, %s, %s,%s)"
            Val = (name, bookid[0], issue_date_obj.strftime('%Y-%m-%d'), return_date_str,False)  

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
            if fetched_values[0][5] == 0:
                print("book not returned ")
            else:
                print("book returned")



            
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise CustomException(e,sys)
        
        finally:
            cursor.close()
            conn.close()


    def check_defaulter(self,name):
        
        logging.info("checking for the defaulter ")
        try:
            
            conn = self.connect_db()
            cursor = conn.cursor()
            query="select return_date,bookreturned from patron where name = %s"
            values =(name,)
            cursor.execute(query,values)
            fetched_values = cursor.fetchall()

            returningDate = fetched_values[0][0]
            isreturn = fetched_values[0][1]

            if isreturn:
                print(f"{name} returned the book ")
            else:
                if self.check(isreturn):
                    print(f"{name} has to returned the book with fine")
                else:
                    print(f"{name} can return the book till {returningDate}")
                    logging.info("checked for the defaulter ")
                
        except Exception as e :
            raise CustomException(e,sys)
        finally:
            cursor.close()
            conn.close()

            # helper function for check_defaulter
    def check(self, input_date):
        today_date = datetime.now().date()

        if isinstance(input_date, int) and input_date != 0:
            input_date_str = str(input_date)  
            try:
                input_date = datetime.strptime(input_date_str, '%Y%m%d').date()  
            except ValueError:
                print(f"Invalid date format for input: {input_date}")
                return False
        else:
            print(f"Invalid input date: {input_date}")
            return False
        if today_date > input_date:
            return True
        else:
            return False
        

    def listAllPatron(self):

        logging.info("listing list of patron")

        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            query ="select name from patron"
        
            cursor.execute(query)
            listofName = cursor.fetchall()
            for i , name1 in enumerate(listofName,start=1):
                print(f"{i}. {name1[0]}")
            

        except Exception as e:
            raise CustomException(e,sys)
        finally:
            cursor.close()
            conn.close()

    def getOverDuePatron(self):

        logging.info("getting the name of all OverDue patron ")
        try: 
            conn = self.connect_db()
            cursor = conn.cursor()
            
            query = " select name from patron where return_date < curdate() AND bookreturned = FALSE"
            cursor.execute(query)

            listOfName = cursor.fetchall()

            for i , name in enumerate(listOfName ,start= 1):
                print(f"{i}. {name[0]} ")
             
        except Exception as e:
            raise CustomException(e,sys)
        
        finally:
            cursor.close()
            conn.close()

    def bookreturned(self,name,bookname):

        logging.info("changing the bookreturned to true")
        try: 
            conn = self.connect_db()
            cursor = conn.cursor()
            
            query = "select BookID from books where name = %s"
            val = (bookname,)
            cursor.execute(query,val)
            bookid = cursor.fetchall()

            query = "update patron set bookreturned = TRUE where name = %s AND BooKID = %s"
            value = (name,bookid[0][0])
            cursor.execute(query,value)

            conn.commit()


            print(f"{name} has returned the book: {bookname}")
             
        except Exception as e:
            raise CustomException(e,sys)
        
        finally:
            cursor.close()
            conn.close()



