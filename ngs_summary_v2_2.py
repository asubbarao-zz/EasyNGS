
import re
import pandas as pd
import wx     
import EasyNGS_with_UI_v3_With_Comments as engs   


app = wx.App()
lb = engs.ListBox(None, -1, 'EasyNGS')
design = lb.design
sam = lb.sam
mpileup = lb.mpileup
app.MainLoop()
        
"""
Modifcation history - 12/13/14
Description: fixing the file read input
Once the file reader was changed from 
    
    
"""


"""
Author: Alok Subbarao
MODIFICATION HISTORY: 12/2/2014
DESCRIPTION: Updated the part of the code that analyzes the SAM file
to calculate insertions and deletions. Prior function below.

index = 0
for each in CIGAR[index]:
    present_cigar = CIGAR[index]
    indels = re.findall('(\d+[ID])', present_cigar)
    for num1, i_or_d in indels :
        print 'Number of indels:' , num1, i_or_d 
        print indels.span()
    index += 1
    
    
    
"""
indels = 0

def hasindel(element, regex=re.compile('\d+[ID]')):
    """
    Description: searches a string for any digit followed by "I" or "D" to 
    determine whether the string contains indels or deletions
    
    Postconditions: Returns either 'true' or 'false'
    
    Side effects: none
    
    Return: True if an indel is present, otherwise false
     """
    global indels
    indels = regex 
    if regex.search(element): #this will return true if it is found otherwise none
         return True
    else:
         return False

index = 0
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


insertions = 0
deletions = 0
for i_or_d in indel_type:
    if i_or_d[1] == "I":
        insertions += int(i_or_d[0])
    elif i_or_d[1] == "D":
        deletions += int(i_or_d[0]) 
        #calculates number of specific indels and deletionos
        
sam.set_cigar_total_indel_info(total_indel_info, insertions, deletions)
print "Num insertions ",insertions
print "Num deletions ", deletions

"""
End of edit from ngs_summary_jeff by A.Subbarao 12/2/2014
"""

#####deletions just returns the length of indel_type (doesn't seem to differentiate between I or D). 
#I think indexing of loop is incorrect        


#Calculate Indels for the file
indelcount = 0
for indels in mpileup.symbols:
    if "-" in indels:
        indelcount += 1
    elif "+" in mpileup.symbols:
        indelcount += 1
print "Count of Insertions/Deletions = ",indelcount

#Calculate SNPs for the file
countofnucleotides = 0
snpcount = 0
substitutioncount = 0


##count the number of A,C,T,G,a,c,t,g present in rbase
acount = 0
ccount = 0
tcount = 0
gcount = 0
bases = ["A", "C", "T", "G", "a", "c", "t", "g"]
for nucleotide in mpileup.rbase:
    if nucleotide.lower() == 'a':
        acount += 1 
    elif nucleotide.lower() == 'c':
        ccount += 1
    elif nucleotide.lower() == 't':
        tcount +=1
    elif nucleotide.lower() == 'g':
        gcount +=1

print "Substitution count: "
print "'a' count = {:d}, 'c' count {:d}, 't' count {:d}, 'g' count {:d}".format(acount, ccount, tcount, gcount)

#####Looking at rbase we should see much larger numbers (all of them seem to be in bases), additionally we should expect count of nucleotides to be the same length as bases (that is: have a count per base)#
#####snpcount will only be 1 if countofnecleotides is >= 1 and 0 otherwise (takes on no other values) (not sure if this in intentional)

             
#####Mapped_reads is missing some matches. I can't make sense of it logically, however when implementing my own version I found additional matches (which I verified)

#Compute the coverage of each sequence
haploidgenome_length = float(3*(10**9))##in basepairs;for human genome
read_length = 65
index = 0
#for each in sam.read_seq:
#    print "depth per base = ",mpileup.depth[index]
#    index += 1
    
#write the data to a csv file    
"""
Modification History: 12/13/14
Author: Jeff Byrnes
Written By Alok Subbarao
Description: Transposes the output, previously each row was output as
a column
"""
data = [[design.ID, design.Name, design.refseq, design.Chromosome_Coordinates_designs, design.Mapping_quality_designs, sam.read_seq, sam.chromosome_coordinates ,design.Row, design.Column, design.Feature_number, mpileup.depth]]

out = pd.DataFrame(data[0][0:10])
fin = out.transpose()

fin.to_csv('output_data.csv') ##instead of outputting the data I would use a key to how the data was subsetted