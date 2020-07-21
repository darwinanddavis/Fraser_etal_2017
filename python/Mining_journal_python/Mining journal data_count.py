# Read in BioCons_final.csv (subset row 'C1' of Biological_Conservation.csv) and separate author from affiliation. Output = 'BioCons3.csv'

# import reg exp, interation, and csv functions
import re
import itertools 
import csv
import collections

# create empty lists
authls = list()
affills = list()
countryls = list()
countls = list()

# ------- opening files
f = file("BioCons_final.csv", "rU")
fdict = dict()

#----------- use when cycling through rows
for row in f:
    # replace all semicolons occuring within square braces with identifier 
    row = re.sub("\[[^]]*\]", lambda x:x.group(0).replace(';','/'), row)
    # strip the white space
    row = row.rstrip()
    # # separate names by semi colon
    entry = row.split(';')
    for e in entry:
        #separate author from affil
        name = e.split(']')
        # select author
        author = name[0]
        # # remove ' [ ' and ' " ' characters.
        author = author.replace('"', "")
        author = author.replace("[", "")
        # split into individal names by identifier
        author = author.split("/")
        # separate authors into new rows
        author_new = "\n".join(a for a in author)
        # # select affil. 
        if e != name[0]:
            affil = name
            affil = affil[1]
            affil = affil.replace('"', "")
            # take last word in affil by separating by last space 
            country = affil.rsplit(' ', 1)[1]
        # #remove white space
            affil = affil.strip()
            # populate lists 
            authls.append(author_new)
            affills.append(affil)
            countryls.append(country)
            countls.append(len(author))



# open and write to BioCons_.csv
with open('BioCons_count.csv', 'w') as csvfile:
    authwriter = csv.writer(csvfile, delimiter=',')
    # transpose elements in author and affil lists to turn into columns, rather than rows
    for val in itertools.izip(authls, affills, countryls, countls):
        authwriter.writerow(val)
