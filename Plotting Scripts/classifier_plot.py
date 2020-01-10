import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

train_loss=np.load("train_epoch_arr.npy")
val_loss=np.load("val_epoch_arr.npy")
accuracy_val=np.load("corr_pred_val.npy")



sns.set_style("dark") #Seaborn style dark

fig, axs=plt.subplots(3, figsize=(8,8), constrained_layout=True)

train_data_list=[]
val_data_list=[]
percen_val=[]


counter=[]
count=1
for i in range(train_loss.shape[0]):
    count+=1
    train_data_list.append(train_loss[i])
    val_data_list.append(val_loss[i])
    percen_val.append(accuracy_val[i])
    counter.append(count)

plt.title("Data Set Of 6000 Lines")
axs[0].plot(counter,train_data_list)
axs[0].set(title="Loss On Training Data",xlabel="epochs")
axs[1].plot(counter,val_data_list)
axs[1].set(title="Loss On Validation Data",xlabel="epochs")

axs[2].set(title="Accuracy On Validation Data",xlabel="epochs")
axs[2].plot(counter,percen_val)
plt.tight_layout()
plt.plot()
plt.savefig("total_plot_complete_overfitting.png")

plt.show()