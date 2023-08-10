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
#        Location Distribution of Genomic Islands in the Genome - Protein Families           #
##############################################################################################

from collections import Counter
#################
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
PFs=[]; PFs_List=[]; PF_S=[]; PF_E=[]; seen=[]
with open('New_GIsANDtheirProteins_New_5.txt', 'r') as f: # New_GIsANDtheirProteins_New_5.txt GIs.txt
  for line in f:
     A=line.split(None, 1)[0]
     if '$' not in A:
         G=A;
     else: 
         PFs.append(A.split('$')[1])            
         if A.split('$')[1] not in seen:
            PFs_List.append(A.split('$')[1]); seen.append(A.split('$')[1])              
         Genome_IDX=Genome.index(G.split('_B_')[0])
         Genome_Size=int(size[Genome_IDX])                 
         Temp=A.split('$')[0]; S=Temp.rfind('_(');   M=Temp.rfind('..');  E=Temp.rfind(')_')
         PF_S.append(round(float(Temp[S+2:M])/Genome_Size,5));   PF_E.append(round(float(Temp[M+2:E])/Genome_Size,5))
###################################
##Count the occurrence in each part
GIs_Distribution=open('PFs_GIs_Distribution_New_5.txt', 'w')
for n in range(10,11):
    P=[]; a=1/n; sum=0
    for i in range (0,n):
        sum+=a
        P.append(round(sum,1)) 
    PFs_List_IDX=-1          
    for i in PFs_List:
        Parts_list=[]; PFs_List_IDX=PFs_List_IDX+1
        print(PFs_List_IDX)
        for PL in range(0,n):
            Parts_list.append([]);      
        PFs_IDX=-1
        for k in PFs:
          PFs_IDX=PFs_IDX+1
          if k == i:
            Start=PF_S[PFs_IDX];  End=PF_E[PFs_IDX];   Prev_j= 0;  P_index=-1
            for j in P:
                P_index+=1;             
                if Prev_j<Start<=j: 
                  if Prev_j<End<=j:  
                     Parts_list[P_index].append(i)          
                  else:
                     if j-Start>0:
                        Parts_list[P_index].append(i)        
                                      
                     #check the End; could be exists in more than one section
                     for k in range (P_index,len(P)-1):
                           if  P[k]<End<=P[k+1]:
                               Parts_list[k+1].append(i)                                   
                               break
                           else:
                               Parts_list[k+1].append(i)                         
                Prev_j=j         
        GIs_Distribution.write(i+' ')                         
        for z in Parts_list:
            GIs_Distribution.write(str(len(z))+' ')            
        GIs_Distribution.write('\n') 
              