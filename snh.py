import sys
import scipy.misc
from matplotlib import cm
from PIL import Image


#Parse command line arguments
filename = sys.argv[1]
basename = filename.split('.')


#Read input image
im = scipy.misc.imread(filename, flatten=True)

#Read crosshair overlay
overlay = Image.open("crosshair.png")


#Apply gamma correction to linear image data from PANSTARRS
im = (im/255.)**(2.2)

#Apply perceptually uniform (CAM02UCS color space) and colorblindness-friendly colormap
#See https://bids.github.io/colormap/images/screenshots/option_a.png
#Change magma to gray for grayscale colormap
im = Image.fromarray(cm.magma(im, bytes=True))

#Merge background with overlay
im = Image.alpha_composite(im, overlay)

#Save final result
im.save(basename[0] + "_gamma.jpg", quality=93, optimize=True, progressive=True)
