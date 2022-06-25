
# Andre Guerra
# June, 2022
# andre.guerra@mail.mcgill.ca

# This is a python script 
# You can make modifications and practice making commits and pushing to the reporsitory

import numpy as np
import matplotlib.pyplot as plt

# ==============================================================
# data initialization
temp = np.arange(0,100) + 273.15 # K
conc = np.logspace(1,0,100)/10 # mol fraction
# generate normal dist'd noise
noise = np.random.normal(0,0.05,conc.shape) 
# add noise to the concentration
conc = conc + noise

# ==============================================================
# Visualization
# sizing factors
TICKSFONT = 13
TITLEFONT = 15
TEXTFONT = 15
FIGWIDTH = 6.4
FIGHEIGHT = 4.8
LINEWIDTH = 3
ROLLWINDOW = 100

# ==============================================================
# Concentration
NROWS = 1
NCOLS = 1
f, axs = plt.subplots(nrows=NROWS,ncols=NCOLS,
                      figsize=(NCOLS*FIGWIDTH,NROWS*FIGHEIGHT))
axs.plot(temp,conc)
axs.set_title("Reagent concentration")
axs.set_xlabel("Temperature, K")
axs.set_ylabel("Concentration, mol fraction")
f.savefig("4_figures/reagent_concentration.png",bbox_inches='tight')