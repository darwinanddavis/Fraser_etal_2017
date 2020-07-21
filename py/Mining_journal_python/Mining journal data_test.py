fh = "[Jackson, Andrew L.] Univ Dublin Trinity Coll, Sch Nat Sci, Dept Zool, Dublin 2, Ireland; [Author 1] Uni Melb; [Author 2] Uni Bristol"

# import reg exp, interation, and csv functions
import re
import itertools 
import csv
# import numpy as N

# create empty lists
authls = list()
affills = list() 
countls = list()
countedls = list()

# strip the white space
line = fh.rstrip()
# separate names by semi colon
names = line.split(';')
for entry in names:
    # separate author from affil
    name = entry.split(']')
    # select author
    author = name[0]
    # split into words
    # # remove ' [ ' and ' " ' characters.
    author = author.replace('"', "")
    author = author.replace("[", "")
    author = author.split()
    # remove all characters associated with a '.'
    author = [x for x in author if not '.' in x]
    # select affil
    affil = name[1]
    #remove white space
    affil = affil.strip()
    # remove commas
    affil = re.sub(',',' ', affil)
    # remove initials from author names
    countls.append(len(author))
             # select affil. Note: removes co-authors from same institution
    #affil = affil.split()
    authls.append(author)
    affills.append(affil)


def is_odd(num):
   return num % 2 != 0 

for c in countls:
    is_odd(c)
    # print c

evens = range(0, 100, 2)

#----- Option 2 for quantifying len() of list
class slist(list):
    @property
    def length(self):
        return len(self)

l = slist(countls)
countlss = l.length
# print type(l)


# print authls
# print affills

# open and write to BioCons csv
with open('BioCons_test.csv', 'w') as csvfile:
    authwriter = csv.writer(csvfile, delimiter=',')
    # transpose elements in author and affil lists to turn into columns, rather than rows
    for val in itertools.izip(authls, affills, countls):
        authwriter.writerow(val)



