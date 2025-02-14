from datasets import load_dataset

ds = load_dataset("big_patent")  # default is 'all' CPC codes
ds = load_dataset("big_patent", "all")  # the same as above
ds = load_dataset("big_patent", "a")  # only 'a' CPC codes
ds = load_dataset("big_patent", codes=["a", "b"])
