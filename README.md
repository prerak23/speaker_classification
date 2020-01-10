# **Speaker recognition**
This is a submission for a Natural Language Processing project
towards the fulfilment of the requirement for the Software project class
in Autumn 2019 at Institut des Sciences du Digital, Management et Cognition, Lorraine University.




## **Strucutre of the README**
* Abstract
* Structure of the repository
* Getting started
* Deployment
* Built with
* Contributing
* Authors
* License
* Acknowledgments

## **Abstract**
TODO

## **Structure of the repository**
*  README.md:
TODO

## **Getting Started*
TODO

### **Prerequisites**
TODO

## **Deployment**
The bash script "get_xvector.sh" says almost everything about this work basically if you run this file you will directly have the x-vectors per utterance given in the dataset
get_xvector.sh expects to params 
First Parameter :- Directory where your dataset is (Full Path)
Second Parameter :- Directory where you want to save the 3 imp files spk2utt,wav.scp and utt2spk

Imp Note :- For proper function of this shell script you have to have your dataset in below defined format 
For Example:- /home/kaldi/dataset "Should be your first parameters"
In this dataset folder there should be folders named by speaker names ["Speaker_Name1","Speaker_Name2","Speaker_Name3","Speaker_Name4"]
then for each "Speaker_Name1":["File_1","File_2","File_3"]
and then for each "File_1":["id_1.wav","id_2.wav","id_3.wav"] etc etc..

Another important thing to note about that this bash script file should be kept at topmost directory "topmost" here means it should be in the outermost directory of your kaldi recipe 
So, the file named as vector_extract.sh and this bash script and utils folder of the kaldi recipe you are using should be at the same level.

About "vector_extract.sh" in this bash file it takes these 3 imp file "wav.scp","utt2spk" and "spk2utt" from the folder "data/train" you can change it to the directory that you passed as an second argument here I will mention all those place in this bash script where you need to change the directory for the functioning of this important bash script as this is bash script which is used to extract x-vector from pre-trained model 
You can also find other comments in the file which you can change as per your need's like the output "x-vectors" in which directory you store them etc 






## **Built with**

* Kaldi  tool: https://github.com/kaldi-asr/kaldi; https://kaldi-asr.org/models/m7
* Deep Neural Network (DNN):
* PyTorch

## **Contributing**
For any contribution, please first discuss the change you wish to make 
with the owner of the repository before making a change.

## **Authors**
* Abrougui Rim
* Balard Srilakshmi
* Srivastava Prerak
* Yang Ruoxiao

## **License**
This project is licensed under the TODO

## **Acknowledgement**
* Hat tip to anyone whose code was used
* Inspiration
* etc

