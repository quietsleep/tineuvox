_base_ = "./default.py"

expname = "small/dnerf_lego-400"
basedir = "./logs/nerf_synthetic"

data = dict(
    datadir="data/dnerf/lego",
    dataset_type="dnerf",
    white_bkgd=True,
)
