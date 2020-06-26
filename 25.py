import re
date = input("write the date in this format yyyy-mm-dd ")
def F(dat):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1', dat)
print(F(date))