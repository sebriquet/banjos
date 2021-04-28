import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / P3_PhlF")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [4.301833e-04,2.517348e-04,2.639544e-04,2.073824e-04,2.892575e-04,4.525755e-04,2.041836e-04,6.284011e-04,2.451931e-04,4.525755e-04,6.601020e-04,4.556304e-04,4.678499e-04,5.497250e-04,4.054562e-04,4.397800e-04,6.439635e-04,4.431229e-04,4.995508e-04,5.529239e-04,4.838444e-04,5.120583e-04,5.309637e-04,6.249142e-04,6.093518e-04,8.958424e-04,9.140277e-04,1.187579e-03,1.348274e-03,1.401791e-03,1.351185e-03,1.417209e-03,1.112101e-03,7.946300e-04,8.638535e-04,1.166627e-03,1.521189e-03,2.004457e-03,2.158466e-03,2.294290e-03,1.712145e-03,1.910362e-03,1.804192e-03,2.215038e-03,3.101572e-03,2.721563e-03,2.519426e-03,2.174173e-03,3.122812e-03,3.887037e-03,3.274487e-03,2.853612e-03,4.146353e-03,4.797434e-03,3.283363e-03,4.524747e-03,5.548144e-03,3.874530e-03,5.681057e-03,5.607339e-03,5.788235e-03,6.881431e-03,6.099165e-03,7.336774e-03,7.419945e-03,7.715168e-03,9.269528e-03,7.599288e-03,9.139526e-03,1.024114e-02,1.056720e-02,1.050394e-02,1.140284e-02,1.213231e-02,1.263782e-02,1.339202e-02,1.404004e-02,1.529613e-02,1.586882e-02,1.617569e-02,1.708508e-02,1.885287e-02,1.837459e-02,2.001855e-02,2.166841e-02,2.146074e-02,2.278051e-02,2.329839e-02,2.487702e-02,2.447026e-02,2.495033e-02,2.703448e-02,2.611592e-02,2.776876e-02,2.818626e-02,2.686925e-02,2.695505e-02,2.813609e-02,2.581084e-02,2.574741e-02,2.469134e-02,2.329545e-02,2.184712e-02,1.951965e-02,1.829865e-02,1.582084e-02,1.396909e-02,1.211268e-02,1.074432e-02,8.635594e-03,7.218816e-03,6.105131e-03,4.710169e-03,3.695361e-03,2.893758e-03,2.127054e-03,1.668080e-03,1.326170e-03,1.042878e-03,9.332210e-04,9.240564e-04,8.581758e-04,5.716852e-04,5.500130e-04,5.719732e-04,4.709048e-04,3.862629e-04,3.613918e-04,3.298350e-04,3.144166e-04,2.482480e-04,2.197460e-04,1.854222e-04,1.979298e-04,2.385073e-04,1.287063e-04,2.168351e-04,1.791685e-04,1.129999e-04,1.285623e-04,1.319052e-04,1.038352e-04,1.381590e-04,8.492991e-05,1.351041e-04,8.478591e-05,5.322905e-05,5.031817e-05,5.337305e-05,6.893548e-05,8.158702e-05,4.086551e-05,6.253771e-06,4.392040e-05,7.533325e-05,3.461174e-05,4.711928e-05,5.351706e-05,2.515908e-05,1.570643e-05,1.876131e-05,3.141286e-05,1.570643e-05,2.196020e-05,6.253771e-06,1.570643e-05,1.876131e-05,1.570643e-05,0.000000e+00,0.000000e+00,2.835797e-05,0.000000e+00,6.253771e-06,3.461174e-05,1.570643e-05,0.000000e+00,9.452657e-06,2.821397e-05,0.000000e+00,2.501508e-05,0.000000e+00,0.000000e+00,1.250754e-05,0.000000e+00,9.452657e-06,0.000000e+00,0.000000e+00,6.253771e-06,6.253771e-06,0.000000e+00,0.000000e+00,9.452657e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.253771e-06,0.000000e+00,6.253771e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.452657e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [6.198871e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.784921e-06,0.000000e+00,3.099435e-06,3.099435e-06,0.000000e+00,0.000000e+00,3.099435e-06,3.099435e-06,0.000000e+00,6.198871e-06,0.000000e+00,3.099435e-06,3.099435e-06,3.099435e-06,6.784921e-06,0.000000e+00,0.000000e+00,1.298379e-05,0.000000e+00,6.198871e-06,6.198871e-06,3.099435e-06,9.298306e-06,1.298379e-05,1.356984e-05,1.666928e-05,0.000000e+00,1.608323e-05,6.784921e-06,2.035476e-05,9.884357e-06,1.356984e-05,1.976871e-05,9.884357e-06,0.000000e+00,0.000000e+00,0.000000e+00,6.198871e-06,1.298379e-05,3.099435e-06,1.666928e-05,1.298379e-05,3.333856e-05,2.286815e-05,3.643799e-05,3.023912e-05,2.906702e-05,1.918266e-05,3.643799e-05,2.286815e-05,3.023912e-05,6.299162e-05,4.883573e-05,5.193517e-05,4.263686e-05,4.690840e-05,4.632235e-05,4.690840e-05,5.000783e-05,5.620670e-05,5.679275e-05,4.263686e-05,2.538153e-05,4.942178e-05,7.346203e-05,7.111783e-05,6.181952e-05,8.761792e-05,8.954526e-05,7.228993e-05,5.813404e-05,6.299162e-05,6.609106e-05,5.252122e-05,1.099000e-04,8.954526e-05,8.217429e-05,1.401391e-04,6.181952e-05,7.228993e-05,6.491896e-05,7.287598e-05,6.299162e-05,1.087279e-04,8.527372e-05,6.181952e-05,5.872009e-05,7.790275e-05,6.491896e-05,2.596758e-05,6.316081e-05,4.883573e-05,5.503460e-05,2.906702e-05,6.374686e-05,4.087871e-05,4.397815e-05,9.339993e-05,9.474121e-05,8.737024e-05,9.666855e-05,1.022814e-04,1.177785e-04,1.499450e-04,1.958505e-04,2.386565e-04,2.311164e-04,3.018173e-04,3.742764e-04,4.015853e-04,4.697729e-04,4.889556e-04,5.391326e-04,7.857461e-04,7.462087e-04,1.010664e-03,1.051712e-03,1.305110e-03,1.640097e-03,1.704182e-03,2.046370e-03,2.264165e-03,2.661726e-03,2.973597e-03,3.389169e-03,3.469247e-03,4.358265e-03,4.885834e-03,5.408037e-03,6.259953e-03,6.782573e-03,7.865853e-03,8.567993e-03,9.537076e-03,1.067639e-02,1.179166e-02,1.285139e-02,1.399514e-02,1.531679e-02,1.659290e-02,1.794663e-02,1.973327e-02,2.237515e-02,2.419391e-02,2.587601e-02,2.879319e-02,3.059546e-02,3.262018e-02,3.633028e-02,3.692185e-02,3.856882e-02,4.040613e-02,4.207227e-02,4.101395e-02,4.048343e-02,3.885224e-02,3.778262e-02,3.536246e-02,3.256168e-02,2.893976e-02,2.663982e-02,2.254941e-02,1.936903e-02,1.712111e-02,1.399467e-02,1.149170e-02,1.014644e-02,8.720588e-03,7.545703e-03,6.250030e-03,5.340929e-03,4.280216e-03,3.591084e-03,3.566706e-03,2.626949e-03,2.488320e-03,2.179730e-03,1.596474e-03,1.447206e-03,1.245000e-03,1.215764e-03,9.691623e-04,8.368110e-04,6.524460e-04,6.689461e-04,5.270488e-04,4.628851e-04,4.086057e-04,4.140494e-04,4.295466e-04,4.016516e-04,2.998778e-04,2.998778e-04,2.455984e-04,1.876336e-04,1.715504e-04,9.633018e-05,1.382118e-04,1.234699e-04,6.047824e-05,5.427937e-05,9.130341e-05,4.012348e-05,2.035476e-05,3.023912e-05,4.322291e-05,4.070953e-05,2.713968e-05,1.666928e-05,6.784921e-06,3.099435e-06,0.000000e+00,0.000000e+00,0.000000e+00,6.784921e-06,6.784921e-06,3.099435e-06,0.000000e+00,9.884357e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.099435e-06,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_P3_PhlF.png", bbox_inches='tight')
