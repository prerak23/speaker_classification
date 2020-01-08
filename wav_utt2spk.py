import os 
import numpy as np
import sys


number_of_speaker=0
no_of_files=0

data_dir=sys.argv[1]

with open(sys.argv[2]+"/wav.scp","w+") as fof,open(sys.argv[2]+"/utt2spk","w+") as fof2:
    for x in os.listdir(data_dir):
        #if len(x) > 5:
            #if ".py" not in x:
                #number_of_speaker+=1
                #if number_of_speaker <= 350:
        ln=[]
        for y in os.listdir(data_dir+"/"+x):
            for z in os.listdir(data_dir+"/"+x+"/"+y):
                ln.append((z,y))
        print(x,len(ln))
        for xp in np.array(ln):
            fof.write(x+"_"+xp[0].replace(".wav","")+" "+data_dir+"/"+x+"/"+xp[1]+"/"+xp[0]+"\n")
            fof2.write(x+"_"+xp[0].replace(".wav","")+" "+x+"\n")


