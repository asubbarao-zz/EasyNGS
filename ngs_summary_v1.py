import csv
import numpy as np
import re
        
        
        
def get_design_np(fname):
    csvfile=open(fname, "r")
    design = csv.reader(csvfile, delimiter=",")
    rows = list(design)
    csvfile.close()
    design_data = np.array([rows[0]], dtype = 'a5000')
    for row in rows[1:]:
        design_data = np.vstack((design_data, np.array(row, dtype='a1000')))
    return design_data  
    
design_data = get_design_np('design_file_small.csv')
refseq = design_data[1:,3]
ID = design_data[1:,0]
Name = design_data[1:,1]
Row = design_data[1:,4]
Column = design_data[1:,5]
Feature_number = design_data[1:,6]
Mapping_quality_designs = design_data[1:,9]
Chromosome_Coordinates_designs = design_data[1:,10]

def get_sam_np(fname):  # function name and filename argument
    csvfile=open(fname,  "r") # opens the file named in fname
    sam = csv.reader(csvfile, delimiter=",") # csv.reader reads 
                                          # in a csv type file
    rows = list(sam)      # create a list of the rows that are read in
    csvfile.close()       # close the file we don't need it anymore
    
    sam_data=np.array([rows[0]], dtype='a1000') # create a 2D array starting with first row
    for row in rows[1:]:      # create numpy array of each subsequent row 
                              # except the first row
        sam_data = np.vstack((sam_data, np.array(row, dtype='a500')))

    return sam_data # return the list of rows
    
sam_data = get_sam_np('sam_small.csv')
chromosome = sam_data[1:,2]
position = sam_data[1:,3]
read_seq = sam_data[1:,9]
chromosome_coordinates = np.array(np.transpose((chromosome[:], position[:])))
CIGAR = sam_data[1:,5]

index = 0
for each in CIGAR[index]:
    present_cigar = CIGAR[index]
    indels = re.findall('(\d+[ID])', present_cigar)
    for num1, i_or_d in indels :
        print 'Number of indels:' , num1, i_or_d 
        print indels.span()
    index += 1



def get_mpileup_np(fname):
    csvfile = open(fname, 'r')
    mpileup = csv.reader(csvfile, delimiter=",")
    rows = list(mpileup)
    csvfile.close()
    
    mpileup_data = np.array([rows[0]], dtype = 'a1000')
    for row in rows[1:]:
        mpileup_data = np.vstack((mpileup_data, np.array(row, dtype = 'a500')))    
    return mpileup_data
    
mpileup_data = get_mpileup_np('mpileup_small.csv')
depth = mpileup_data[1:,3]
rbase = mpileup_data[1:,4]

#Calculate Indels for the file
indelcount = 0
for indels in rbase:
    if "-" in indels:
        indelcount += 1
    elif "+" in rbase:
        indelcount += 1
print "indelcount = ",indelcount

#Calculate SNPs for the file
countofnucleotides = 0
snpcount = 0
substitutioncount = 0
bases = ["A", "C", "T", "G", "a", "c", "t", "g"]
for nucleotide in bases:
    if nucleotide in rbase:
        countofnucleotides += 1 
        if countofnucleotides == 1:
            snpcount += 1
        else:
            substitutioncount += 1
print "substitutioncount = ",substitutioncount
print "snpcount = ",snpcount
             
#Extract the mapped reads present in the design file and the sequencing output file(reads)
mapped_reads = []        
for seq in refseq:
    for read in read_seq:
        if seq == read:
            mapped_reads.append(read)
print mapped_reads

#Compute the coverage of each sequence
haploidgenome_length = float(3*(10**9))##in basepairs;for human genome
read_length = 65
index = 0
for each in read_seq:
    print "depth per base = ",depth[index]
    index += 1
    
#write the data to a csv file    
data = [[ID, Name, refseq, Chromosome_Coordinates_designs, Mapping_quality_designs, read_seq, chromosome_coordinates ,Row, Column, Feature_number, indelcount, snpcount, substitutioncount, depth]]
length = len(data[0])
with open('ngs_summary_output.csv', 'w') as test_file:
    csvwriter = csv.writer(test_file)
    for y in range(length):
        csvwriter.writerow([x[y] for x in data])
 
    
