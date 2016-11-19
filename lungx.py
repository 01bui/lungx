import dicom, os, pylab

ds_path = '/home/vbui/LUNGx/DOI/'
for path, subdirs, files in os.walk(ds_path):
    for dir in subdirs:
        print dir
        if dir.startswith("CT-Training-"):
            print dir
            for path, subdirs, files in os.walk(os.path.join(ds_path, dir)):
                for f in files:
                    ds = dicom.read_file(f)
                    instance_number = ds[0x0020, 0x0013].value
                    if instance_number == 70:
                        pylab.imshow(ds.pixel_array, cmap=pylab.cm.gray)
                        pylab.show()