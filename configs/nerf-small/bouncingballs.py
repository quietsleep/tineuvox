_base_ = "./default.py"

expname = "small/dnerf_bouncingballs-400"
basedir = "./logs/nerf_synthetic"

data = dict(
    datadir="data/dnerf/bouncingballs",
    dataset_type="dnerf",
    white_bkgd=True,
)
