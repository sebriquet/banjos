import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$2 / H1_HlyIIR")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.997164e-05,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.997164e-05,0.000000e+00,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,1.997164e-05,1.997164e-05,2.995746e-05,0.000000e+00,9.985820e-06,9.985820e-06,1.997164e-05,9.985820e-06,9.985820e-06,0.000000e+00,3.994328e-05,9.985820e-06,1.997164e-05,1.997164e-05,5.991492e-05,9.985820e-06,2.995746e-05,3.994328e-05,3.994328e-05,2.995746e-05,3.994328e-05,1.997164e-05,0.000000e+00,2.995746e-05,1.997164e-05,2.995746e-05,3.994328e-05,1.997164e-05,4.992910e-05,9.985820e-06,5.991492e-05,1.997164e-05,5.991492e-05,3.994328e-05,4.992910e-05,6.990074e-05,4.992910e-05,8.987238e-05,6.990074e-05,8.987238e-05,9.985820e-06,6.990074e-05,6.990074e-05,8.987238e-05,7.988656e-05,9.985820e-05,7.988656e-05,7.988656e-05,1.497873e-04,4.992910e-05,5.991492e-05,4.992910e-05,7.988656e-05,5.991492e-05,8.987238e-05,7.988656e-05,4.992910e-05,4.992910e-05,6.990074e-05,3.994328e-05,3.994328e-05,4.992910e-05,4.992910e-05,2.995746e-05,1.997164e-05,4.992910e-05,3.994328e-05,3.994328e-05,3.994328e-05,9.985820e-06,1.997164e-05,9.985820e-06,0.000000e+00,4.992910e-05,1.997164e-05,0.000000e+00,1.997164e-05,9.985820e-06,1.997164e-05,2.995746e-05,1.997164e-05,3.994328e-05,1.997164e-05,3.994328e-05,2.995746e-05,1.997164e-05,1.997164e-05,6.990074e-05,2.995746e-05,0.000000e+00,4.992910e-05,1.997164e-05,2.995746e-05,8.987238e-05,1.298157e-04,4.693335e-04,4.194044e-04,9.386671e-04,1.427972e-03,2.386611e-03,3.475065e-03,5.661960e-03,8.198358e-03,1.226259e-02,1.695592e-02,2.131973e-02,2.842963e-02,3.310299e-02,4.008308e-02,4.504603e-02,5.122726e-02,5.494198e-02,5.650976e-02,5.807753e-02,5.646981e-02,5.676939e-02,5.393341e-02,4.969943e-02,4.416728e-02,3.842544e-02,3.435122e-02,3.025704e-02,2.536398e-02,2.216852e-02,1.941243e-02,1.633680e-02,1.389028e-02,1.260211e-02,1.182321e-02,1.049510e-02,8.767550e-03,6.850273e-03,6.301053e-03,5.102754e-03,4.184059e-03,3.544966e-03,3.435122e-03,2.596313e-03,2.316710e-03,1.937249e-03,1.487887e-03,1.567774e-03,1.218270e-03,1.068483e-03,1.128398e-03,8.587805e-04,7.888798e-04,8.188373e-04,5.991492e-04,4.593477e-04,5.192626e-04,3.794612e-04,4.493619e-04,3.994328e-04,2.796030e-04,2.696171e-04,1.597731e-04,2.196880e-04,1.597731e-04,1.597731e-04,7.988656e-05,1.198298e-04,9.985820e-05,7.988656e-05,5.991492e-05,3.994328e-05,7.988656e-05,1.298157e-04,1.997164e-05,9.985820e-06,4.992910e-05,9.985820e-06,2.995746e-05,9.985820e-06,9.985820e-06,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.997164e-05,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.997164e-05,0.000000e+00,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,1.997164e-05,1.997164e-05,2.995746e-05,0.000000e+00,9.985820e-06,9.985820e-06,1.997164e-05,9.985820e-06,9.985820e-06,0.000000e+00,3.994328e-05,9.985820e-06,1.997164e-05,1.997164e-05,5.991492e-05,9.985820e-06,2.995746e-05,3.994328e-05,3.994328e-05,2.995746e-05,3.994328e-05,1.997164e-05,0.000000e+00,2.995746e-05,1.997164e-05,2.995746e-05,3.994328e-05,1.997164e-05,4.992910e-05,9.985820e-06,5.991492e-05,1.997164e-05,5.991492e-05,3.994328e-05,4.992910e-05,6.990074e-05,4.992910e-05,8.987238e-05,6.990074e-05,8.987238e-05,9.985820e-06,6.990074e-05,6.990074e-05,8.987238e-05,7.988656e-05,9.985820e-05,7.988656e-05,7.988656e-05,1.497873e-04,4.992910e-05,5.991492e-05,4.992910e-05,7.988656e-05,5.991492e-05,8.987238e-05,7.988656e-05,4.992910e-05,4.992910e-05,6.990074e-05,3.994328e-05,3.994328e-05,4.992910e-05,4.992910e-05,2.995746e-05,1.997164e-05,4.992910e-05,3.994328e-05,3.994328e-05,3.994328e-05,9.985820e-06,1.997164e-05,9.985820e-06,0.000000e+00,4.992910e-05,1.997164e-05,0.000000e+00,1.997164e-05,9.985820e-06,1.997164e-05,2.995746e-05,1.997164e-05,3.994328e-05,1.997164e-05,3.994328e-05,2.995746e-05,1.997164e-05,1.997164e-05,6.990074e-05,2.995746e-05,0.000000e+00,4.992910e-05,1.997164e-05,2.995746e-05,8.987238e-05,1.298157e-04,4.693335e-04,4.194044e-04,9.386671e-04,1.427972e-03,2.386611e-03,3.475065e-03,5.661960e-03,8.198358e-03,1.226259e-02,1.695592e-02,2.131973e-02,2.842963e-02,3.310299e-02,4.008308e-02,4.504603e-02,5.122726e-02,5.494198e-02,5.650976e-02,5.807753e-02,5.646981e-02,5.676939e-02,5.393341e-02,4.969943e-02,4.416728e-02,3.842544e-02,3.435122e-02,3.025704e-02,2.536398e-02,2.216852e-02,1.941243e-02,1.633680e-02,1.389028e-02,1.260211e-02,1.182321e-02,1.049510e-02,8.767550e-03,6.850273e-03,6.301053e-03,5.102754e-03,4.184059e-03,3.544966e-03,3.435122e-03,2.596313e-03,2.316710e-03,1.937249e-03,1.487887e-03,1.567774e-03,1.218270e-03,1.068483e-03,1.128398e-03,8.587805e-04,7.888798e-04,8.188373e-04,5.991492e-04,4.593477e-04,5.192626e-04,3.794612e-04,4.493619e-04,3.994328e-04,2.796030e-04,2.696171e-04,1.597731e-04,2.196880e-04,1.597731e-04,1.597731e-04,7.988656e-05,1.198298e-04,9.985820e-05,7.988656e-05,5.991492e-05,3.994328e-05,7.988656e-05,1.298157e-04,1.997164e-05,9.985820e-06,4.992910e-05,9.985820e-06,2.995746e-05,9.985820e-06,9.985820e-06,9.985820e-06,9.985820e-06,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.985820e-06,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [8.154279e-05,3.057855e-05,4.077139e-05,1.019285e-05,5.096424e-05,6.115709e-05,2.038570e-05,5.096424e-05,1.019285e-05,4.077139e-05,9.173564e-05,1.019285e-04,4.077139e-05,8.154279e-05,7.134994e-05,6.115709e-05,5.096424e-05,4.077139e-05,3.057855e-05,8.154279e-05,7.134994e-05,5.096424e-05,8.154279e-05,7.134994e-05,8.154279e-05,1.019285e-04,1.325070e-04,2.038570e-04,1.223142e-04,1.630856e-04,1.019285e-04,3.057855e-04,1.630856e-04,1.936641e-04,1.834713e-04,2.038570e-04,1.834713e-04,3.363640e-04,4.586782e-04,3.567497e-04,2.548212e-04,3.057855e-04,2.548212e-04,2.752069e-04,5.300281e-04,4.994496e-04,4.484853e-04,2.853998e-04,4.280996e-04,5.707995e-04,5.504138e-04,4.077139e-04,5.911852e-04,8.358136e-04,6.625352e-04,6.625352e-04,9.581278e-04,6.523423e-04,9.887063e-04,9.479349e-04,9.887063e-04,1.304685e-03,1.131406e-03,1.325070e-03,1.223142e-03,1.294492e-03,1.569699e-03,1.345456e-03,1.814327e-03,1.865291e-03,1.977413e-03,1.936641e-03,2.293391e-03,2.273005e-03,2.660334e-03,3.078240e-03,3.006890e-03,3.200554e-03,4.077139e-03,4.158682e-03,4.739675e-03,5.116810e-03,4.770253e-03,5.626452e-03,6.594773e-03,6.339952e-03,7.410201e-03,8.042158e-03,8.949321e-03,9.346842e-03,1.038651e-02,1.170139e-02,1.288376e-02,1.403555e-02,1.530966e-02,1.676724e-02,1.780691e-02,2.088515e-02,2.134383e-02,2.355567e-02,2.534961e-02,2.658295e-02,2.911078e-02,3.025237e-02,3.191381e-02,3.355486e-02,3.568516e-02,3.539976e-02,3.580748e-02,3.800913e-02,3.677580e-02,3.779508e-02,3.588902e-02,3.364659e-02,3.221959e-02,2.912097e-02,2.681738e-02,2.338239e-02,2.054878e-02,1.741958e-02,1.430057e-02,1.256778e-02,9.703592e-03,8.694500e-03,7.400008e-03,5.840502e-03,4.882375e-03,4.005790e-03,3.445183e-03,3.017083e-03,2.588984e-03,2.171077e-03,1.906063e-03,1.569699e-03,1.467770e-03,1.172178e-03,1.060056e-03,8.460064e-04,9.988992e-04,6.931137e-04,6.319566e-04,5.504138e-04,6.625352e-04,3.261712e-04,4.892567e-04,3.669426e-04,3.057855e-04,3.159783e-04,2.242427e-04,2.752069e-04,1.630856e-04,2.242427e-04,2.140498e-04,2.038570e-04,1.732784e-04,1.426999e-04,1.223142e-04,1.223142e-04,1.019285e-04,6.115709e-05,7.134994e-05,5.096424e-05,7.134994e-05,3.057855e-05,8.154279e-05,1.223142e-04,5.096424e-05,3.057855e-05,4.077139e-05,1.019285e-05,3.057855e-05,4.077139e-05,3.057855e-05,3.057855e-05,1.019285e-05,2.038570e-05,4.077139e-05,0.000000e+00,1.019285e-05,2.038570e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.038570e-05,1.019285e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.019285e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.019285e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [8.154279e-05,3.057855e-05,4.077139e-05,1.019285e-05,5.096424e-05,6.115709e-05,2.038570e-05,5.096424e-05,1.019285e-05,4.077139e-05,9.173564e-05,1.019285e-04,4.077139e-05,8.154279e-05,7.134994e-05,6.115709e-05,5.096424e-05,4.077139e-05,3.057855e-05,8.154279e-05,7.134994e-05,5.096424e-05,8.154279e-05,7.134994e-05,8.154279e-05,1.019285e-04,1.325070e-04,2.038570e-04,1.223142e-04,1.630856e-04,1.019285e-04,3.057855e-04,1.630856e-04,1.936641e-04,1.834713e-04,2.038570e-04,1.834713e-04,3.363640e-04,4.586782e-04,3.567497e-04,2.548212e-04,3.057855e-04,2.548212e-04,2.752069e-04,5.300281e-04,4.994496e-04,4.484853e-04,2.853998e-04,4.280996e-04,5.707995e-04,5.504138e-04,4.077139e-04,5.911852e-04,8.358136e-04,6.625352e-04,6.625352e-04,9.581278e-04,6.523423e-04,9.887063e-04,9.479349e-04,9.887063e-04,1.304685e-03,1.131406e-03,1.325070e-03,1.223142e-03,1.294492e-03,1.569699e-03,1.345456e-03,1.814327e-03,1.865291e-03,1.977413e-03,1.936641e-03,2.293391e-03,2.273005e-03,2.660334e-03,3.078240e-03,3.006890e-03,3.200554e-03,4.077139e-03,4.158682e-03,4.739675e-03,5.116810e-03,4.770253e-03,5.626452e-03,6.594773e-03,6.339952e-03,7.410201e-03,8.042158e-03,8.949321e-03,9.346842e-03,1.038651e-02,1.170139e-02,1.288376e-02,1.403555e-02,1.530966e-02,1.676724e-02,1.780691e-02,2.088515e-02,2.134383e-02,2.355567e-02,2.534961e-02,2.658295e-02,2.911078e-02,3.025237e-02,3.191381e-02,3.355486e-02,3.568516e-02,3.539976e-02,3.580748e-02,3.800913e-02,3.677580e-02,3.779508e-02,3.588902e-02,3.364659e-02,3.221959e-02,2.912097e-02,2.681738e-02,2.338239e-02,2.054878e-02,1.741958e-02,1.430057e-02,1.256778e-02,9.703592e-03,8.694500e-03,7.400008e-03,5.840502e-03,4.882375e-03,4.005790e-03,3.445183e-03,3.017083e-03,2.588984e-03,2.171077e-03,1.906063e-03,1.569699e-03,1.467770e-03,1.172178e-03,1.060056e-03,8.460064e-04,9.988992e-04,6.931137e-04,6.319566e-04,5.504138e-04,6.625352e-04,3.261712e-04,4.892567e-04,3.669426e-04,3.057855e-04,3.159783e-04,2.242427e-04,2.752069e-04,1.630856e-04,2.242427e-04,2.140498e-04,2.038570e-04,1.732784e-04,1.426999e-04,1.223142e-04,1.223142e-04,1.019285e-04,6.115709e-05,7.134994e-05,5.096424e-05,7.134994e-05,3.057855e-05,8.154279e-05,1.223142e-04,5.096424e-05,3.057855e-05,4.077139e-05,1.019285e-05,3.057855e-05,4.077139e-05,3.057855e-05,3.057855e-05,1.019285e-05,2.038570e-05,4.077139e-05,0.000000e+00,1.019285e-05,2.038570e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.038570e-05,1.019285e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.019285e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.019285e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$2_H1_HlyIIR.png", bbox_inches='tight')
