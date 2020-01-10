import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns



tsne_data=np.load("tsne_data.npy")[1:]
tsne_trans_data=tsne_data[:,:127]
tsne_label=tsne_data[:,127]
ab,cd=np.unique(tsne_label,return_counts=True)
sd={n:m for n,m in zip(ab,cd) if m > 200}
print(len(sd))
cm = ["lightcoral","sienna","tan","gold","olive","lawngreen","darkgreen","turquoise","darkslategrey","teal","deepskyblue","dodgerblue","navy","slateblue","indigo","violet","magenta"]

X_embed=TSNE(n_components=2).fit_transform(tsne_trans_data)

print(X_embed.shape)

sns.set_style("dark") #Seaborn style dark

fig, axss=plt.subplots(figsize=(8,8), constrained_layout=True)
arr_list=list(sd.keys())

for x,y in zip(X_embed,tsne_label):
    if y in sd :
        axss.scatter(x[0],x[1],color=cm[arr_list.index(y)],marker=".")


axss.grid()
axss.set(title="TSNE Plot For The Speakers Who Have Greater Than 200 Utterances 15 Speakers hence 15 clusters")

plt.tight_layout()
plt.plot()
plt.show()
