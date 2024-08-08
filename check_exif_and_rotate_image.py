#####################################
# check_exif_and_rotate_image v1.0 2024/08/08
# massimo martinelli  
#####################################

from PIL import Image
import os
import piexif

def rotate_image_based_on_exif(image):
    filename = image.filename
    """Rotate the image based on its EXIF, and return the rotated image and its EXIF."""
    try:
        # Get the EXIF data
        exif_data = image.info.get('exif')
        if exif_data:
            image_exif = Image.Exif()
            image_exif.load(exif_data)
            orientation_tag = 274  #  EXIF orientation tag
            
            if(image_exif.get(orientation_tag,99) == 99):
                print('no orientation tag: ',filename)
            
            # get the orientation
            orientation = image_exif.get(orientation_tag, 1)
            
            # rotate the image based on the orientation tag
            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(-90, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)
            
            # Reset the orientation tag to 1 (normal orientation)
            image_exif[orientation_tag] = 1
            exif_bytes = image_exif.tobytes()
            return image, exif_bytes
        else:
            return image, None
    except Exception as e:
        #print(f"Error processing EXIF data: {e}")
        print('wrong exif :',filename)
        return image, None

def check_dir(image_dir):
    print('\n********* ',image_dir)
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):  # or filename.endswith('.png'):
            # load the image
            image_path = os.path.join(image_dir, filename)
            try:
                image = Image.open(image_path)
            except Exception as e:
                    print('error reading the image:',filename)
                    return image, None
            
            # Rotate the image based on its orientation EXIF
            image, exif_bytes = rotate_image_based_on_exif(image)

            # Save the rotated image
            if exif_bytes:
                image.save(image_path, exif=exif_bytes)
            else:
                # save the image without EXIF
                try:
                    image.save(image_path)
                    print('saved without exif:',filename)
                except Exception as e:
                    print('error writing the imagw:',filename)
                    return image, None
                



# specify the directories containing the images
image_dirs =['dir1','dir2','dir3']


for image_dir in image_dirs:
    check_dir(image_dir)
