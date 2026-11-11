from matplotlib import pyplot as plt
import os
from PIL import Image
import warnings
from dotenv import load_dotenv

load_dotenv()


# Suppress all warnings
warnings.filterwarnings("ignore")
from datasets import load_dataset

ds = load_dataset("huggan/flowers-102-categories")

# # # show number or rows
print(ds.num_rows)

# # # get an image from the dataset
# flower = ds["train"][78]["image"]
# # Display the image using matplotlib
# plt.imshow(flower)
# plt.axis("off")
# plt.show()S