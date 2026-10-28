import numpy as np
import matplotlib.pyplot as plt
# --- Arevalo Rafael NC:0031 ---
No_Lista=[1,2,3,17,48]
Califa_ML=[20,30,80,100,90]
Califa_VA=[70,90,60,90,100]
plt.plot(No_Lista, Califa_ML,label="Califa_ML")
plt.plot(No_Lista, Califa_VA,label="Califa_VA")
plt.title(" Calificaciones Materias 0031")
plt.xlabel("Numero de listas")
plt.ylabel("Calificacion")
plt.legend()
plt.show()