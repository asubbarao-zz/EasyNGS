import csv
import numpy as np
import re
import pandas as pd        
from pandas import *
import time
import classes

start_time = time.time()        

design_np_inst = classes.design_np()
design_np_inst.populate_design_np('design_file_small.csv', 'a1000', ',')
   
sam_data_inst = classes.sam_np()
sam_data_inst.populate_sam_np('sam_small.csv','a5000', ',')

index = 0
indels = re.compile('\d+[ID]')

def hasindel(element):
    """
    Description: searches a string for any digit followed by "I" or "D" to 
    determine whether the string contains indels or deletions
    
    Postconditions: Returns either 'true' or 'false'
    
    Side effects: none
    
    Return: True if an indel is present, otherwise false
     """
    if indels.search(element): #this will return true if it is found otherwise none
         return True
    else:
         return False

index = 0
indel_loc =[] #contains index of indels in CIGAR
indel_span = [] #the span of the indels within CIGAR[index]
indel_type = [] #list of strings containing the actual indel
total_indel_info=[] #metalist of the above 3 lists

for index in enumerate(sam_data_inst.CIGAR): 
    if hasindel(index[1]): 
        indel_loc.append(index[0]) #if the item has an indel, append the  location 
        
for x in indel_loc:
    present_cigar =  indels.finditer(sam_data_inst.CIGAR[x]) #create iterator, use regex to store the span and group
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
        
"""
End of edit from ngs_summary_jeff by A.Subbarao 12/2/2014
"""
    
sam_data_inst.set_cigar_total_indel_info(total_indel_info, insertions, deletions)

mpile_up_inst = classes.mpile_up()
mpile_up_inst.populate_mpile_up('mpileup_small.csv','a5000',',')

#Calculate Indels for the file
indelcount = 0
for indels in mpile_up_inst.symbols:
    if "-" in indels:
        indelcount += 1
    elif "+" in mpile_up_inst.symbols:
        indelcount += 1
print "indelcount = ",indelcount

#Calculate SNPs for the file
'''Question: countofnucleotides inside the forloop is always going to be 1? 
So how is it counting SNPS? '''
countofnucleotides = 0
snpcount = 0
substitutioncount = 0
bases = ["A", "C", "T", "G", "a", "c", "t", "g"]
for nucleotide in bases:
    if nucleotide in mpile_up_inst.rbase:
        countofnucleotides += 1 
        if countofnucleotides == 1:
            snpcount += 1
        else:
            substitutioncount += 1
print "substitutioncount = ",substitutioncount
print "snpcount = ",snpcount
             
#Extract the mapped reads present in the design file and the sequencing output file(reads)
mapped_reads = []        
for seq in design_np_inst.refseq:
    for read in sam_data_inst.read_seq:
        if seq == read:
            mapped_reads.append(read)
print mapped_reads

#Compute the coverage of each sequence
haploidgenome_length = float(3*(10**9))##in basepairs;for human genome
read_length = 65
index = 0
for each in sam_data_inst.read_seq:
    print "depth per base = ",mpile_up_inst.depth[index]
    index += 1
    
#write the data to a csv file    
    
#temp = [ID, Name, refseq, Chromosome_Coordinates_designs, Mapping_quality_designs, read_seq, chromosome_coordinates ,Row, Column, Feature_number, indelcount, snpcount, substitutioncount, depth]
#out = DataFrame(np.asarray(temp))
#out.to_csv("out.csv",sep = "\t")
"""To find the total run time of the program """
end_time = time.time()
print "Time elapsed in seconds ",(end_time - start_time)
 
    