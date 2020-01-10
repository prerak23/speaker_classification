import os
import numpy as np

abs=[]
speaker_unique={}
with open("xvector.scp","r") as fof:
    for x in fof:
        abc=x.split(" ")
        print(abc)
        abs.append(abc[0].split("_")[0])
        if abc[0].split("_")[0] not in speaker_unique:
            speaker_unique[abc[0].split("_")[0]]=len(speaker_unique)

print(len(abs))
print(abs)
print(speaker_unique)
print(len(speaker_unique))
np.save("speaker_arr.npy",np.array(abs),allow_pickle=True)
np.save("speaker_unique.npy",np.array(speaker_unique),allow_pickle=True)
