#NAME OF THE FILE: EasyNGS_with_UI_v3.py
#BY: Kiranmayee Dhavala, Alok Subbarao, Renu Jayakrishnan, Harjot Hans
#DATE SUBMITTED: 12/17/2014
#Python Version(s): 2.7.4

""" This module finds and calculated the number of insertions and deletions on the
gene sequence using an important function, 'hasindel'. Once identified, it calculates
the number of Insertions and deletions, substitutions and writes the desired output
to a csv file. The doctest module checks if the critical function, 'hasindel', works
as expected. The modules required are re, pandas, wx, EasyNGS_with_UI_v3_With_Comments 
and sys.

Author: Alok Subbarao
MODIFICATION HISTORY: 12/2/2014
DESCRIPTION: Updated the part of the code that analyzes the SAM file
to calculate insertions and deletions. 


"""

import re
import pandas as pd
import wx     
import EasyNGS_GUI_v3 as engs
reload(engs)   
import sys
import EasyNGS_results_module_v2_1 as res

app = wx.App()
lb = engs.ListBox(None, -1, 'EasyNGS')
design = lb.design
sam = lb.sam
mpileup = lb.mpileup
app.MainLoop()

## If unsuitable file name is given, the code will not proceed further. It will
## display error message and exit. 
if design.num_elements == 0 :
    print 'Insufficient data'
    sys.exit(1)
elif sam.num_elements == 0:
    print 'In sufficient data'
    sys.exit(1)
elif mpileup.num_elements == 0:
    print 'Insufficient data'
    sys.exit(1)
"""
Modifcation history:
    Date: 12/13/14
    Description: fixing the file read input
                Once the file reader was changed.
    
    Date: 12/13/14
    Author: Jeff Byrnes
    Written By Alok Subbarao
    Description: Transposes the output, previously each row was output as
        a column

    Date: 12/16/14
    Author:Renu Jayakrishnan
    Edit: Documentation and adding Autotest module. 

    
    
"""

indels = 0 # insertions or deletions.

def hasindel(element, regex=re.compile('\d+[ID]')):
    """
    Description: searches a string for any digit followed by "I" or "D" to 
    determine whether the string contains indels or deletions. Default argument
    is a regular expression. In this case, set to I/D. 
    
    Postconditions: Returns either 'true' or 'false'
    
    Side effects: global variable "indels" used but no possible effect on the rest of the code
    
    Return: True if an indel is present, otherwise false.
    >>> hasindel('ABCDEI')
    True
    >>> hasindel('32M1D32M')
    True
    >>> hasindel('D6M1D56M1I')
    True
    >>> hasindel('32456789')
    False
    >>> hasindel(1989)
    Traceback (most recent call last):
        ...
        TypeError: expected string or buffer 
     """
    global indels
    indels = regex 
    if regex.search(element): #this will return true if it is found otherwise none
         return True
    else:
         return False

index = 0 #initialize global variable "indels"
indel_loc =[] #contains index of indels in CIGAR
indel_span = [] #the span of the indels within CIGAR[index]
indel_type = [] #list of strings containing the actual indel
total_indel_info=[] #metalist of the above 3 lists

for index in enumerate(sam.CIGAR): 
    if hasindel(index[1]): 
        indel_loc.append(index[0]) #if the item has an indel, append the  location 
        
for x in indel_loc:
    present_cigar =  indels.finditer(sam.CIGAR[x]) #create iterator, use regex to store the span and group
    for y in present_cigar:
        indel_span.append(y.span())
        indel_type.append(y.group())
        
for q in range(len(indel_loc)):
    total_indel_info.insert(q,((indel_loc[q], indel_type[q], indel_span[q]))) #merge the created lists into one list



"""
End of edit from ngs_summary_jeff by A.Subbarao 12/2/2014
"""

    
#write the data to a csv file    
data = [[design.ID, design.Name, design.refseq, design.Chromosome_Coordinates_designs, design.Mapping_quality_designs, sam.read_seq, sam.chromosome_coordinates ,design.Row, design.Column, design.Feature_number, mpileup.depth]]

out = pd.DataFrame(data[0][0:10])
fin = out.transpose()

fin.to_csv('output_data.csv') #writes the data given above to "output_data" in csv format in the working directory

if __name__ == "__main__":
    import doctest
    doctest.testmod()
