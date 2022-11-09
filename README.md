# augmentation
convert a small dataset of images into large augmented dataset
## Arguments
```
--width (int) width of the output image (default:256)
--height (int) height of the output image (default:256)
--num (int) number of augmentation per image (default:10)
--input (str) input images directory (default:input/)
--output (str) output images directory (default:output/)
```
## Example
```
python augmentation.py --input 'images/' --output 'output/' --num 5 
```
