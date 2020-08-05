import h5py
filename = "Movie1_t00000_crop_gt.h5"

with h5py.File(filename, "r") as f:
    # List all groups
    print(type(f))
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[1]
    print(a_group_key)

    # Get the data
    data = list(f[a_group_key])
    print(type(f[a_group_key]))
    print(len(data))
    print(data[0].shape)

