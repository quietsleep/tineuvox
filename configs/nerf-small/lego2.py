_base_ = "./default.py"

expname = "small/dnerf_lego-400_2"
basedir = "./logs/nerf_synthetic"

model_and_render = dict(
    occ_grid_reso=128,
    occ_ema_decay=0.99,
)
data = dict(
    datadir="data/dnerf/lego",
    dataset_type="dnerf",
    white_bkgd=True,
    aabb=(-1.3, -1.3, -1.3, 1.3, 1.3, 1.3),
)
