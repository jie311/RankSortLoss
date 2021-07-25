
_base_ = 'ranksort_mask_rcnn_r50_fpn_1x_coco.py'

model = dict(
    neck=dict(
        type='FPN_CARAFE',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=5,
        start_level=0,
        end_level=-1,
        norm_cfg=None,
        act_cfg=None,
        order=('conv', 'norm', 'act'),
        upsample_cfg=dict(
            type='carafe',
            up_kernel=5,
            up_group=1,
            encoder_kernel=3,
            encoder_dilation=1,
            compressed_channels=64)))

optimizer = dict(type='SGD', lr=0.012, momentum=0.9, weight_decay=0.0001)
