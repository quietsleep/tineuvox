_base_ = "./default.py"

expname = "base/dnerf_jumpingjacks-400"
basedir = "./logs/nerf_synthetic"

data = dict(
    datadir="data/dnerf/jumpingjacks",
    dataset_type="dnerf",
    white_bkgd=True,
)
