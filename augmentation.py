import albumentations as A
import argparse
import os
import cv2

parser = argparse.ArgumentParser(description='augmentation')
parser.add_argument('--width', default=256, type=int, help='width of the input image')
parser.add_argument('--height', default=256, type=int, help='height of the input image')
parser.add_argument('--num', default=10, type=int, help='number of augmentation per image')
parser.add_argument('--input', default='input/', type=str, help='input directory that contains images')
parser.add_argument('--output', default='output', type=str, help='input directory that contains images')

args = parser.parse_args()

transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.2, p=0.8),
])

def resize_image(image, weight, height):
    """
        Resize an image to a specific resolution
    """
    return cv2.resize(image, (height,weight))

def augment_image(image):
    """
        Augment an image using albumentations
    """
    return transform(image=image)

def get_images(folder):
    """
    Get all images from a folder
    """
    images = []
    for f in os.listdir(folder):
        images.append(f)
    
    return images

def augment_all_images(folder: list):
    """
        Augments all images from a list of folders
    """
    count = 0
    for file in folder:

        try:
            image = cv2.imread(os.path.join(args.input, file))
        except:
            print(f'Could not load image {os.path.join(args.input, file)}')
            exit()

        h, w, _ = image.shape

        if h != args.height or w != args.width:
            image = resize_image(image, args.width, args.height)

        for i in range(0, args.num):
            aug_image = augment_image(image)['image']
            cv2.imwrite(f'{os.path.join(args.output, file)}_{i}.png', aug_image)
            count += 1

    print(f'Done! Created {count} augmentated images')

def main():

    if not os.path.exists(args.input):
        print('ERROR: INPUT FOLDER DOES NOT EXISTS')
        exit()

    if not os.path.exists(args.output):
        print('ERROR: OUTPUT FOLDER DOES NOT EXISTS')
        exit()

    images = get_images(args.input)

    print(f'Found: {len(images)} images')

    if len(images) == 0:
        print('Folder does not contain images. Empty?')
        exit()

    augment_all_images(images)

if __name__ == '__main__':
    main()