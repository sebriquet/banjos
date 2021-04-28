import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / B3_BM3R1")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [4.471996e-04,3.855169e-04,2.158895e-04,2.158895e-04,2.621515e-04,5.243030e-04,2.158895e-04,6.785097e-04,4.009376e-04,4.471996e-04,6.476684e-04,5.397237e-04,4.163583e-04,4.471996e-04,5.243030e-04,4.934616e-04,7.401925e-04,4.163583e-04,6.322477e-04,7.093511e-04,5.088823e-04,5.551443e-04,4.626203e-04,6.168270e-04,8.327165e-04,9.560819e-04,8.172958e-04,1.464964e-03,1.357019e-03,1.279916e-03,1.310757e-03,1.202813e-03,1.218233e-03,8.327165e-04,1.202813e-03,1.171971e-03,1.603750e-03,1.850481e-03,2.081791e-03,2.266839e-03,2.112633e-03,1.757957e-03,1.711695e-03,2.205157e-03,3.562176e-03,2.929928e-03,2.698618e-03,2.189736e-03,3.207501e-03,4.071058e-03,3.654700e-03,2.991611e-03,4.117321e-03,5.057982e-03,3.546755e-03,4.657044e-03,5.983222e-03,4.317789e-03,5.366395e-03,5.952381e-03,6.322477e-03,6.630891e-03,6.615470e-03,7.926227e-03,7.864545e-03,7.170614e-03,9.884653e-03,7.926227e-03,1.000802e-02,1.117999e-02,1.060943e-02,1.099494e-02,1.076363e-02,1.279916e-02,1.353935e-02,1.320010e-02,1.569825e-02,1.546694e-02,1.716321e-02,1.682396e-02,1.682396e-02,1.956884e-02,1.819640e-02,2.124969e-02,2.095670e-02,2.203615e-02,2.300765e-02,2.410252e-02,2.528991e-02,2.458056e-02,2.562916e-02,2.749507e-02,2.670861e-02,2.797311e-02,2.897545e-02,2.678571e-02,2.616889e-02,2.791142e-02,2.476561e-02,2.490439e-02,2.427214e-02,2.239082e-02,2.033987e-02,1.909080e-02,1.779546e-02,1.491179e-02,1.386319e-02,1.176598e-02,9.653343e-03,8.743523e-03,6.661732e-03,5.829016e-03,3.716383e-03,3.423390e-03,2.220577e-03,1.650012e-03,1.264495e-03,9.406612e-04,6.168270e-04,6.322477e-04,5.551443e-04,2.929928e-04,4.009376e-04,3.392549e-04,2.313101e-04,1.542068e-04,2.004688e-04,9.252406e-05,1.696274e-04,1.542068e-04,9.252406e-05,7.710338e-05,7.710338e-05,7.710338e-05,1.542068e-05,4.626203e-05,4.626203e-05,6.168270e-05,6.168270e-05,0.000000e+00,1.542068e-05,0.000000e+00,3.084135e-05,0.000000e+00,4.626203e-05,3.084135e-05,3.084135e-05,1.542068e-05,1.542068e-05,3.084135e-05,0.000000e+00,1.542068e-05,1.542068e-05,3.084135e-05,1.542068e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.542068e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [4.471996e-04,3.855169e-04,2.158895e-04,2.158895e-04,2.621515e-04,5.243030e-04,2.158895e-04,6.785097e-04,4.009376e-04,4.471996e-04,6.476684e-04,5.397237e-04,4.163583e-04,4.471996e-04,5.243030e-04,4.934616e-04,7.401925e-04,4.163583e-04,6.322477e-04,7.093511e-04,5.088823e-04,5.551443e-04,4.626203e-04,6.168270e-04,8.327165e-04,9.560819e-04,8.172958e-04,1.464964e-03,1.357019e-03,1.279916e-03,1.310757e-03,1.202813e-03,1.218233e-03,8.327165e-04,1.202813e-03,1.171971e-03,1.603750e-03,1.850481e-03,2.081791e-03,2.266839e-03,2.112633e-03,1.757957e-03,1.711695e-03,2.205157e-03,3.562176e-03,2.929928e-03,2.698618e-03,2.189736e-03,3.207501e-03,4.071058e-03,3.654700e-03,2.991611e-03,4.117321e-03,5.057982e-03,3.546755e-03,4.657044e-03,5.983222e-03,4.317789e-03,5.366395e-03,5.952381e-03,6.322477e-03,6.630891e-03,6.615470e-03,7.926227e-03,7.864545e-03,7.170614e-03,9.884653e-03,7.926227e-03,1.000802e-02,1.117999e-02,1.060943e-02,1.099494e-02,1.076363e-02,1.279916e-02,1.353935e-02,1.320010e-02,1.569825e-02,1.546694e-02,1.716321e-02,1.682396e-02,1.682396e-02,1.956884e-02,1.819640e-02,2.124969e-02,2.095670e-02,2.203615e-02,2.300765e-02,2.410252e-02,2.528991e-02,2.458056e-02,2.562916e-02,2.749507e-02,2.670861e-02,2.797311e-02,2.897545e-02,2.678571e-02,2.616889e-02,2.791142e-02,2.476561e-02,2.490439e-02,2.427214e-02,2.239082e-02,2.033987e-02,1.909080e-02,1.779546e-02,1.491179e-02,1.386319e-02,1.176598e-02,9.653343e-03,8.743523e-03,6.661732e-03,5.829016e-03,3.716383e-03,3.423390e-03,2.220577e-03,1.650012e-03,1.264495e-03,9.406612e-04,6.168270e-04,6.322477e-04,5.551443e-04,2.929928e-04,4.009376e-04,3.392549e-04,2.313101e-04,1.542068e-04,2.004688e-04,9.252406e-05,1.696274e-04,1.542068e-04,9.252406e-05,7.710338e-05,7.710338e-05,7.710338e-05,1.542068e-05,4.626203e-05,4.626203e-05,6.168270e-05,6.168270e-05,0.000000e+00,1.542068e-05,0.000000e+00,3.084135e-05,0.000000e+00,4.626203e-05,3.084135e-05,3.084135e-05,1.542068e-05,1.542068e-05,3.084135e-05,0.000000e+00,1.542068e-05,1.542068e-05,3.084135e-05,1.542068e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.542068e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [4.471996e-04,3.855169e-04,2.158895e-04,2.158895e-04,2.621515e-04,5.243030e-04,2.158895e-04,6.785097e-04,4.009376e-04,4.471996e-04,6.476684e-04,5.397237e-04,4.163583e-04,4.471996e-04,5.243030e-04,4.934616e-04,7.401925e-04,4.163583e-04,6.322477e-04,7.093511e-04,5.088823e-04,5.551443e-04,4.626203e-04,6.168270e-04,8.327165e-04,9.560819e-04,8.172958e-04,1.464964e-03,1.357019e-03,1.279916e-03,1.310757e-03,1.202813e-03,1.218233e-03,8.327165e-04,1.202813e-03,1.171971e-03,1.603750e-03,1.850481e-03,2.081791e-03,2.266839e-03,2.112633e-03,1.757957e-03,1.711695e-03,2.205157e-03,3.562176e-03,2.929928e-03,2.698618e-03,2.189736e-03,3.207501e-03,4.071058e-03,3.654700e-03,2.991611e-03,4.117321e-03,5.057982e-03,3.546755e-03,4.657044e-03,5.983222e-03,4.317789e-03,5.366395e-03,5.952381e-03,6.322477e-03,6.630891e-03,6.615470e-03,7.926227e-03,7.864545e-03,7.170614e-03,9.884653e-03,7.926227e-03,1.000802e-02,1.117999e-02,1.060943e-02,1.099494e-02,1.076363e-02,1.279916e-02,1.353935e-02,1.320010e-02,1.569825e-02,1.546694e-02,1.716321e-02,1.682396e-02,1.682396e-02,1.956884e-02,1.819640e-02,2.124969e-02,2.095670e-02,2.203615e-02,2.300765e-02,2.410252e-02,2.528991e-02,2.458056e-02,2.562916e-02,2.749507e-02,2.670861e-02,2.797311e-02,2.897545e-02,2.678571e-02,2.616889e-02,2.791142e-02,2.476561e-02,2.490439e-02,2.427214e-02,2.239082e-02,2.033987e-02,1.909080e-02,1.779546e-02,1.491179e-02,1.386319e-02,1.176598e-02,9.653343e-03,8.743523e-03,6.661732e-03,5.829016e-03,3.716383e-03,3.423390e-03,2.220577e-03,1.650012e-03,1.264495e-03,9.406612e-04,6.168270e-04,6.322477e-04,5.551443e-04,2.929928e-04,4.009376e-04,3.392549e-04,2.313101e-04,1.542068e-04,2.004688e-04,9.252406e-05,1.696274e-04,1.542068e-04,9.252406e-05,7.710338e-05,7.710338e-05,7.710338e-05,1.542068e-05,4.626203e-05,4.626203e-05,6.168270e-05,6.168270e-05,0.000000e+00,1.542068e-05,0.000000e+00,3.084135e-05,0.000000e+00,4.626203e-05,3.084135e-05,3.084135e-05,1.542068e-05,1.542068e-05,3.084135e-05,0.000000e+00,1.542068e-05,1.542068e-05,3.084135e-05,1.542068e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.542068e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.416645e-04,8.571043e-05,5.108041e-05,8.669398e-05,1.101878e-04,2.029417e-04,8.464759e-05,1.867291e-04,1.274632e-04,1.317145e-04,2.101437e-04,1.745301e-04,2.356046e-04,1.775600e-04,1.398208e-04,1.560333e-04,1.530034e-04,1.051908e-04,2.080180e-04,2.274983e-04,1.795271e-04,1.510363e-04,1.489899e-04,2.091601e-04,3.040396e-04,2.072723e-04,3.682234e-04,4.408305e-04,4.183202e-04,4.305193e-04,4.713677e-04,5.661680e-04,3.572457e-04,4.183202e-04,5.099320e-04,3.713326e-04,5.326008e-04,6.437722e-04,7.530557e-04,8.040568e-04,6.896970e-04,6.437722e-04,5.795884e-04,8.365612e-04,1.066106e-03,1.030492e-03,9.915316e-04,7.927620e-04,9.970044e-04,1.504890e-03,1.248663e-03,1.068311e-03,1.608859e-03,1.796413e-03,1.437280e-03,1.457157e-03,2.070154e-03,1.598627e-03,2.452464e-03,2.129023e-03,2.007112e-03,2.791292e-03,2.216939e-03,2.830761e-03,2.877161e-03,3.173444e-03,3.629820e-03,3.423452e-03,4.028264e-03,4.172653e-03,4.321167e-03,4.260601e-03,4.719341e-03,5.492813e-03,5.600050e-03,6.061345e-03,6.372428e-03,6.927888e-03,7.381980e-03,7.314021e-03,7.827649e-03,9.309712e-03,9.187008e-03,1.036168e-02,1.127686e-02,1.072140e-02,1.207864e-02,1.306225e-02,1.417030e-02,1.545926e-02,1.556796e-02,1.651115e-02,1.773215e-02,1.857082e-02,1.946652e-02,2.036623e-02,2.206642e-02,2.337103e-02,2.414143e-02,2.516872e-02,2.581154e-02,2.612848e-02,2.704440e-02,2.796996e-02,2.874189e-02,2.912049e-02,2.916204e-02,2.853456e-02,2.771150e-02,2.762215e-02,2.672641e-02,2.617236e-02,2.447839e-02,2.246212e-02,2.152372e-02,1.921476e-02,1.684145e-02,1.664555e-02,1.420944e-02,1.237515e-02,1.050744e-02,9.553855e-03,8.076408e-03,7.097519e-03,6.146804e-03,5.733052e-03,3.879831e-03,3.695386e-03,2.968980e-03,2.271066e-03,2.142619e-03,2.018424e-03,1.670982e-03,1.233895e-03,1.196235e-03,1.086126e-03,9.882959e-04,9.414668e-04,8.049139e-04,5.145325e-04,5.522718e-04,4.401962e-04,5.227181e-04,4.177652e-04,3.810888e-04,3.535815e-04,2.649204e-04,2.853050e-04,3.372897e-04,2.017202e-04,1.579211e-04,1.670902e-04,1.212447e-04,1.691366e-04,1.029065e-04,1.029065e-04,1.365530e-04,1.008601e-04,1.008601e-04,4.993829e-05,2.243098e-05,4.993829e-05,1.029065e-04,2.750731e-05,3.160008e-05,2.955369e-05,4.584551e-05,4.789190e-05,1.833820e-05,0.000000e+00,2.046388e-06,2.046388e-06,2.447737e-05,1.121549e-05,2.750731e-05,9.169102e-06,2.046388e-06,1.833820e-05,0.000000e+00,1.326188e-05,1.833820e-05,0.000000e+00,0.000000e+00,1.833820e-05,0.000000e+00,2.243098e-05,0.000000e+00,1.326188e-05,2.046388e-06,0.000000e+00,0.000000e+00,9.169102e-06,0.000000e+00,9.169102e-06,0.000000e+00,0.000000e+00,0.000000e+00,2.046388e-06,0.000000e+00,0.000000e+00,0.000000e+00,9.169102e-06,9.169102e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.169102e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_B3_BM3R1.png", bbox_inches='tight')