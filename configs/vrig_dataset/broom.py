_base_ = "./hyper_default.py"

expname = "vrig/base-broom"
basedir = "./logs/vrig_data"

data = dict(
    datadir="data/nerfies/broom",
    dataset_type="hyper_dataset",
    white_bkgd=False,
)
