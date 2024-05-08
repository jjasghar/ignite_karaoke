import os
import random



def get_random_image_files():
    random.sample(os.listdir('imgs/'), 4)
