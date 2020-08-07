import nibabel as nib
import numpy as np
import h5py

data_list = [10001, 10005, 10009, 10017, 10031, 20001, 20003, 20005, 20020, 20201]

for ind in data_list:

    h5_file = h5py.File('/iacl/pg20/shangxian/Thalamus/training_TBI/h5/{}_left.h5'.format(inv), 'w')

    fa = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_left_01_FA_ref.nii.gz".format(inv)).get_fdata()
    fa = np.swapaxes(fa, 2, 0, 1)

    edge = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_left_01_edgemap.nii.gz".format(inv)).get_fdata()
    edge = np.swapaxes(edge, 2, 0, 1)

    mp = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_left_01_MPRAGEPre.nii.gz".format(inv)).get_fdata()
    mp = np.swapaxes(mp, 2, 0, 1)

    t2 = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_left_01_T2.nii.gz".format(inv)).get_fdata()
    t2 = np.swapaxes(t2, 2, 0, 1)

    label = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_left_01_mask.nii.gz".format(inv)).get_fdata()
    label = np.swapaxes(label, 2, 0, 1)

    data_x = np([fa, edge, mp, t2])
    h5_file.create_dataset('raw', data=data_x, compression='gzip', compression_opts=4, dtype='uint8')
    h5_file.create_dataset('label', data=label, compression='gzip', compression_opts=1, dtype='uint8')
    h5_file.close()

    h5_file = h5py.File('/iacl/pg20/shangxian/Thalamus/training_TBI/h5/{}_right.h5'.format(inv), 'w')

    fa = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_right_01_FA.nii.gz".format(inv)).get_fdata()
    fa = np.swapaxes(fa, 2, 0, 1)

    edge = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_right_01_edgemap.nii.gz".format(inv)).get_fdata()
    edge = np.swapaxes(edge, 2, 0, 1)

    mp = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_right_01_MPRAGEPre.nii.gz".format(inv)).get_fdata()
    mp = np.swapaxes(mp, 2, 0, 1)

    t2 = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_right_01_T2.nii.gz".format(inv)).get_fdata()
    t2 = np.swapaxes(t2, 2, 0, 1)

    label = nib.load("/iacl/pg20/shangxian/Thalamus/training_TBI/{}_right_01_mask.nii.gz".format(inv)).get_fdata()
    label = np.swapaxes(label, 2, 0, 1)

    data_x = np([fa, edge, mp, t2])
    h5_file.create_dataset('raw', data=data_x, compression='gzip', compression_opts=4, dtype='uint8')
    h5_file.create_dataset('label', data=label, compression='gzip', compression_opts=1, dtype='uint8')
    h5_file.close()