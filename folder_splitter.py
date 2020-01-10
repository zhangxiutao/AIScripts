import split_folders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
split_folders.ratio("E:\\Binary-Image-Classifier-PyTorch-master\\face", output="E:\\Binary-Image-Classifier-PyTorch-master\\splitted", seed=1337, ratio=(.6, .2, .2)) # default values

# Split val/test with a fixed number of items e.g. 100 for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
#split_folders.fixed('input_folder', output="output", seed=1337, fixed=(100, 100), oversample=False) # default values