"""
In this file, we'll practice working with byte files.

"""

with open("./sample_data/dog.jpg", "rb") as img_file:
    print(img_file.readline())
