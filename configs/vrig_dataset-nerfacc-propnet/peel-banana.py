_base_ = "./hyper_default.py"

expname = "vrig/base-peel-banana-nerfacc-propnet"
basedir = "./logs/vrig_data"

data = dict(
    datadir="./vrig-peel-banana",
    dataset_type="hyper_dataset",
    white_bkgd=False,
)

model_and_render = dict(
    voxel_factor_per_prop=[2.0],
    voxel_dim_factor_per_prop=[1.5],
    defor_depth_factor_per_prop=[1.5],
    net_width_factor_per_prop=[2.0],
    num_samples_per_prop=[128],
    num_samples=64,
    opaque_bkgd=True,
    sampling_type="uniform",
)
