import os 
import numpy as np
import sys


number_of_speaker=0
no_of_files=0

'''
with open("/home/kaldi_asr/kaldi/egs/voxceleb/v2/data/train/wav.scp","w+") as fof,open("/home/kaldi_asr/kaldi/egs/voxceleb/v2/data/train/utt2spk","w+") as fof2:
    for x in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data"):
        #if len(x) > 5:
            #if ".py" not in x:
                #number_of_speaker+=1
                #if number_of_speaker <= 350:
        ln=[]
        for y in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x):
            for z in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x+"/"+y):
                ln.append((z,y))
        print(x,len(ln))
        for xp in np.array(ln):
            fof.write(x+"_"+xp[0].replace(".wav","")+" "+"/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x+"/"+xp[1]+"/"+xp[0]+"\n")
            fof2.write(x+"_"+xp[0].replace(".wav","")+" "+x+"\n")

'''
print(len(sys.argv))
print(sys.argv[0],sys.argv[1],sys.argv[2])
data_dir=sys.argv[1]
with open(sys.argv[2]+"/spk2utt","w+") as fof3:
    for x in os.listdir(data_dir):
        ln=[]
        for y in os.listdir(data_dir+"/"+x):
            
        #if len(x) > 5:
            #if ".py" not in x :
                #number_of_speaker+=1
                #if number_of_speaker <= 350:
            print(x,y)
            for z in os.listdir(data_dir+"/"+x+"/"+y):
                ln.append(z)
        print(len(ln))
        lns=[]
        for k in np.array(ln):
            lns.append(x+"_"+k.replace(".wav",""))
        st=" ".join(lns)
        fof3.write(x+" "+st+"\n")
print(number_of_speaker)


