# Deduplicate Images 

This script uses [ImageHash](https://github.com/jenssegers/imagehash) to generate a hash for each image in the folder defined.

Then it calculates hash-distance between images.

Thereshold is set looking at distances between images to find similar images.

Takes about **2.3 seconds to classify 12 images**.


# Requirements:

```
ImageHash==3.4
matplotlib==2.0.2
scipy==0.19.1
Pillow==5.0.0
```

# Similar Images:

## Set 1:

![Image](images/10_.jpg) 
![Image](images/11_.jpg)
![Image](images/12_.jpg) 
![Image](images/9_.jpg)

## Set 2:

![Image](images/4_.jpg) 
![Image](images/5_.jpg)
![Image](images/6_.jpg) 
![Image](images/7_.jpg)
![Image](images/8_.jpg)

## Set 3:

![Image](images/1_.jpg) 
![Image](images/2_.jpg)
![Image](images/3_.jpg) 
