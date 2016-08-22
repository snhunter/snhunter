# snhunter
Usage: `python snh.py test-image.jpg`

snh.py expects input image as argument and writes result to `{basename}_gamma_(gs|cm).jpg`

Further information: [Supernova Hunters Talk](https://www.zooniverse.org/projects/dwright04/supernova-hunters/talk/478/80831)

## Sample Images
snh.py applies gamma correction to the linear images from Supernova Hunters. Using a perceptually uniform colormap it further facilitates supernova classification.

![Original Image from Supernova Hunters](https://github.com/snhunter/snhunter/blob/master/test-image.jpg)
![Enhanced Image, grayscale](https://github.com/snhunter/snhunter/blob/master/test-image_gamma_gs.jpg)
![Enhanced Image, colormap](https://github.com/snhunter/snhunter/blob/master/test-image_gamma_cm.jpg)

Note: Images should be viewed against dark background
