import os
import numpy as np
import pandas as pd
import re
import random
import subprocess
from operator import itemgetter
dic={}
cn=0

# Iterate thorugh all the files in the downloaded dataset from voxforge 

for x in os.listdir(os.getcwd()):
    if os.path.exists(os.getcwd()+"/"+x+"/"+"wav"): #Check that this folder contains wav file or not 
        xn=x.split("-") #Split the name
        if not bool(re.search("[0-9_]+",xn[0])): #Check that the Name is a proper name or not and should not contain any numbers or special char's
            #Create a dictionary which calculate how many utterances are present for each author
            if xn[0] not in dic:
                dic[xn[0]]=len(os.listdir(os.getcwd()+"/"+x+"/"+"wav"))
            else:
                dic[xn[0]]=len(os.listdir(os.getcwd()+"/"+x+"/"+"wav"))+dic[xn[0]]
    cn+=1

print(sorted(dic.items(),key=itemgetter(1)))

#os.mkdir(os.getcwd()+"/"+"/big_data/"+dic.keys()[0])
llp={}


#Iterate through the files

for x in os.listdir(os.getcwd()):
    if os.path.exists(os.getcwd()+"/"+x+"/"+"wav"): #Check if the file contain ".wav" file or not
        xn=x.split("-") 
        if not bool(re.search("[0-9_]+",xn[0])): #Check if the name contain any special char's or Nubmers
            if dic[xn[0]] > 30 and dic[xn[0]] < 2000 : #Check the author name in the dictonary created above to check how many utterances are there are there per author it should be in the range of 30 to 2000 
                if xn[0] not in llp: #This to check if the author folder is already present in the directory if not then here it create first the author folder and then the subfolder
                    llp[xn[0]]=[]
                    os.mkdir(os.getcwd()+"/"+"/big_data/"+xn[0]) #Create Folder name with author first name 
                    os.mkdir(os.getcwd()+"/"+"/big_data/"+xn[0]+"/"+x) #Create Sub Folder Name 
                    xni=0
                    #Copy every utterance file into subfolder which is on top of the main folder which is named by author first name
                    for y in os.listdir(os.getcwd()+"/"+x+"/"+"wav"):
                        subprocess.call(["cp","-r",os.getcwd()+"/"+x+"/"+"wav/"+y,os.getcwd()+"/"+"big_data/"+xn[0]+"/"+x])
                        xni+=1
                    llp[xn[0]].append((xni,x))
                else: #The Author folder is already present then just need to copy the utterance by creating a subfolder and the copying the utterances 
                    xni=0
                    os.mkdir(os.getcwd()+"/"+"/big_data/"+xn[0]+"/"+x)
                    for y in os.listdir(os.getcwd()+"/"+x+"/"+"wav"):
                        subprocess.call(["cp","-r",os.getcwd()+"/"+x+"/"+"wav/"+y,os.getcwd()+"/"+"big_data/"+xn[0]+"/"+x])
                        xni+=1
                    llp[xn[0]].append((xni,x))

print("=======================================================")
print(llp)


#print(len(dic),cn)
#print(dic)
#nns=random.sample(dic.keys(),500)
#print(nns)
#print("-----------------------")

#dic={xl:0 for xl in nns}
'''
total_file_len=0
ex=0
for xl in nns:

        print(xl,len(os.listdir(os.getcwd()+"/"+dic[xl][0]+"/"+"wav")))
        total_file_len=total_file_len+len(os.listdir(os.getcwd()+"/"+dic[xl][0]+"/"+"wav"))
        subprocess.call(["cp","-r",os.getcwd()+"/"+dic[xl][0],"/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/train_data"])
        ex+=1
            
         
print(total_file_len,ex)
'''
