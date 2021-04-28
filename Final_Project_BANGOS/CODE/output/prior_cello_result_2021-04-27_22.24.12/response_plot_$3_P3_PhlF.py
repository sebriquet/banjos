import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.799999e+00,6.799999e+00,6.799998e+00,6.799997e+00,6.799995e+00,6.799992e+00,6.799987e+00,6.799979e+00,6.799966e+00,6.799945e+00,6.799910e+00,6.799855e+00,6.799765e+00,6.799618e+00,6.799381e+00,6.798996e+00,6.798371e+00,6.797359e+00,6.795717e+00,6.793057e+00,6.788747e+00,6.781769e+00,6.770483e+00,6.752258e+00,6.722909e+00,6.675850e+00,6.600919e+00,6.482918e+00,6.300285e+00,6.025072e+00,5.626608e+00,5.081876e+00,4.392834e+00,3.602038e+00,2.789704e+00,2.044942e+00,1.430031e+00,9.647490e-01,6.354056e-01,4.131375e-01,2.679183e-01,1.750387e-01,1.164417e-01,7.979153e-02,5.699223e-02,4.285704e-02,3.411178e-02,2.870820e-02,2.537208e-02,2.331340e-02,2.204341e-02,2.126010e-02,2.077703e-02,2.047913e-02,2.029544e-02,2.018217e-02,2.011233e-02,2.006926e-02,2.004271e-02,2.002633e-02,2.001624e-02,2.001001e-02,2.000617e-02,2.000381e-02,2.000235e-02,2.000145e-02,2.000089e-02,2.000055e-02,2.000034e-02,2.000021e-02,2.000013e-02,2.000008e-02,2.000005e-02,2.000003e-02,2.000002e-02,2.000001e-02,2.000001e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,])
c = "#f9a427"

hi_x = np.array([1.300000e-03,1.300000e-03,])
hi_y = np.array([6.800000e+00,6.800000e+00,])
lo_x = np.array([4.400000e+00,4.400000e+00,])
lo_y = np.array([2.002805e-02,2.002805e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / P3_PhlF")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_P3_PhlF.png", bbox_inches='tight')
