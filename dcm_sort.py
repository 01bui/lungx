import dicom, os
import numpy as np

def dcm_sort(dcm_path):
    for f in os.listdir(dcm_path):
        # Read the first dicom to get the image size
        dcm_file = dicom.read_file(os.path.join(dcm_path, f))
        row = dcm_file[0x0028, 0x0010].value
        col = dcm_file[0x0028, 0x0011].value
        break

    image_files = os.listdir(dcm_path)
    dataset = np.ndarray(shape=(len(image_files), row, col), dtype=np.float32)

    # Sort the dicoms and assign it to numpy array
    for f in os.listdir(dcm_path):
        dcm_file = dicom.read_file(os.path.join(dcm_path, f))
        image_number = dcm_file[0x0020, 0x0013].value
        dcm_pixel_data = dcm_file.pixel_array.astype(float) / np.max(dcm_file.pixel_array)
        dataset[image_number - 1, :, :] = dcm_pixel_data

    return dataset


