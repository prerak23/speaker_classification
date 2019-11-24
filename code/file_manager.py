import os
import numpy as np
import pandas as pd
import re
import random
import subprocess
from operator import itemgetter
dic={}
cn=0
for x in os.listdir(os.getcwd()):
    if os.path.exists(os.getcwd()+"/"+x+"/"+"wav"):
        xn=x.split("-")
        if not bool(re.search("[0-9_]+",xn[0])):
            if xn[0] not in dic:
                dic[xn[0]]=len(os.listdir(os.getcwd()+"/"+x+"/"+"wav"))
            else:
                dic[xn[0]]=len(os.listdir(os.getcwd()+"/"+x+"/"+"wav"))+dic[xn[0]]
    cn+=1

print(sorted(dic.items(),key=itemgetter(1)))
#os.mkdir(os.getcwd()+"/"+"/big_data/"+dic.keys()[0])
llp={}
'''
for x in os.listdir(os.getcwd()):
    if os.path.exists(os.getcwd()+"/"+x+"/"+"wav"):
        xn=x.split("-")
        if not bool(re.search("[0-9_]+",xn[0])):
            if dic[xn[0]] > 30 and dic[xn[0]] < 2000 :
                if xn[0] not in llp:
                    llp[xn[0]]=[]
                    os.mkdir(os.getcwd()+"/"+"/big_data/"+xn[0])
                    os.mkdir(os.getcwd()+"/"+"/big_data/"+xn[0]+"/"+x)
                    xni=0
                    for y in os.listdir(os.getcwd()+"/"+x+"/"+"wav"):
                        subprocess.call(["cp","-r",os.getcwd()+"/"+x+"/"+"wav/"+y,os.getcwd()+"/"+"big_data/"+xn[0]+"/"+x])
                        xni+=1
                    llp[xn[0]].append((xni,x))
                else:
                    xni=0
                    os.mkdir(os.getcwd()+"/"+"/big_data/"+xn[0]+"/"+x)
                    for y in os.listdir(os.getcwd()+"/"+x+"/"+"wav"):
                        subprocess.call(["cp","-r",os.getcwd()+"/"+x+"/"+"wav/"+y,os.getcwd()+"/"+"big_data/"+xn[0]+"/"+x])
                        xni+=1
                    llp[xn[0]].append((xni,x))

print("=======================================================")
print(llp)
'''


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
