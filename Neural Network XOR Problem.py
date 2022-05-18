import numpy as np
import matplotlib.pyplot as plt
import random

print("   ")
i1 = np.array([0,0,1,1])
i2 = np.array([0,1,0,1])
istenilen_cikis = np.array([0,1,1,0])  
n = 0.5
iterasyon = 3000
b1 = random.random()            
b2 = random.random()                 
w1 = random.random()            
w2 = random.random() 
w3 = random.random()           
w4 = random.random()    
w5 = random.random()           
w6 = random.random() 
  
Etotal_list=[]
outo1_list=[]

def sigmoid(z):
    z= 1 / (1 + np.exp(-z))
    return z

def ileri_yayilim(w1,w2,w3,w4,b1,i1,i2):
    neth1 = w1 * i1 + w2 * i2 + b1
    neth2 = w3 * i1 + w4 * i2 + b1
    outh1 = sigmoid(neth1)    
    outh2 = sigmoid(neth2) 
    neto1 = w5 * outh1 + w6 * outh2 + b2 * 1
    outo1 = sigmoid(neto1)
    return neth1,neth2,outh1,outo1

def geri_yayilim(outo1,istenilen_cikis,outh1):
    Etotal_outo1 = outo1 - istenilen_cikis 
    outo1_neto1 = outo1 * (1 - outo1)
    neto1_w5 = outh1
    neto1_w6 = sigmoid(neth2)
    Etotal_outh1 = (Etotal_outo1 * outo1_neto1)*w5
    Etotal_outh2 = (Etotal_outo1 / sigmoid(neth2))*w6
    outh1_neth1 = outh1 * (1 - outh1)
    outh2_neth2 = sigmoid(neth2) * (1 - sigmoid(neth2))
    neth1_w1 = i1
    neth1_w2 = i2

    Etotal_w1 = Etotal_outh1 * outh1_neth1 * neth1_w1
    Etotal_w2 = Etotal_outh1 * outh1_neth1 * neth1_w2
    Etotal_w3 = Etotal_outh2 * outh2_neth2 * neth1_w1
    Etotal_w4 = Etotal_outh2 * outh2_neth2 * neth1_w2
    Etotal_w5 = Etotal_outo1 * outo1_neto1 * neto1_w5
    Etotal_w6 = Etotal_outo1 * outo1_neto1 * neto1_w6
    return Etotal_w1,Etotal_w2,Etotal_w3,Etotal_w4,Etotal_w5,Etotal_w6

for i in range(iterasyon):
    neth1,neth2,outh1,outo1 = ileri_yayilim(w1,w2,w3,w4,b1,i1,i2)
    Etotal = ((istenilen_cikis-outo1 ) ** 2) / 2
    Etotal_list.append(Etotal)
    Etotal_w1,Etotal_w2,Etotal_w3,Etotal_w4,Etotal_w5,Etotal_w6 = geri_yayilim(outo1,istenilen_cikis,outh1)
    w1 = w1 - (n * Etotal_w1)
    w2 = w2 - (n * Etotal_w2)
    w3 = w3 - (n * Etotal_w3)
    w4 = w4 - (n * Etotal_w4)
    w5 = w5 - (n * Etotal_w5)
    w6 = w6 - (n * Etotal_w6)
    outo1_list.append(outo1)
    if((Etotal < 0.00060).any()):
        break

print("Cikis: ", outo1)

plt.figure(figsize=(20,10))
plt.subplot(2,2,1)   
plt.plot(Etotal_list)
plt.xlabel("İterasyon Sayısı")
plt.ylabel("Eğitim")

plt.subplot(2,2,2)   
plt.plot(outo1_list)
plt.xlabel("İterasyon Sayısı")
plt.ylabel("Çıkış")
plt.show()
