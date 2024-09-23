from src.LibManSys.Patron import Patron
from src.LibManSys.Book import Book
import datetime
a =Patron()
b = Book()
# # a.add("pulkit tyagi","harry potter",datetime.datetime.now().strftime('%Y-%m-%d'))
# # a.patronInfo("sarthak tyagi")
# # a.add("puks","harry potter","2024-8-1")
# # a.getOverDuePatron()
# a.bookreturned("puks","harry potter")
# a.getOverDuePatron()
# b.search("harry potter")
# b.listAlltheBook()
b.add("the cheat sheet","sarah adams","ROMANTIC",10)
b.add("Harry potter","j.k. Rowling","Romantic",10)
b.add("she is with me","jessica cunsolo","romantic",20)
b.add("it ends with us ","colleen hoover","romantic",12)
b.listAlltheBook()
b.searchbyBooktype("romantic")
