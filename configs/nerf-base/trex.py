_base_ = "./default.py"

expname = "base/dnerf_trex-400"
basedir = "./logs/nerf_synthetic"

data = dict(
    datadir="data/dnerf/trex",
    dataset_type="dnerf",
    white_bkgd=True,
)
