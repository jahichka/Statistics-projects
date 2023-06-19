import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import scipy.signal as sp

mean=0
std_dev=1
n=5000

awgn=random.normal(mean,std_dev,n)
awgnInverted=-1*awgn
hn=sp.firwin(numtaps=111,cutoff=0.3)
y=1/len(hn)*(np.convolve(awgn,hn,mode='same'))
plt.plot(y)
plt.show()

hn_kappa=(1/n)*np.convolve(y,awgnInverted,mode='same')
plt.plot(hn_kappa)
plt.show()
error=hn-hn_kappa
plt.plot(error)
plt.show()