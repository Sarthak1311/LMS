from src.LibManSys.Patron import Patron
import datetime
a =Patron()
# a.add("pulkit tyagi","harry potter",datetime.datetime.now().strftime('%Y-%m-%d'))
# a.patronInfo("sarthak tyagi")
# a.add("puks","harry potter","2024-8-1")
# a.getOverDuePatron()
a.bookreturned("puks","harry potter")
a.getOverDuePatron()