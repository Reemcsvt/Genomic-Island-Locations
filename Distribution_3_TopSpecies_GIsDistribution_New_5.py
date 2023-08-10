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
#                   Location Distribution of Genomic Islands in the Genome                   #
#  The most frequent species in the data set in relation to the origin of replication        #
#                                    (circular genomes)                                      #
##############################################################################################

from collections import Counter
#################
Name=[]; ID=[]
with open('Species_AccN_New_3.txt', 'r') as f:  
  for line in f:
     Name.append(line.split(None, 1)[0]); ID.append(line.split(None, 2)[1])
 
Top_Species=['Escherichia_coli$',  'Salmonella_enterica$',   'Klebsiella_pneumoniae$',  'Bordetella_pertussis$',  'Pseudomonas_aeruginosa$']   
##################   
#Get the GIs
Genome=[]; size=[]; Structure=[]
with open('Genome_Size_Structure_New_5.txt', 'r') as f:  #Genome_Size_Structure_New_5.txt GSZ.txt
  for line in f:
     Genome.append(line.split(None, 1)[0])
     size.append(line.split(None, 3)[2])
     Structure.append(line.split(None, 4)[3])
##################
GIs=[]; S=[]; E=[]
with open('Overlap_GIs_New_5.txt', 'r') as f: # Overlap_GIs_New_5.txt OG.txt
   for line in f:       
     GIs.append(line.split(None, 1)[0]); S.append(int(line.split(None, 2)[1])); E.append(int(line.split(None, 3)[2]))
###################################
#Count the occurrence in each part
GIs_Distribution_Circular=open('TopSpecies_GIsDistribution_Circular_New_5.txt', 'w')
GIs_Distribution_Linear=open('TopSpecies_GIsDistribution_Linear_New_5.txt', 'w')
for T in Top_Species:
    for n in range(10,11):
        P=[]; a=1/n; sum=0
        for i in range (0,n):
            sum+=a
            P.append(round(sum,1))
        index=-1;   Parts_list_Circular=[];  Parts_list_Linear=[]; 
        for PL in range(0,n):
            Parts_list_Circular.append([]);    Parts_list_Linear.append([]); 
                
        for i in GIs:
            index+=1
            G_Name=Name[ID.index(i.split('_B_')[0])]
            if  G_Name+'$'==T:        
                Genome_IDX=Genome.index(i.split('_B_')[0])
                Genome_Size=int(size[Genome_IDX])
                Genome_Structure=Structure[Genome_IDX]                       
                Start=S[index]/Genome_Size; End=E[index]/Genome_Size
                Length=abs(End-Start);      Prev_j= 0;  P_index=-1
                for j in P:
                    P_index+=1;             
                    if Prev_j<Start<=j: 
                      if Prev_j<End<=j:  
                         if   Genome_Structure == 'circular':  Parts_list_Circular[P_index].append(i)   
                         elif Genome_Structure == 'linear':    Parts_list_Linear[P_index].append(i)       
                      else:
                         if j-Start>0:
                            if   Genome_Structure == 'circular':  Parts_list_Circular[P_index].append(i)   
                            elif Genome_Structure == 'linear':    Parts_list_Linear[P_index].append(i)       
                                          
                         #check the End; could be exists in more than one section
                         for k in range (P_index,len(P)-1):
                               if  P[k]<End<=P[k+1]:
                                   if   Genome_Structure == 'circular':  Parts_list_Circular[k+1].append(i)   
                                   elif Genome_Structure == 'linear':    Parts_list_Linear[k+1].append(i)                                  
                                   break
                               else:
                                   if   Genome_Structure == 'circular':  Parts_list_Circular[k+1].append(i)   
                                   elif Genome_Structure == 'linear':    Parts_list_Linear[k+1].append(i)                       
                    Prev_j=j 
                
      
        GIs_Distribution_Circular.write(T+'\n'); GIs_Distribution_Linear.write(T+'\n')      
        for i in Parts_list_Circular:
            GIs_Distribution_Circular.write(str(len(i))+', ')            
        GIs_Distribution_Circular.write('\n') 
        
        for i in Parts_list_Linear:
            GIs_Distribution_Linear.write(str(len(i))+', ')            
        GIs_Distribution_Linear.write('\n')      

             