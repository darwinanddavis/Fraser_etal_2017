# Read in BioCons_final.csv (subset row 'C1' of Biological_Conservation.csv) and separate author from affiliation. Output = 'BioCons3.csv'

# import reg exp, interation, and csv functions
import re
import itertools 
import csv

# create empty lists
authls = list()
affills = list()

# ------- opening files
f = file("BioCons_final.csv", "rU")

#----------- cycle through each row in csv
for row in f:
    # sub semicolon for colon for first 50 characters
    first = re.sub(';',',',row[:65])
    # paste new string to old string
    f = ''.join([first, row[66:]])
    # strip the white space
    row = f.rstrip()
    # # separate entries by semi colon
    entry = f.split(';')
    # for each entry
    for e in entry:
    #separate author from affil
        name = e.split(']')
    #   # select author
        author = name[0]
        # # remove ' [ ' and ' " ' characters.
        author = author.replace('"', "")
        author = author.replace("[", "")
        # #remove white space
        author = author.strip()
        # # select affil. Note: removes co-authors from same institution
        if e != name[0]:
            affil = name
            affil = affil[1]
            affil = affil.replace('"', "")
        # #remove white space
            affil = affil.strip()
            # populate lists with author and affil
            authls.append(author)
            affills.append(affil)

#print authls
#print affills

# open and write to BioCons_.csv
with open('BioCons_7.csv', 'w') as csvfile:
    authwriter = csv.writer(csvfile, delimiter=',')
    # transpose elements in author and affil lists to turn into columns, rather than rows
    for val in itertools.izip(authls, affills):
        authwriter.writerow(val)
