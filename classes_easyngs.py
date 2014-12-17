import pandas as pd
import numpy as np

    
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
    
    def populate_design_np(self, df_design):
        self.refseq = df_design['Payload'].tolist()
        self.ID = df_design['ID'].tolist()
        self.Name = df_design['name'].tolist()
        self.Row = df_design['row'].tolist()
        self.Column = df_design['col'].tolist()
        self.Feature_number = df_design['number'].tolist()
        self.Mapping_quality_designs = df_design['Mapping_Quality'].tolist()
        self.Chromosome_Coordinates_designs = df_design['MappingProbeName'].tolist()
        
    def __iter__ (self):
        self.iter_count = 0
        return self
    
    def __next__ (self):
        if self.iter_count < self.num_elements:
            result = None
            result.append(self.refseq(self.iter_count))
            result.append(self.ID(self.iter_count))
            result.append(self.Name(self.iter_count))
            result.append(self.Row(self.iter_count))
            result.append(self.Column(self.iter_count))
            result.append(self.Feature_number(self.iter_count))
            result.append(self.Mapping_quality_designs(self.iter_count))
            result.append(self.Chromosome_Coordinates_designs(self.iter_count))
            self.iter_count += 1
            return result
            
    def __getitem__(self,i):
        new_list_design = []
        new_list_design.append(self.refseq(i))
        new_list_design.append(self.ID(i))
        new_list_design.append(self.Name(i))
        new_list_design.append(self.Row(i))
        new_list_design.append(self.Column(i))
        new_list_design.append(self.Feature_number(i))
        new_list_design.append(self.Mapping_quality_designs(i))
        new_list_design.append(self.Chromosome_Coordinates_designs(i))
        return new_list_design

class sam_np:
    def __init__(self):
        self.chromosome = None
        self.position = None
        self.read_seq = None
        self.chromosome_coordinates = None
        self.CIGAR = None
        self.cigar_total_info = None
        
    def populate_sam_np(self, df_sam):
        self.chromosome = df_sam['Ref_Seq_Name'].tolist()
        self.position = df_sam['Position'].tolist()
        self.read_seq = df_sam['Seq'].tolist()
        self.chromosome_coordinates = list(pd.DataFrame(np.array(np.transpose((self.chromosome[:], self.position[:])))))
        self.CIGAR = df_sam['CIGAR'].tolist()
        self.num_elements = len(self.chromosome)
        
    def set_cigar_total_indel_info(self, cigar_total_info, num_insertions, num_deletions):
        self.cigar_total_info = cigar_total_info
        self.num_insertions = num_insertions
        self.num_deletions = num_deletions
    
    def __iter__ (self):
        self.iter_count = 0
        return self
    
    def __next__ (self):
        if self.iter_count < self.num_elements:
            result = None
            result.append(self.chromosome(self.iter_count))
            result.append(self.position(self.iter_count))
            result.append(self.red_seq(self.iter_count))
            result.append(self.chromosome_coordinates(self.iter_count))
            result.append(self.CIGAR(self.iter_count))
            self.iter_count += 1
            return result
        else:
            return None
    
    def __getitem__(self,index):
        new_list_sam = []
        new_list_sam.append(self.chromosome(index))
        new_list_sam.append(self.position(index))
        new_list_sam.append(self.red_seq(index))
        new_list_sam.append(self.chromosome_coordinates(index))
        new_list_sam.append(self.CIGAR(index))
        return new_list_sam

class mpile_up:
    def __init__(self):
        self.rbase = None
        self.symbols = None
        self.depth = None
        
    def populate_mpile_up(self, df_mpileup):
        self.rbase = df_mpileup['RBASE'].tolist()
        self.symbols = df_mpileup['READ_BASES'].tolist()
        self.depth = df_mpileup['DEPTH'].tolist()
        self.num_elements = len(self.symbols)
    
    def __iter__ (self):
        self.iter_count = 0
        return self
        
    def __next__ (self):
        if self.iter_count < self.num_elements:
            result = None
            result.append(self.rbase(self.iter_count))
            result.append(self.symbols(self.iter_count))
            result.append(self.depth(self.iter_count))
            self.iter_count += 1
            return result
            
    def __getitem__(self,i):
        new_list_mpile_up = []
        new_list_mpile_up.append(self.rbase(i))
        new_list_mpile_up.append(self.symbols(i))
        new_list_mpile_up.append(self.depth(i))
        return new_list_mpile_up 