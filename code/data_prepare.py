import os 
import numpy as np



number_of_speaker=0
no_of_files=0



# To Create 3 important files WAV.scp utt2spk and spk2utt
'''


with open("/home/kaldi_asr/kaldi/egs/voxceleb/v2/data/train/wav.scp","w+") as fof,open("/home/kaldi_asr/kaldi/egs/voxceleb/v2/data/train/utt2spk","w+") as fof2:
    #Iterate through all the files in the directory
    for x in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data"):
        #if len(x) > 5: 
            #if ".py" not in x:
                #number_of_speaker+=1
                #if number_of_speaker <= 350:
        ln=[] #For Every Speaker We create this empty list to store name of all the wav files
        #Iterate Through all the sub dirs in the main speaker folder
        
        for y in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x):
            
            #Iterate Through all the ".wav" files in the sub dirs
            
            for z in os.listdir("/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x+"/"+y):
                ln.append((z,y))
                
        print(x,len(ln)) #Printing Number of utterance per speaker 
        
        # Write the information of all the utterance "wav files" in the requested format 
        
        for xp in np.array(ln):
        
            fof.write(x+"_"+xp[0].replace(".wav","")+" "+"/home/kaldi_asr/kaldi/egs/voxforge/s5/voxforge/big_data/"+x+"/"+xp[1]+"/"+xp[0]+"\n")
            fof2.write(x+"_"+xp[0].replace(".wav","")+" "+x+"\n")

'''

#Same thing is as above but for the file "spk2utt"


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
        for k in np.array(ln):
            lns.append(x+"_"+k.replace(".wav",""))
        st=" ".join(lns)
        fof3.write(x+" "+st+"\n")
print(number_of_speaker)


