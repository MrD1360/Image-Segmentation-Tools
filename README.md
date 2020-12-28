# Image-Segmentation-Tools

This repository aims at providing helpful scripts for image segmentation. In particular, for what concerns image annotation and dataset preparation.


So far the scripts in this repository are:

- Jupyter notebook for mask refinement: in some cases it can be difficult to manually annotate/label the dataset. So it can be useful to have a tool that defines the mask pixel to pixel after having manually and roughly annotate them.

- python scripts json to maks: as easily inferrable from the name this script creates binary masks from the JSON file that describes our annotations. In particular, this script is specially made for an open source annotator tool: https://www.robots.ox.ac.uk/~vgg/software/via/
