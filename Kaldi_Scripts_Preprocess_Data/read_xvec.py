from kaldiio import ReadHelper
import numpy as np
m=0
nsp=np.array([])
abss=[]
with ReadHelper('scp:spk_xvector.scp') as reader:
    for key, ab in reader:
        if m == 0:
            nsp=np.array(ab).reshape(1,-1)
        else:
            nsp=np.vstack((nsp,ab.reshape(1,-1)))
        m+=1
print(nsp.shape)
np.save("spk_vector_bigd.npy",nsp)
