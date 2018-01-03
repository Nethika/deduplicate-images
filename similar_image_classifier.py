"""
Nethika Suraweera
TinMan Kinetics
01/02/2018


This script uses ImageHash to generate a hash for each image in the folder defined.
Then it calculates the distance between images.
Thereshold is set looking at distances between images to find similar images.

"""

import scipy
from scipy import spatial
from pathlib import Path
from PIL import Image
import imagehash
import itertools
import scipy.io
import scipy.misc
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

#%matplotlib inline   #To show images in Jupyter Notebook

"""
To show images in Jupyter Notebook
"""
def show_image(img_path):
    content_image = scipy.misc.imread(img_path)
    imshow(content_image)
    return

"""
To calculate distance between hash
"""
def distance(x,y):
    return x-y

"""
To find the connected images
"""
def connected_tuples(pairs):
    # for every element, we keep a reference to the list it belongs to
    lists_by_element = {}
 
    def make_new_list_for(x, y):
        lists_by_element[x] = lists_by_element[y] = [x, y]
 
    def add_element_to_list(lst, el):
        lst.append(el)
        lists_by_element[el] = lst
 
    def merge_lists(lst1, lst2):
        merged_list = lst1 + lst2
        for el in merged_list:
            lists_by_element[el] = merged_list
 
    for x, y in pairs:
        xList = lists_by_element.get(x)
        yList = lists_by_element.get(y)
 
        if not xList and not yList:
            make_new_list_for(x, y)
 
        if xList and not yList:
            add_element_to_list(xList, y)
 
        if yList and not xList:
            add_element_to_list(yList, x)            
 
        if xList and yList and xList != yList:
            merge_lists(xList, yList)
 
    # return the unique lists present in the dictionary
    return set(tuple(l) for l in lists_by_element.values())

if  __name__ == '__main__':

    # Define the location of images
    directory_in_str = "images"
    pathlist = Path(directory_in_str).glob('**/*.jpg')

    # Set the threshold
    threshold = 23    # decided looking at the distances between image pairs.

    # Create hash
    hash_dict={}
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        hash_ = imagehash.average_hash(Image.open(path_in_str))
        hash_dict[path_in_str] = hash_

    #Calculate distances between images
    img_list=list(hash_dict.keys())
    dist_pairs=[]

    for pair in itertools.combinations(img_list, r=2):
        (a,b) = pair
        x = hash_dict[a]
        y = hash_dict[b]
        dist = distance (x,y)
        if dist < threshold :
            dist_pairs.append(pair)

    #find simillar images
    print (connected_tuples(dist_pairs))

    """
    # Show pictures in Jupyter Notebook
    # need to fix: imshow doesn't show every image in a loop.
    for img in img_list:
        print(img)
        show_image(img)
    """