import visbrain
from visbrain.gui import Brain
from visbrain.objects import VolumeObj, CrossSecObj, SourceObj

path='/media/maria/DATA1/Documents/fMRIData/haxby2001/subj2/anat.nii.gz'

vol_obj=VolumeObj(path)

vb=Brain(vol_obj=vol_obj)
vb.show()
