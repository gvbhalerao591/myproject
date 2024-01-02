import os
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib.image

def show_slices(slices):
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
         axes[i].imshow(slice.T, cmap="gray", origin="lower")
            
def nii2png(img):
    dirname = os.path.dirname(img)
    os.chdir(dirname)
    imgname = os.path.basename(img)
    img = nib.load(imgname)
    slice_0 = img.get_fdata()[int(img.shape[0]/2),:,:]
    slice_1 = img.get_fdata()[:,int(img.shape[1]/2),:]
    slice_2 = img.get_fdata()[:,:,int(img.shape[2]/2)]
    show_slices([slice_0, slice_1, slice_2])
    matplotlib.image.imsave(os.path.join(dirname,'sagittal_2D.png'), slice_0)
    matplotlib.image.imsave(os.path.join(dirname,'coronal_2D.png'), slice_1)
    matplotlib.image.imsave(os.path.join(dirname,'transverse_2D.png'), slice_2)
