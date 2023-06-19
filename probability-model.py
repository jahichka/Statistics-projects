import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

#izolujemo samo kolone koje su nam potrebne za analizu
analysed_columns=["absences", "G3"]
data=pd.read_csv("student-mat.csv",usecols=analysed_columns)

#trazimo najcescu vrijednost izostanaka i prazna polja ispunjavamo sa njom
counted_elements=Counter(data["absences"])
most_common_element=counted_elements.most_common(1)[0][0]
data["absences"].fillna(most_common_element, inplace=True)

#racunamo prosjecnu vrijednost i devijaciju izostanaka
mean_absences=data["absences"].mean()
std_dev_absences=data["absences"].std()
var_absences= data["absences"].var()
print("Srednja vrijednost broja izostanaka studenata prije filtriranja podataka: ")
print(mean_absences)
print("Varijansa broja izostanaka studenata prije filtriranja podataka: ")
print(var_absences)
print("Standardna devijacija broja izostanaka studenata prije filtriranja podataka: ")
print(std_dev_absences)

#trazimo interval od jedne standardne devijacije i iskljucujemo iz analize rezultate koji nisu u tom intervalu
lower_bound=mean_absences-std_dev_absences
upper_bound=mean_absences+std_dev_absences
filtered_data=data[(data["absences"]<=upper_bound)&(data["absences"]>=lower_bound)]

points=filtered_data["G3"].max()*0.8
grade_10=np.where(filtered_data.loc[:,'G3']>=points,1,0)
excessive_absence=np.where(filtered_data.loc[:,'absences']>=10,1,0)
counter=grade_10*excessive_absence

l=len(filtered_data);

#vjerovatnoca da je student dobio 10
P_A=np.count_nonzero(grade_10)/float(l)

#vjerovatnoca da je student izostao vise od 10 predavanja
P_B=np.count_nonzero(excessive_absence)/float(l)

#vjerovatnoca da je student dobio 10 i izostao vise od 10 predavanja
P_AB=np.count_nonzero(counter)/float(l)

#vjerovatnoca da je student dobio 10 ako je izostao vise od 10 predavanja
P_A_B=P_AB/float(P_B)

#prosjek i standardna devijacija
average=filtered_data["absences"].mean()
std=filtered_data["absences"].std()
var=filtered_data["absences"].var()

print("Vjerovatnoća da student dobije ocjenu 10: ")
print(P_A)
print("Vjerovatnoća da je student izostao sa 10 ili vise predavanja: ")
print(P_B)
print("Vjerovatnoća da student dobije ocjenu 10 i da je izostao sa 10 ili više predavanja: ")
print(P_AB)
print("Vjerovatnoća da student dobije ocjenu 10 ako je izostao sa 10 ili više predavanja: ")
print(P_A_B)
print("Srednja vrijednost broja izostanaka studenata: ")
print(average)
print("Varijansa broja izostanaka studenata: ")
print(var)
print("Standardna devijacija broja izostanaka studenata: ")
print(std)

plt.subplot(2,1,1)
plt.hist(filtered_data["absences"],bins=10)
plt.xlabel('Izostanci')
plt.ylabel('Broj studenata')
plt.title("Broj izostanaka studenata")
plt.grid()
plt.subplot(2,1,2)
plt.hist(filtered_data["G3"],bins=21)
plt.xlabel('Ocjene')
plt.xticks(range(21))
plt.ylabel('Broj studenata')
plt.title("Broj bodova studenata")
plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.show()