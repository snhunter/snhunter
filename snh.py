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
overlaycolor = Image.open("crosshaircolor.png")


#Apply gamma correction to linear image data from PANSTARRS
im = (im/255.)**(2.2)

#Apply perceptually uniform (CAM02UCS color space) and colorblindness-friendly colormap
#See https://bids.github.io/colormap/images/screenshots/option_a.png
#Generate grayscale version
imcm = Image.fromarray(cm.magma(im, bytes=True))
imgs = Image.fromarray(cm.gray(im, bytes=True))

#Merge background with overlay
imcm = Image.alpha_composite(imcm, overlay)
imgs = Image.alpha_composite(imgs, overlaycolor)

#Save final results
imcm.save(basename[0] + "_gamma_cm.jpg", subsampling="4:4:4", quality=89, optimize=True, progressive=True)
imgs.save(basename[0] + "_gamma_gs.jpg", subsampling="4:4:4", quality=89, optimize=True, progressive=True)
