##############################################################################################
# Copyright and terms of use (DO NOT REMOVE):
# The code is made freely available for non-commercial uses only, provided that the copyright 
# header in each file not be removed, and suitable citation(s) (see below) be made for papers 
# published based on the code.
#
# The copyright of the code is retained by the authors.  By downloading/using this code you
# agree to all the terms stated above.
#
#   Dr. Reem Aldaihani, Prof. Lenwood S. Heath 
#   "Investigating the Nature of Genomic Island Locations within a Genome" 
#   Department of Computer Science, Virginia Tech.
#   Blacksburg, VA, 2023. 
#
# Copyright (c) 2023, Reem Aldaihani All rights reserved.
##############################################################################################

##############################################################################################
#             Genomic Islands location in Relation to the Origin of Replication              #
#  The most frequent species in the data set in relation to the origin of replication        #
#                                    (circular genomes)                                      #
##############################################################################################

#Get GIs that belongs to the following species: 
#Escherichia_coli  Salmonella_enterica   Klebsiella_pneumoniae  Bordetella_pertussis  Pseudomonas_aeruginosa
Name=[]; ID=[]
with open('Species_AccN_New_3.txt', 'r') as f:  #Genomes_Size.txt GZ.txt
  for line in f:
     Name.append(line.split(None, 1)[0]); ID.append(line.split(None, 2)[1])

Top_Species=['Escherichia_coli$',  'Salmonella_enterica$',   'Klebsiella_pneumoniae$',  'Bordetella_pertussis$',  'Pseudomonas_aeruginosa$']

Genome=[]; size=[]; Structure=[]
with open('Genome_Size_Structure_New_5.txt', 'r') as f:  #Genome_Size_Structure_New_5.txt GSZ.txt
  for line in f:
     Genome.append(line.split(None, 1)[0]);  size.append(line.split(None, 3)[2]); Structure.append(line.split(None, 4)[3])
          
for i in  Top_Species:    
    Histogram_OOR_Normalization_Circular=open(i+'Histogram_OOR_Normalization_Circular_New_5.txt', 'w')
    Histogram_OOR_Normalization_Linear=open(i+'Histogram_OOR_Normalization_Linear_New_5.txt', 'w') 
    Circular_Genomes_oric_Middle=open(i+'_OOR_oric_Middle_Values.txt','w')
    oriC =0;  Middle=0
    Histogram_OOR_Normalization_Circular.write('[');  Histogram_OOR_Normalization_Linear.write('[')
    
    with open('Overlap_GIs_New_5.txt', 'r') as f: # Overlap_GIs_New_5.txt OG.txt
       for line in f:           
         G=(line.split(None, 1)[0]).split('_B_')[0]
         G_Name=Name[ID.index(G)]
         Genome_IDX=Genome.index(G)
         Genome_Structure=Structure[Genome_IDX]
         Genome_Size=int(size[Genome.index(G)])
         New_Start=round((int(line.split(None, 2)[1])/Genome_Size),5)                  
         
         if G_Name+'$' == i:          
           
            if Genome_Structure == 'circular':
               Histogram_OOR_Normalization_Circular.write(str(New_Start)+' ')    
               if 0.25<New_Start<=0.75: Middle=Middle+1
               else:   oriC=oriC+1
                              
            elif Genome_Structure == 'linear':
               Histogram_OOR_Normalization_Linear.write(str(New_Start)+' ')
                 
    Circular_Genomes_oric_Middle.write('oriC= '+str(oriC)+'\n'+'Middle of the genome= '+str(Middle)+'\n') 
    Histogram_OOR_Normalization_Circular.write(']'); Histogram_OOR_Normalization_Linear.write(']'); 
    Histogram_OOR_Normalization_Circular.close();    Histogram_OOR_Normalization_Linear.close()






