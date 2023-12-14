# neverWriteByHand

## Usage

1. put font file and background file into `/src/`
2. set up configs:
    ``` ini
    [DEFAULT]
    size = 4
    txt_path = ./source.txt
    ttf_path = ./src/writeup.TTF
    save_path = ./result/
    white = 0
    fill = #000060FF
    ```
    - `size`: Positive Number, Set the random offset of each character on the paper.
    - `txt_path`: The path of the txt file.
    - `ttf_path`: Font file path (TTF only).
    - `save_path`: Generated image would save into this path. Should be a directory.
    - `while`: If this param set as `True`, a white background-ed image would generated; else, a default background.
    - `fill`: The stroke color(RGBA) of character.

# Result

![img1](./img/1.png)
![img2](./img/2.png)
