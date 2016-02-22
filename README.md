The first face for IQAE using shiny and image maps to create an interactive segmentation which can be used to specify the parameters and criteria for analyzing large datasets.

## List images

```
http://86.119.33.242:5000/slic_generator/list_images
```

### Output

```json
{
  "images": [
    "17426326746_78a4081eb9_o.jpg",
    "L15-0333E-1260N-mini-small.png",
    "L15-0333E-1260N-mini.png"
  ]
}
```

## Grab the image as a data-url

```
http://86.119.33.242:5000/slic_generator/grab_image/L15-0333E-1260N-mini-small.png
```

### Output

```
{"data_url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAkAAAHMCAIAAAA4eGZ2AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAAAsTAAALEwEAmpwYAAAB1WlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOkNvbXByZXNzaW"}
```

## Calculate Super-pixels

### Format

- http://86.119.33.242:5000/slic_generator/create_slic/__image name__/__segment-size__

### Example

```
http://86.119.33.242:5000/slic_generator/create_slic/L15-0333E-1260N-mini-small.png/1000
```

### Output
Important field is areas and the sub-field path which contains a list of polygon vertices

```json
{"areas": [{"perimeter": 4388.147520065308, "avg_color": [106.66390514399612, 133.49106380803926, 144.69115069123245], "name": "region-0", "area": 195665, "color_name": "slategray", "path": [[[1, 1]], [[1, 300]], [[2, 301]]
```