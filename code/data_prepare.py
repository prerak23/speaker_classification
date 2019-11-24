import os 
import numpy as np



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
                ln.append(z)
        print(x,len(ln))
        for xp in np.sort(np.array(ln)):
            fof.write(x+"_"+xp.replace(".wav","")+" "+"/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x+"/"+y+"/"+xp+"\n")
            fof2.write(x+"_"+xp.replace(".wav","")+" "+x+"\n")

'''
with open("/home/kaldi_asr/kaldi/egs/voxceleb/v2/data/train/spk2utt","w+") as fof3:
    for x in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data"):
        ln=[]
        for y in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x):
            
        #if len(x) > 5:
            #if ".py" not in x :
                #number_of_speaker+=1
                #if number_of_speaker <= 350:
            print(x,y)
            for z in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x+"/"+y):
                ln.append(z)
        print(len(ln))
        lns=[]
        for k in np.sort(np.array(ln)):
            lns.append(x+"_"+k.replace(".wav",""))
        st=" ".join(lns)
        fof3.write(x+" "+st+"\n")
print(number_of_speaker)


