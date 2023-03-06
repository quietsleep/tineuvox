_base_ = "./hyper_default.py"

expname = "vrig/base-3dprinter"
basedir = "./logs/vrig_data"

data = dict(
    datadir="data/hypernerf/vrig-3dprinter",
    dataset_type="hyper_dataset",
    white_bkgd=False,
)
