import torch.nn as nn
import torch
import numpy as np

import torch.optim as optim




def check(predicted_label,actual_label,number):

    if torch.argmax(predicted_label).item() == actual_label.item():
        number=number+1
    return number


arr_tsne=np.random.rand(1,128)



class classify(nn.Module):

    def __init__(self,n_classes,vec_size):
        super().__init__()
        self.n_class=n_classes
        self.conv1d=nn.Conv1d(1,1,3,stride=2)
        self.relu=nn.ReLU()
        self.maxpool=nn.MaxPool1d(3,stride=2)
        self.linear_1=nn.Linear(127,127)
        self.linear=nn.Linear(127,self.n_class)

    def forward(self,x,labels,epo):

        ip=torch.unsqueeze(x,1)

        op=self.relu(self.conv1d(ip))

        op=self.maxpool(op)

        op=self.linear_1(op)

        if "train_lst" in epo:
           global arr_tsne
           tt=torch.squeeze(op,1).detach().numpy()
           tt=np.hstack((tt,torch.unsqueeze(torch.tensor(labels),1)))
           print(tt.shape)
           arr_tsne=np.vstack((arr_tsne,tt))

        ops=self.linear(self.relu(op))

        return torch.squeeze(ops,1)





model=classify(169,100)


load_train_data=np.load("training_data.npy")
load_val_data=np.load("val_data.npy")
load_test_data=np.load("test_data.npy")
print(load_train_data.shape)
print(load_val_data.shape)

load_train_labels=load_train_data[:,512]
load_train_data=load_train_data[:,:511]
load_val_labels=load_val_data[:,512]
load_val_data=load_val_data[:,:511]
test_data=load_test_data[:,:511]
test_labels=load_test_data[:,512]


print(load_train_data.shape,load_train_labels.shape,test_data.shape,test_labels.shape)
epoch=0
lsp=0.02
losss_func=optim.SGD(model.parameters(), lr=lsp)
epoch_arr=[]

val_loss_avg_arr=[]
corr_pred_val=[]

def validation(data,labels):
    val_loss_avg=0
    count_val=0
    correct_pred=0
    for x in np.arange(0, data.shape[0], 1):
        forward_val_data = data[x, :].reshape(1, -1)
        forward_val_label = torch.tensor(np.array([labels[x]])).long()

        output = model(torch.tensor(forward_val_data, dtype=torch.float, requires_grad=True),forward_val_label,"Val")

        loss_func = nn.CrossEntropyLoss()

        loss_val = loss_func(output, forward_val_label)
        val_loss_avg=loss_val.item()+val_loss_avg
        count_val+=1
        correct_pred = check(output, forward_val_label, correct_pred)

    val_loss_avg_arr.append((val_loss_avg/count_val))
    corr_pred_val.append((correct_pred/count_val)*100)
    print(correct_pred)



def test(test_data,test_labels):
    val_loss_avg=0
    count_val=0
    correct_pred_test=0
    for x in np.arange(0, test_data.shape[0], 1):
        forward_test_data = test_data[x, :].reshape(1, -1)
        forward_test_label = torch.tensor(np.array([test_labels[x]])).long()

        output = model(torch.tensor(forward_test_data, dtype=torch.float, requires_grad=True),forward_test_label,"Test")
        #loss_func = nn.CrossEntropyLoss()
        #loss_val = loss_func(output, forward_val_label)
        #val_loss_avg=loss_val.item()+val_loss_avg
        count_val+=1
        correct_pred_test = check(output, forward_test_label, correct_pred_test)
        #print(loss_val)

    #val_loss_avg_arr.append((val_loss_avg/count_val))
    return (correct_pred_test/count_val)*100





while epoch < 4:

    if epoch == 3:
        to_take_value="train_lst"
    else:
        to_take_value="train"
    loss_avg=0
    count=0
    for x in np.arange(0,load_train_data.shape[0],4):
        forward_pass_data=load_train_data[x:x+4,:]
        forward_pass_label=load_train_labels[x:x+4]
        losss_func.zero_grad()

        output=model(torch.tensor(forward_pass_data,dtype=torch.float,requires_grad=True),forward_pass_label,to_take_value)

        loss_func=nn.CrossEntropyLoss()
        loss=loss_func(output,torch.tensor(forward_pass_label).long())

        #print(loss)
        loss.backward()
        losss_func.step()
        loss_avg=loss.item()+loss_avg
        count+=1

    print("Epoch",epoch)
    epoch_arr.append((loss_avg/count))
    validation(load_val_data,load_val_labels)
    epoch+=1


print("On Test Data Set Accuracy",test(test_data,test_labels))
print(epoch_arr)
print(val_loss_avg_arr)
print(corr_pred_val)


np.save("train_epoch_arr.npy",np.array(epoch_arr))
np.save("val_epoch_arr.npy",np.array(val_loss_avg_arr))
np.save("corr_pred_val.npy",np.array(corr_pred_val))
np.save("tsne_data",np.array(arr_tsne))

#print(model)
#print(model(torch.randn(5,1,512)).shape)
