import numpy as np
from sklearn.model_selection import train_test_split


speaker_arr=list(np.load("speaker_arr.npy",allow_pickle=True)) #Labels Load
speaker_arr_unique=dict(np.load("speaker_unique.npy",allow_pickle=True)[()]) #Labels Encoded In Dict
vectors=np.load("x_vector_bigd.npy") #Xvector Loaded
speaker_id_arr=[speaker_arr_unique[x] for x in speaker_arr] #Labels encoded to dict

print(speaker_id_arr)
print(vectors.shape,len(speaker_id_arr))

X_train_val, X_test, y_train_val, y_test = train_test_split(vectors, np.array(speaker_id_arr), test_size=0.15, random_state=42)
X_train, X_val ,y_train,y_val=train_test_split(X_train_val,y_train_val,test_size=0.15,random_state=42)

#a,b=np.unique(np.array(speaker_id_arr),return_counts=True)
#print(dict(zip(a,b)))
c,d=np.unique(y_train,return_counts=True)

print(len(dict(zip(c,d))))


print(X_train.shape,y_train.shape,X_test.shape,y_test.shape,X_val.shape,y_val.shape)


np.save("training_data.npy",np.hstack((X_train,y_train.reshape(-1,1))))
np.save("val_data.npy",np.hstack((X_val,y_val.reshape(-1,1))))
np.save("test_data.npy",np.hstack((X_test,y_test.reshape(-1,1))))
