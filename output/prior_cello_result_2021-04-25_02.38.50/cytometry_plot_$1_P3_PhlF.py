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
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,7.033734e-06,0.000000e+00,0.000000e+00,0.000000e+00,7.033734e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.821112e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,7.033734e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,7.033734e-06,7.033734e-06,0.000000e+00,2.787378e-06,0.000000e+00,0.000000e+00,2.787378e-06,0.000000e+00,7.033734e-06,0.000000e+00,1.406747e-05,7.033734e-06,2.787378e-06,1.964222e-05,5.574757e-06,0.000000e+00,2.787378e-06,9.821112e-06,8.362135e-06,2.787378e-06,5.574757e-06,2.667596e-05,2.388858e-05,2.110120e-05,0.000000e+00,1.406747e-05,1.406747e-05,9.821112e-06,2.110120e-05,2.667596e-05,1.685485e-05,1.114951e-05,2.667596e-05,2.521698e-05,1.818325e-05,5.574757e-06,3.795605e-05,3.928445e-05,2.667596e-05,3.928445e-05,4.061285e-05,2.521698e-05,3.225072e-05,6.038565e-05,5.189294e-05,4.910556e-05,4.485921e-05,3.782547e-05,2.375800e-05,4.061285e-05,2.521698e-05,2.388858e-05,4.910556e-05,4.618761e-05,8.427423e-05,1.053754e-04,6.158348e-05,1.122786e-04,6.874779e-05,3.928445e-05,8.281525e-05,6.874779e-05,9.834170e-05,1.136070e-04,7.710992e-05,9.263637e-05,1.247565e-04,7.020676e-05,8.984899e-05,5.613930e-05,1.137376e-04,5.468032e-05,1.009985e-04,7.856890e-05,4.910556e-05,2.800436e-05,8.706161e-05,1.194429e-04,4.074343e-05,4.074343e-05,3.225072e-05,6.038565e-05,4.777716e-05,2.946334e-05,1.685485e-05,9.821112e-06,4.485921e-05,3.649707e-05,2.787378e-06,2.787378e-06,2.110120e-05,2.110120e-05,5.574757e-06,1.685485e-05,0.000000e+00,3.649707e-05,2.667596e-05,1.818325e-05,1.539587e-05,1.539587e-05,2.521698e-05,5.613930e-05,4.340023e-05,1.818325e-05,3.769490e-05,3.357912e-05,3.769490e-05,8.242352e-05,5.587814e-05,9.901722e-05,1.606007e-04,2.010830e-04,1.744070e-04,2.050682e-04,2.468788e-04,3.918225e-04,4.673429e-04,5.692781e-04,6.416193e-04,8.235824e-04,1.068588e-03,1.107350e-03,1.573081e-03,1.834680e-03,2.230465e-03,2.708520e-03,3.198531e-03,3.954388e-03,4.387454e-03,5.868591e-03,6.739383e-03,8.177318e-03,9.684263e-03,1.093316e-02,1.346788e-02,1.517573e-02,1.781143e-02,2.074897e-02,2.321500e-02,2.698348e-02,3.082316e-02,3.401528e-02,3.699889e-02,4.017538e-02,4.316175e-02,4.642989e-02,4.810208e-02,4.898700e-02,4.933054e-02,4.746661e-02,4.564345e-02,4.226721e-02,3.946262e-02,3.588333e-02,3.153302e-02,2.810526e-02,2.419920e-02,2.120276e-02,1.766949e-02,1.484361e-02,1.255718e-02,9.916440e-03,8.716329e-03,7.613968e-03,6.313380e-03,5.400040e-03,4.839300e-03,3.596310e-03,3.666102e-03,2.865585e-03,2.669685e-03,2.180372e-03,1.811155e-03,1.802532e-03,1.282558e-03,1.144932e-03,1.024160e-03,8.524329e-04,8.876015e-04,7.469268e-04,6.840150e-04,5.925764e-04,5.843449e-04,5.240898e-04,3.806277e-04,2.979431e-04,3.272758e-04,2.879914e-04,1.770412e-04,1.700074e-04,1.136070e-04,1.053754e-04,1.209019e-04,1.166555e-04,1.053754e-04,9.409534e-05,8.148685e-05,5.481090e-05,2.388858e-05,2.110120e-05,2.813494e-05,0.000000e+00,0.000000e+00,1.685485e-05,9.821112e-06,0.000000e+00,2.110120e-05,2.787378e-06,7.033734e-06,0.000000e+00,0.000000e+00,7.033734e-06,0.000000e+00,0.000000e+00,7.033734e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_P3_PhlF.png", bbox_inches='tight')