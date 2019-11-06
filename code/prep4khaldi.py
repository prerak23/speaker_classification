import os
import numpy as np
path="D:\\MSc_NLP\\software_project\\code\\script_python\\xvector_data\\train_data"
speaker_folder_list=[]
ns=0
for spk_elt in os.listdir(path): #loop over the speaker folder
    if ".py" not in spk_elt: #here if skip the file with the extension '.py'
        if ns < 450:
            wav_array=[]
            ns +=1
            for item in os.listdir(path+"\\"+spk_elt+"\\"+"wav"):#loop over wav folder of each speaker
                wav_array.append(item) #append item which is the utterance of each speaker to the wav_array list
            spk_utt_array=[]
            for xp in np.sort(np.array(wav_array)):
                spk_utt_array.append(spk_elt+"_"+xp.replace(".wav", ""))
                #with open("spk2utt.txt", 'a') as spk2utt:
                    #print(spk_elt+" "+xp.replace(".wav","")+"_"+spk_elt, file=spk2utt)
                    #print(spk_elt+" " + " ".join(spk_utt_array), file=spk2utt)

                """ write the output (print) result of the utterrance to speaker, utt2spk, into a text file
                    The text file name is utt2spk.txt
                    The structure of this file is <utterance-id> <speaker-id>
                """
                with open("utt2spk.txt", 'a') as utt2spk:
                    print(spk_elt+"_"+xp.replace(".wav","") + " " + spk_elt, file=utt2spk)

                """ write the output(print) result of the utterrance,wav, into a text file
                    The file is wav.scp
                    The structure of this file is <speaker-id>_<utterance-id> <directory path>
                """
                with open("wav.scp", 'a') as wav_file:
                    print(spk_elt+"_"+xp.replace(".wav","") +" "+path+"\\"+spk_elt+"\\"+"wav"+"\\"+xp, file=wav_file)

                #print("wav.scp: " +spk_elt+"_"+xp.replace(".wav","") +" "+path+"\\"+spk_elt+"\\"+"wav"+"\\"+xp)
                #print("spk2utt: "+spk_elt+" "+xp.replace(".wav",""), file=spk2utt)
                #print("utt2spk: " + xp.replace(".wav","") + " " + spk_elt)
            """ write the output (print) result of speaker to utterrance, spk2utt, into a text file.
                The text file name is spk2utt.txt
                The structure of this file is <speaker-id> <utterance-id>
            """
            with open("spk2utt.txt", 'a') as spk2utt:
                print(spk_elt+" " + " ".join(spk_utt_array), file=spk2utt)
print(ns)
