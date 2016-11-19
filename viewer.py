import dicom, os
import matplotlib.pyplot as plt

ds_path = '/home/vbui/LUNGx/DOI/'
for path, subdirs, files in os.walk(ds_path):
    for dir in subdirs:
        if dir.startswith("CT-Training-"):
            print dir
            for p, s, dicoms in os.walk(os.path.join(ds_path, dir)):
                for f in dicoms:
                    ds = dicom.read_file(os.path.join(p, f))
                    instance_number = ds[0x0020, 0x0013].value
                    if dir == 'CT-Training-LC001' and instance_number == 135:
                        plt.plot(120, 325, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-LC002' and instance_number == 70:
                        plt.plot(139, 359, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-LC003' and instance_number == 70:
                        plt.plot(375, 323, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-LC008' and instance_number == 65:
                        plt.plot(95, 328, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-LC009' and instance_number == 63:
                        plt.plot(145, 299, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-BE001' and instance_number == 169:
                        plt.plot(405, 296, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-BE002' and instance_number == 117:
                        plt.plot(184, 268, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-BE006' and instance_number == 241:
                        plt.plot(449, 266, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-BE007' and instance_number == 194:
                        plt.plot(385, 206, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
                    elif dir == 'CT-Training-BE010' and instance_number == 69:
                        plt.plot(120, 336, 'ro')
                        plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                        plt.show()
