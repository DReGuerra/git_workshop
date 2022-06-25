
# Andre Guerra
# June, 2022
# andre.guerra@mail.mcgill.ca

# This is a python script 
# You can make modifications and practice making commits and pushing to the reporsitory

from matplotlib import markers
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# ==============================================================
# Functions
def fit_exp(x,A,t,b):
    return A*np.exp(-t*x)+b
# initial guess
p0 = [1000, 0.1, 50]

# ==============================================================
# data initialization
temp = np.arange(0,100) + 273.15 # K
concn = np.logspace(1,0,100)/10 # mol fraction
# generate normal dist'd noise
noise = np.random.normal(0,0.05,concn.shape) 
# add noise to the concentration
concn = concn + noise
# fit an exponential to the data
params, cv = opt.curve_fit(fit_exp,temp,concn,p0)
A, t, b = params
# Coefficient of determination
diffSqrd = np.square(concn - fit_exp(temp,A,t,b))
diffSqrd_mean = np.square(concn - np.mean(concn))
R2 = 1 - np.sum(diffSqrd)/np.sum(diffSqrd_mean)

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
axs.plot(temp,concn,marker='o',
         markeredgewidth=1.5,
         linestyle='none',
         label='data')
axs.plot(temp,fit_exp(temp,A,t,b),
         label='fit: $c=Aexp(-t*T)+b$')
axs.set_title("Reagent concentration")
axs.set_xlabel("Temperature, K")
axs.set_ylabel("Concentration, mol fraction")
axs.annotate("R$^2$ = " + str(np.around(R2,decimals=3)),
             xy=(0.5,0.7),xycoords='axes fraction',
             fontsize=TEXTFONT)
axs.legend(loc=(0.5,0.8))
f.savefig("4_figures/reagent_concentration.png",bbox_inches='tight')