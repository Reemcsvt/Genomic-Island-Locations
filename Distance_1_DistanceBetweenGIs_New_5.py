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
#                   The Nature of the Distances between the Genomic Islands                  #
#                               All of the GIs in the data set                               #
##############################################################################################

Genome=[]; size=[]; Structure=[]
with open('Genome_Size_Structure_New_5.txt', 'r') as f:  #Genome_Size_Structure_New_5.txt GSZ.txt
  for line in f:
     Genome.append(line.split(None, 1)[0]); size.append(line.split(None, 3)[2]); Structure.append(line.split(None, 4)[3])

Dataset=[]; seen=[]
with open('Overlap_GIs_New_5.txt', 'r') as f: # Overlap_GIs_New_5.txt OG.txt
   for line in f:       
     G=(line.split(None, 1)[0]).split('_B_')[0]
     if G+'$' not in seen:
        Dataset.append(G); seen.append(G+'$')
          
Distance_GIs_Circular=open('Distance_GIs_Circular.txt', 'w'); Distance_GIs_Linear=open('Distance_GIs_Linear.txt', 'w')

GIs=list(); S_Cr=list(); E_Cr=list(); Distances=list()
for Dataset_Genome in Dataset:
    Genome_Structure=Structure[Genome.index(Dataset_Genome)]
    Genome_Size=int(size[Genome.index(Dataset_Genome)])
    visit=0; count=0; Distance=-1
    with open('Overlap_GIs_New_5.txt', 'r') as f: # Overlap_GIs_New_5.txt OG.txt
       for line in f:       
         G=(line.split(None, 1)[0]).split('_B_')[0]
         if G==Dataset_Genome:
             visit=1     
             GI = (line.split(None, 1)[0]).split('_B_')[1]; S = int(line.split(None, 2)[1]); E = int(line.split(None, 3)[2])
             GIs.append(GI); S_Cr.append(S); E_Cr.append(E); count=count+1
         elif visit ==1:  break                 
    
    if visit ==1:  #Compute the distances  
     if count>1:   
        if Genome_Structure == 'circular':                 
           for i in range (0,count):             
               if i== (count-1):    Distance=round(abs(  (S_Cr[0]/Genome_Size) +  (1-(E_Cr[i]/Genome_Size))  ),5)         
               else:                Distance=round(abs(  (S_Cr[i+1]-E_Cr[i])/Genome_Size  ),5)
               Distance_GIs_Circular.write(str(Distance)+'\n')   
           
        elif  Genome_Structure == 'linear':  
              for i in range (0,count-1):
                  Distance=round(abs(  (S_Cr[i+1]-E_Cr[i])/Genome_Size  ),5)              
                  Distance_GIs_Linear.write(str(Distance)+'\n')                                    
     GIs.clear(); S_Cr.clear(); E_Cr.clear()


