import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Force matplotlib to use 'TkAgg' backend, which opens plots in a separate window
matplotlib.use('TkAgg')

# Data
categories = ['CC', 'PM', 'MRD', 'LU', 'EFW', 'POF', 'HTOX_nC', 'WU', 'FRD']
Cost_opti = [0.46,	0.83,	1.53,	7.13,	2.34,	0.06,	0.05,	0.04,	0.43]
LCA_opti = [0.03,	1.94,	6.45,	10.85,	6.37,	0.14,	0.22,	0.04,	0.41]
COST_opti_49 = [1.09,	0.98,	1.44,	7.35,	2.31,	0.06,	0.05,	0.03,	0.60]
LCA_opti_49 = [0.03,	1.75,	5.96,	9.10,	5.74,	0.12,	0.20,	0.04,	0.37]
MC1_opti_49 = [0.09,	0.85,	1.63,	9.27,	2.47,	0.05,	0.05,	0.06,	0.22]
MC2_opti_49 = [0.03,	0.63,	1.27,	4.11,	1.29,	0.03,	0.04,	0.01,	0.08]
cost_2020 = [2.421535377,	1.460508928,	0.91075466,	    5.484744364,	2.6865172,	    0.114687228,	0.047145717,	0.02716845,	    1.950636448]
cost_2025 = [1.831631920,   1.021820950,	0.864771684,	4.761280869,	1.787314276,	0.096489394,	0.040542806,	0.020529161,	1.051205345]
cost_2030 = [1.424602841,	0.847959216,	0.954506138,	5.18079213,	    1.541292438,	0.088097791,	0.037694325,	0.023262325,	0.946315422]
cost_2035 = [1.068451953,	0.823082941,	1.12189141,	    5.599352252,	1.849815539,	0.07553783,	    0.041758682,	0.021674245,	0.744018430]
cost_2040 = [0.737740631,	0.811287699,	1.297827726,	7.722210587,	1.956207606,	0.069540845,	0.044551561,	0.02091469,	    0.633183214]
cost_2045 = [0.513751097,	0.801896143,	1.477232363,	10.42142024,	2.283442078,	0.064601874,	0.049125467,	0.036460499,	0.542280723]
cost_2050 = [0.356150647,	0.832607972,	1.534768963,	11.89035457,	2.157397372,	0.061229204,	0.049855197,	0.026001249,	0.476965697]
MC_2045 = [0.50270701,	0.633050227,	1.239315798,	2.236299756,	1.521091526,	0.037694766,	0.038523772,	0.010804644,	0.296895798]
MC_2050 = [0.356150651,	0.698024982,	1.325844836,	5.092046672,	1.793372301,	0.042667992,	0.04201115,	0.013635959,	0.34650339]

#FEDECOM - COUNTRY SCALE#
BE_70_U = [1.780753256,	0.876966836,	0.890238528,	5.749107767,	1.89807061,	    0.092777568,	0.039997541,	0.020994677,	1.110034258]
BE_39_U = [0.992133953,	0.76424083,	1.088217126,	5.26744718,	1.834853936,	0.069307276,	0.03991706,	0.03588804,	0.627755646]
BE_8_U = [0.203514658,	0.719674044,	1.223153015,	9.677485757,	2.001161223,	0.04898213,	0.04097683,	0.065550507,	0.342116679]
BE_20_MC = [0.51,	0.55,	0.89,	1.28,	1.21,	0.03,	0.03,	0.01,	0.28]

