from api import remove_watermark

remove_watermark(
    image_path = "wm.png",
    mask_path = "C:\Users\{}\Downloads\mask.jpeg",
    max_dim = 2,
    show_step = 1,
    reg_noise = 5,
    input_depth = 2048,
    lr = 1000,
    training_steps = 20000,
    tqdm_length = 900
)
