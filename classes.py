import csv
import numpy as np
import re
import pandas as pd        
from pandas import *

def get_csvfile_data(fname, given_dtype, delim):
    """API usage: fname is string, given_dtype is data type passed to
    np.assarray, delim is the delimiter to read csv file"""
    raw = pd.read_csv(fname, delim)
    ret = np.asarray(raw.values, given_dtype)
    return ret
    
class design_np:
    def __init__(self):
        self.refseq = None
        self.ID = None
        self.Name = None
        self.Row = None
        self.Column = None
        self.Feature_number = None
        self.Mapping_quality_designs = None
        self.Chromosome_Coordinates_designs = None
    
    def populate_design_np(self,fname, given_dtype, delim):
        design_data = get_csvfile_data(fname, given_dtype, delim)
        df_design = DataFrame(design_data)
        self.refseq = list(design_data[3])
        self.ID = list(design_data[0])
        self.Name = list(design_data[1])
        self.Row = list(design_data[4])
        self.Column = list(design_data[5])
        self.Feature_number = list(df_design[6])
        self.Mapping_quality_designs = list(df_design[9])
        self.Chromosome_Coordinates_designs = list(df_design[10])
        
class sam_np:
    def __init__(self):
        self.chromosome = None
        self.position = None
        self.read_seq = None
        self.chromosome_coordinates = None
        self.CIGAR = None
        self.cigar_total_info = None
        
    def populate_sam_np(self, fname, given_dtype, delim):
        sam_data = get_csvfile_data(fname, given_dtype, delim)
        df_sam = DataFrame(sam_data)
        self.chromosome = list(df_sam[2])
        self.position = list(df_sam[3])
        self.read_seq = list(df_sam[9])
        self.chromosome_coordinates = list(DataFrame(np.array(np.transpose((self.chromosome[:], self.position[:])))))
        self.CIGAR = list(df_sam[5])
        
    def set_cigar_total_indel_info(self, cigar_total_info, num_insertions, num_deletions):
        self.cigar_total_info = cigar_total_info
        self.num_insertions = num_insertions
        self.num_deletions = num_deletions
        
class mpile_up:
    def __init__(self):
        self.rbase = None
        self.symbols = None
        self.depth = None
        
    def populate_mpile_up(self, fname, given_dtype, delim):
        mpileup_data = get_csvfile_data(fname, given_dtype, delim)
        df_mpileup = DataFrame(mpileup_data)
        self.rbase = list(df_mpileup[2])
        self.symbols = list(df_mpileup[4])
        self.depth = list(df_mpileup[3])