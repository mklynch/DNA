################################################
# attempt to read CSV files
################################################

# system
import csv
import sys

# my subroutines (not currently used)
import sub2

####################
# RelativeKeys
####################
# Relative Id [uniq]
# Relative Name    [superfluous, but could do checking]
# Key
# Source


def read_relative_keys1 (relative_keys) :

    for row in csv.DictReader(open(relative_keys, 'r', errors="ignore")) :
        name=row['Relative Name']
        if 'whitelock' in name.lower():
            print(row)
            print(name)
            print()
    print('completed :)')

def read_relative_keys2 (relative_keys) :

    for row in csv.DictReader(open(relative_keys, 'r', errors="ignore")) :
        name=row['Relative Id']
        print(name)

################################
# 
################################
def count_segments(relative_keys,chromosome_browser) :

    for row in csv.DictReader(open(relative_keys, 'r', errors="ignore")) :
        name=row['Relative Id']
        numseg[name]=0
        RelativeName[name]=row['Relative Name']
        
    for row in csv.DictReader(open(chromosome_browser, 'r', errors="ignore")) :
        name=row['RelativeId']
        numseg[name] += 1
    
    # print any id's with more than 10 segments
    for num in numseg :
        if (numseg[num] > 5) :
            print (numseg[num], num, RelativeName[num])
            

        
################################
# main routine
################################

#relative_keys = 'C:\\Users\\Mary\\Documents\\Python\\DNA program\\files\\RelativeKeys.csv'
relative_keys = sys.argv[1]

#chromosome_browser = 'C:\\Users\\Mary\\Documents\\Python\\DNA program\\files\\ChromosomeBrowser.csv'
chromosome_browser = sys.argv[2]

print ('RelativeKeys = ', relative_keys)
print ('ChromosomeBrowser = ', chromosome_browser)

#read_relative_keys1(relative_keys)
#read_relative_keys2(relative_keys)

numseg=dict()           # indexed by RelativeId
RelativeName=dict()     # Relative Name


count_segments(relative_keys,chromosome_browser)

# read in files from GMPro

# read all existing files (or just ones I will need)
# read new files, merge and dedupe
# write out new versions






####################
# Triangulations
####################
# Relative1    [superfluous, but could do checking]
# RelativeId1
# Relative2    [superfluous, but could do checking]
# RelativeId2
# Source    [e.g. FTDNA, gedmatch]
# Chr
# Start_Point
# End_Point


####################
# Segments
####################
# Profile
# Group
# Generation
# Chr
# Start_Point
# End_Point
# Side
# Paternal_Ancestor
# Maternal_Ancestor
# Description

####################
# Relatives
####################
# Relative    [should only be here, and is only for info]
# RelativeId
# Sex
# Maternal_Haplogroup
# Paternal_Haplogroup
# Contact_Name
# Contact_Email
# Contact_Phone
# Status
# Status_Date
# Surname_List
# Ancestor_List
# Family_Locations
# MRCA_Note
# Research_Notes


####################
# ChromosomeBrowser
####################
# Profile        [e.g. Mary, Martin]
# Relative        [superfluous, but could do checking]
# RelativeId    [as defined elsewhere]
# Side            [P/M]
# Group            [p20K]
# Source        [FTDNA, combined, gedmatch, ...]
# Chr
# Start_Point
# End_Point
# cMs
# SNPs
# Maternal_MRCA
# Paternal_MRCA
# Notes            [I don't often make notes on segments]

