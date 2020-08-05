import nibabel as nib
import numpy as np
import h5py



h5_file = h5py.File('./t1.h5', 'w')
# bogus data with the correct size
data_x = nib.load("./nii/patient001_t1.nii.gz").get_fdata()
label = nib.load("./nii/patient001_seg.nii.gz").get_fdata()
#
h5_file.create_dataset('raw', data=data_x, compression='gzip', compression_opts=4, dtype='uint8')
h5_file.create_dataset('label', data=label, compression='gzip', compression_opts=1, dtype='uint8')
h5_file.close()

h5_file = h5py.File('./t2.h5', 'w')
# bogus data with the correct size
data_x = nib.load("./nii/patient001_t2.nii.gz").get_fdata()
label = nib.load("./nii/patient001_seg.nii.gz").get_fdata()
#
h5_file.create_dataset('raw', data=data_x, compression='gzip', compression_opts=4, dtype='uint8')
h5_file.create_dataset('label', data=label, compression='gzip', compression_opts=1, dtype='uint8')
h5_file.close()

h5_file = h5py.File('./flair.h5', 'w')
# bogus data with the correct size
data_x = nib.load("./nii/patient001_flair.nii.gz").get_fdata()
label = nib.load("./nii/patient001_seg.nii.gz").get_fdata()
#
h5_file.create_dataset('raw', data=data_x, compression='gzip', compression_opts=4, dtype='uint8')
h5_file.create_dataset('label', data=label, compression='gzip', compression_opts=1, dtype='uint8')
h5_file.close()

h5_file = h5py.File('./t1ce.h5', 'w')
# bogus data with the correct size
data_x = nib.load("./nii/patient001_t1ce.nii.gz").get_fdata()
label = nib.load("./nii/patient001_seg.nii.gz").get_fdata()
#
h5_file.create_dataset('raw', data=data_x, compression='gzip', compression_opts=4, dtype='uint8')
h5_file.create_dataset('label', data=label, compression='gzip', compression_opts=1, dtype='uint8')
h5_file.close()