ES_150_U = [1.407128143,	1.558857415,	2.376392288,	1.88,	3.248734193,	0.066670407,	0.077373487,	0.020727267,	0.504732111]
ES_83_U = [0.778610909,	1.468651792,	2.925893377,	1.88,	3.691645491,	0.060417244,	0.08375373,	0.023882016,	0.389991778]
ES_17_U =    [0.159474524,	1.282846787,	3.052887502,	1.88,	3.292111163,	0.047792824,	0.083583072,	0.025203392,	0.225900546]
ES_17_U_MC = [0.19,	        1.27,	        2.47,	        1.88,	        2.30,	0.04,	         0.07,	         0.02,	        0.21]
ES_17_U_PV = [0.94,	1.48,	3.01,	3.66,	3.22,	0.06,	0.09,	0.02,	0.37]
CH_22_U = [1.296498306,	2.2671197,	3.872660148,	3.117897048,	3.689888697,	0.092316708,	0.119154247,	0.023324515,	0.493994211]
CH_10_U = [1.063574934,	1.808763135,	1.384293145,	1.590772928,	1.822864922,	0.066966987,	0.051196987,	0.017773345,	0.340675459]
CH_2_U = [0.284891776,	2.291729684,	5.453802419,	3.362971136,	5.881161299,	0.085379046,	0.149316199,	0.045024364,	0.403557925]
CH_2_MC = [0.84,	1.93,	1.33,	2.42,	2.12,	0.08,	0.05,	0.06,	0.45]
CH_2_MC_2 = [0.95,	1.86,	1.15,	1.82,	1.80,	0.07,	0.05,	0.02,	0.42]

#FEDECOM - PILOT SCALE#
LIC_PV_2t = [0.520341378,	0.565730126,	1.956468691,	2.215928582,	0.317061509,	0.003352882,	0.063148573,	0.019304426,	0.023345987]
LIC_GRID_2t = [1.261980248,	0.707696734,	0.529844733,	11.06313972,	0.125476016,	0.00167683,	    0.031821786,	0.048100932,	0.044141429]

ES_NEW_150 = [0.47,	1.56,	4.88,	6.49,	4.55,	0.07,	0.15,	0.03,	0.36]
ES_NEW_100 = [0.94,	2.31,	9.68,	9.39,	8.15,	0.12,	0.31,	0.04,	0.52]
ES_NEW_50 = [1.26,	1.92,	5.33,	5.72,	5.22,	0.09,	0.17,	0.03,	0.48]

BE_100_new = [2.54,	3.36,	17.12,	16.49,	14.02,	0.24,	0.58,	0.08,	1.31]
BE_50_new = [1.27,	1.23,	1.00,	5.12,	2.19,	0.08,	0.04,	0.03,	0.68]
BE_10_new = [0.25,	0.71,	0.98,	12.92,	1.80,	0.06,	0.04,	0.02,	0.58]

CH_100_new = [2.54,	3.36,	17.12,	16.49,	14.02,	0.24,	0.58,	0.08,	1.31]
CH_50_new = [0.84,	1.84,	1.39,	5.89,	1.90,	0.07,	0.05,	0.02,	0.36]
CH_10_new = [0.25,	0.71,	0.98,	12.92,	1.80,	0.06,	0.04,	0.02,	0.58]


values = LIC_PV_2t
# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for the values and angles
values += values[:1]
angles += angles[:1]

# Create polar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Set up color for each segment
colors = ['green' if v <= 1 else 'orange' if v <= 2 else 'red' for v in values[:-1]]

# Plot each segment starting further out to make the inner circle larger
bars = ax.bar(angles[:-1], values[:-1], width=2*np.pi/num_vars, color=colors, align='edge', edgecolor='grey', bottom=0)  # Increase 'bottom' for larger inner circle

# Set the radial limit so the circle is capped at 7 (to leave some space)
ax.set_ylim(0, 7)

# Make the center circle white by setting the facecolor
ax.set_facecolor('white')

# Remove category labels on the axes
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])

# Set the radial ticks (grey circles) with a step size of 1
ax.set_yticks(np.arange(1, 7, 2))  # Tick marks from 1 to 15 with a step size of 2
ax.yaxis.grid(True, linestyle=':', alpha=0.8)

# Remove radial labels (already hidden)
ax.set_yticklabels([])

# Show the plot in a separate window
plt.show()
