################################################
# attempt to read CSV files
################################################

# system
import csv
# This program adds up integers in the command line
import sys

# my subroutines
import sub2

####################
# RelativeKeys
####################
# Relative Id [uniq]
# Relative Name    [superfluous, but could do checking]
# Key
# Source


def read_relative_keys (relative_keys) :

    f = open(relative_keys, 'r')
    line1=f.readline()
    print ('line1' ,line1)

    # should check line1 is as expected
    # Relative Id, Relative Name,Key,Source

    print('x2')
    lines=0
    
    with f as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            lines = lines + 1
            
            if (lines == 1) :
                print ('line 1', row)
                
            #print ('line ', lines, ' ', row)
            #print ()
            #print (lines) 
            #if (lines > 35895 ) :
            # break
            #print (row)
            
    print('x3')
    print(lines)
    print ('last line', row)

################################
# main routine
################################
print ("Hello again World")

relative_keys = sys.argv[1]

print ('infile = ', relative_keys)

#relative_keys = 'C:\\Users\\Mary\\Documents\\Python\\DNA program\\files\\RelativeKeys.csv'

read_relative_keys(relative_keys)

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
