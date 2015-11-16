import numpy as np
import scipy.io as io
import h5py

lines = io.loadmat('calcofi_lines.mat')

fno = 'calcofi_lines.h5'

h5file = h5py.File(fno, 'w')

# line 93 (southern most)
h5file.create_dataset("line93/lon", data=np.array([-123.59, -122.92, -122.26,
                                          -121.59, -120.92, -120.25, -119.57,
                                          -119.23, -118.89, -118.56, -118.21, 
                                          -117.87, -117.53, -117.4 ]))

h5file.create_dataset("line93/lat", data=np.array([29.85,  30.18,  30.51,  30.85,
                                                   31.18,  31.51,  31.85,  32.01,
                                                   32.18,  32.35,  32.51,  32.68,
                                                   32.85,  32.91]))

h5file.create_dataset("line93/station", data=np.array([120, 110, 100,  90,  80,  70,
                                                       60,  55,  50,  45,  40,  35,  
                                                       30, 28]))

h5file.create_dataset("line93/p", data=np.array([0.49459812,  90.98188469]))


# line 90
h5file.create_dataset("line90/lon", data=np.array([-124.  , -123.33, -122.66, -121.99,
                                                   -121.32, -120.64, -119.96, -119.48,
                                                   -118.94, -118.39, -118.25, -117.91,
                                                   -117.77 ]))

h5file.create_dataset("line90/lat", data=np.array([30.42,  30.75,  31.09,  31.42,  31.75,
                                                   32.09,  32.42,  32.65,  32.92,  33.19,  
                                                   33.25,  33.42,  33.49]))

h5file.create_dataset("line90/stations", data=([120, 110, 100,  90,  80,  70,  60,  53,  45, 
                                                37,  35,  30,  28]))

h5file.create_dataset("line90/p", data=np.array([0.49215733,  91.45454184]))


h5file.close()
