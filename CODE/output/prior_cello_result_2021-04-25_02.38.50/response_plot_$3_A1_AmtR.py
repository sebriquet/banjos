import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([3.795829e+00,3.794987e+00,3.793974e+00,3.792758e+00,3.791296e+00,3.789541e+00,3.787432e+00,3.784901e+00,3.781861e+00,3.778214e+00,3.773838e+00,3.768591e+00,3.762302e+00,3.754770e+00,3.745754e+00,3.734972e+00,3.722094e+00,3.706729e+00,3.688426e+00,3.666664e+00,3.640842e+00,3.610283e+00,3.574227e+00,3.531835e+00,3.482204e+00,3.424380e+00,3.357397e+00,3.280314e+00,3.192280e+00,3.092609e+00,2.980866e+00,2.856961e+00,2.721236e+00,2.574535e+00,2.418243e+00,2.254271e+00,2.084991e+00,1.913115e+00,1.741523e+00,1.573079e+00,1.410439e+00,1.255893e+00,1.111252e+00,9.777946e-01,8.562620e-01,7.469057e-01,6.495601e-01,5.637338e-01,4.887017e-01,4.235901e-01,3.674495e-01,3.193116e-01,2.782316e-01,2.433167e-01,2.137440e-01,1.887692e-01,1.677296e-01,1.500419e-01,1.351982e-01,1.227594e-01,1.123488e-01,1.036446e-01,9.637341e-02,9.030367e-02,8.523990e-02,8.101750e-02,7.749814e-02,7.456578e-02,7.212323e-02,7.008917e-02,6.839561e-02,6.698581e-02,6.581237e-02,6.483578e-02,6.402310e-02,6.334688e-02,6.278423e-02,6.231611e-02,6.192666e-02,6.160266e-02,6.133313e-02,6.110892e-02,6.092240e-02,6.076725e-02,6.063820e-02,6.053084e-02,6.044155e-02,6.036727e-02,6.030549e-02,6.025410e-02,6.021135e-02,6.017580e-02,6.014622e-02,6.012162e-02,6.010116e-02,6.008414e-02,6.006999e-02,6.005821e-02,6.004842e-02,6.004027e-02,6.003350e-02,])
c = "#3ba9e0"

hi_x = np.array([3.400000e-03,3.400000e-03,])
hi_y = np.array([3.770647e+00,3.770647e+00,])
lo_x = np.array([2.800000e+00,2.800000e+00,])
lo_y = np.array([7.019507e-02,7.019507e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / A1_AmtR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_A1_AmtR.png", bbox_inches='tight')
