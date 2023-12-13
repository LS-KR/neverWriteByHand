# neverWriteByHand
## Usage

1. put font file and background file into `/src/`
2. set up arguments:
    ``` python
    size = 2  # Chaos
    txt_path = './source.txt'  # Text File
    ttf_path = "src/writeup.TTF"  # Font
    save_path = "./result/"  # storage folder
    white = False  # If True, a white background is generated
    fill = (0, 0, 96, 255)  # Color (RGBA)
    ```
    - `size`: Positive Number, Set the random offset of each character on the paper.
    - `txt_path`: The path of the txt file.
    - `ttf_path`: Font file path (TTF only).
    - `save_path`: Generated image would save into this path. Should be a directory.
    - `while`: If this param set as `True`, a white background-ed image would generated; else, a default background.
    - `fill`: The stroke color(RGBA) of character. If you want black stroke, use `(0, 0, 0, 255)`.


# Result
![img](./img/test.jpg)
