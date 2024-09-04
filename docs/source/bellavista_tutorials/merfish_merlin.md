MERFISH - MERlin
================

```{eval-rst}
.. note::

   WORK IN PROGRESS...
   FIX EXAMPLE JSON STUFF
```


This tutorial is for visualizing datasets from custom (home-built) MERFISH setups processed via the [MERlin](https://github.com/emanuega/MERlin) pipeline. Our aim was to make the Bella Vista package as lightweight as possible and make it easy for users to customize the code for custom setups, analyses, and needs. Check out the [napari website](https://napari.org/) for further documentation and features you can implement!

## MERlin pipeline outputs

Standard MERlin outputs folder organization:
```{eval-rst}
.. code-block:: 

  %ANALYSIS_HOME%
  ├── ...
  ├── ExportBarcodes
  │   └── barcodes.csv
  ├── ...
  ├── FiducialCorrelationWarp
  │   └── images
  │       └── aligned_images0.tif
          └── ...
          └── aligned_images406.tif
  ├── ...
  ├── RefineCellDatabases
  │   └── features
  │       └── feature_data_0.hdf5
          └── ...
          └── feature_data_406.tif
  ├── ...
  ├── codebook.csv
  ├── microscope_parameters.json
  └── positions.csv
```

From these outputs, it is possible to visualize tissue images, spatial transcript locations, and cell/nuclear segmentation boundaries.

To visualize tissue images, individual field-of-views (FOVs) must be stitched together. FOV images can be found in the `FiducialCorrelationWarp/Images` folder. Currently, Bella Vista does not include a stitching pipeline. Stitching can be accomplished using image processing utilizing python packages such as [NumPy](https://numpy.org/) and [Dask](https://www.dask.org/) or softwares such as [BigStitcher](https://imagej.net/plugins/bigstitcher/). The output stitched image must be a TIFF image, with individually stitched images for each channel you wish to visualize. The stitched images should be saved in the `%ANALYSIS_HOME%` directory.

Transcript locations and cell/nuclear segmentations exported by MERlin can be processed directly by Bella Vista.

In order to visualize your MERFISH dataset in Bella Vista, you will need to create a dataset-specific JSON configuration file containing paths to the MERlin outputs for your dataset. These output files will be processed to generate visualization files for Bella Vista. Creating these visualization files will take a few minutes but only need to be created once. For subsequent runs, `create_inputs` can be set to `False`.

## Configuration JSON file structure

```{eval-rst}
.. code-block:: JSON

    { 
        "system": "merlin", 
        "data_folder": "/path/to/merlin_outs",
        "bella_vista_output_folder": "/path/to/merlin_outs/bellavista_outs",
        "create_bellavista_inputs": true,

        "visualization_parameters": {
            "plot_image": true,
            "plot_transcripts": true,
            "plot_allgenes": true,
            "plot_cell_seg": true
        },

        "input_files": {
                "transcript_filename": "ExportBarcodes/barcodes.csv",
                "codebook": "codebook.csv",
                "images": "DAPI_z3.tif",
                "microscope_parameters": "microscope_parameters.json",
                "positions_list": "positions.csv",
                "z_plane": 3,
                "cell_segmentation": "RefineCellDatabases/features"
        }
    }
```

## Input file parameters (MERlin)

**transcript_filename**: *string*
: relative path to CSV file containing decoded gene transcript spatial coordinates. If None, no transcripts will be plotted

**codebook**: *string*
: relative path to CSV containing map from `barcode_id` to gene ID. This is *required* to plot transcripts. If None, no transcripts will be plotted

**images**: *string or 1D array of strings, default=None*
: relative path to stitched image(s) to display. If None, no images will be displayed. Images must be an OME-TIFF or TIFF file. If an image file is 3D (z,y,x) format, the image used will be from the `z_plane` index. If the specified `z_plane` does not exist, the first image in the stack will be used 

**microscope_parameters**: *string*
: relative path to JSON file containing microscope micron to pixel transform. This is *required* if displaying images. If None, no images will be displayed

**positions_list**: *string*
: relative path to CSV file containing micron microscope positions for each FOV. This is *required* if displaying images. If None, no images will be displayed

**z_plane**: *integer, default=0*
: z-plane to plot segmented cell/nuclear boundaries from

**cell_segmentation**: *string, default=None*
: relative path to folder containing HDF5 cell segmentation boundaries. If None, no boundaries will be plotted

**nuclear_segmentation**: *string, default=None*
: relative path to folder containing HDF5 nuclear segmentation boundaries. If None, no boundaries will be plotted

```{eval-rst}
.. note::

  All input file paths **must** be relative paths to :samp:`data_folder`
  
    If you are missing some input files, remove those input file parameters from the JSON file. Bella Vista will skip the visualization of these data.

    For example, if you do not have cell segmentations, the input file parameters in your JSON file might look like this: 

    .. code-block:: JSON

            "input_files": {
                "transcript_filename": "barcodes.csv",
                "codebook": "codebook.csv",
                "images": "DAPI.tif",
                "microscope_parameters": "microscope_parameters.json",
                "positions_list": "positions.csv"
            }
```
## General parameters

**system**: *string*
: Value: `"merlin"`\
 The input is not case-sensitive, so values "merlin", "MERlin", and "MERLIN" are treated equivalently

**data_folder**: *string*
: Path to folder containing dataset output files
  
**bella_vista_output_folder**: *string*
: Path to save & load Bella Vista visualization files
  
**create_bellavista_inputs**: *boolean, default=true*
: Create required visualization files for Bella Vista. Must be `true` when first loading data.\
 Can be `false` in subsequent runs (since files have already been created)

## Visualization parameters

**plot_image**: *boolean, default=False*
: Display image(s). Default value is False

**plot_transcripts**: *boolean, default=False*
: Plot gene transcript spatial coordinates

**plot_allgenes**: *boolean, default=True*
: Plot transcripts for all gene IDs. If False, only gene IDs in `selected_genes` will be plotted

**selected_genes**: *1D array of strings, default=None*
: Plot transcripts only for specified gene IDs

**plot_cell_seg**: *boolean, default=False*
: Plot cell segmentation

**plot_nuclear_seg**: *boolean, default=False*
: Plot nuclear segmentation

**transcript_point_size**: *float, default=1.0*
: Point size for plotting transcript coordinates

**contrast_limits**: *tuple array of integers, default=None*
: Values in the range [0, 65535]. Contrast limits for displayed image(s)

**rotate_angle**: *integer, default=None*
: Value in the range [0, 360]. Angle in degrees by which to rotate the data

<br><br>
<hr class="custom-line">

## Sample dataset & JSON

For this example, we processed the first FOV from a MERFISH sample dataset from the Brain Image Library [@Zhuang2020] via MERlin.

Download MERlin processed MERFISH mouse primary motor cortex dataset (mouse 2, sample 4, FOV 0) from [dropbox](https://www.dropbox.com/scl/fo/8km4m5wcj5a95ezfqyz7o/AOonVJDDv9GdzwdD-4_7NcU?rlkey=hcruoy48tzveyewkw1z2fya5t).

### Load Bella Vista

1. In the folder downloaded from dropbox, open `merlin_sample.json`
2. Replace the paths in `data_folder` and `bella_vista_output_folder`
<br><br>

**merlin_sample.json**
```{eval-rst}
.. code-block:: JSON 
  :emphasize-lines: 3-4

  { 
      "system": "merlin", 
      "data_folder": "/path/to/merlin_outs",
      "bella_vista_output_folder": "/path/to/merlin_outs/bellavista_outs",
      "create_bellavista_inputs": true,

      "parameters": { 
          "plot_image": true,
          "plot_transcripts": true,
          "plot_allgenes": true
          "plot_cell_seg": true,
          "transcript_point_size": 0.75
      },

      "input_files": {
          "microscope_parameters": "microscope_parameters.json",
          "codebook": "codebook.csv",
          "positions_list": "positions.csv",
          "images": "polyT_z3.tif",
          "z_plane": 3,
          "transcript_filename": "ExportBarcodes/barcodes.csv",
          "cell_segmentation": "RefineCellDatabases/features"
      }
  }
```

3. In the terminal, run Bella Vista with the MERlin sample JSON:

```{eval-rst}
.. code-block:: python

  bellavista merlin_sample.json
```

```{eval-rst}
.. note::

    It will take a few minutes to create the required data files. The terminal will print updates & have progress bars for time consuming steps.
```

Using this JSON file, the displayed output should look similar to this: 

<img src="../_static/tutorials/merlin/merlin_position0.png" alt="MERlin brain initial view" />

```{eval-rst}
.. note::

    Gene colors are assigned randomly every time Bella Vista is launched. So, the gene colors displayed in your window will be different from the image above. See :ref:`useful-napari-commands` in the FAQ for commands to configure gene colors and other customizable visualization options. 
    
    To reproduce the same colors every time you launch Bella Vista, see :ref:`creating-figures` in the Figure Guide.
```

Try zooming in & out, toggling gene and cell segmentation layers on & off:

<img src="../_static/tutorials/merlin/merlin_subset.png" alt="MERlin brain layer subset" />

### References

[@Zhuang2020]: Zhuang, Xiaowei, Zhang, Meng. (2020). A molecularly defined and spatially resolved cell atlas of the mouse primary motor cortex. [ Collection / Dataset ]. Brain Image Library. https://doi.org/10.35077/g.21

## Visualizing your MERFISH dataset

Steps to visualize your dataset:

1. Stitch FOVs into a single TIF image (optional)
2. Create and configure a JSON file for your dataset, ensuring all input file paths are relative to `data_folder`. Once this JSON file has been created, it can be reused every time you launch Bella Vista for this dataset.
3. Run Bella Vista with your configured JSON
4. Explore your data!

If you encounter any issues, please check the [FAQ](../faq.md#frequently-asked-questions). If you're experiencing issues not addressed in the FAQ, please check the open issues or [open a new issue](https://github.com/pkosurilab/BellaVista/issues)in our GitHub repository. You can also leave any feedback here!

<div class="flex justify-between items-center pt-6 mt-12 border-t border-border gap-4">
    <div class="mr-auto">
      <a href="../tutorials.html" class="inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors border border-input hover:bg-accent hover:text-accent-foreground py-2 px-4" style="text-decoration: none;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2 h-4 w-4">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        Tutorials
      </a>
    </div>
  <div class="ml-auto">
    <a href="../figure_guide.html" class="inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors border border-input hover:bg-accent hover:text-accent-foreground py-2 px-4" style="text-decoration: none;">
      Figure Guide
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="ml-2 h-4 w-4">
        <polyline points="9 18 15 12 9 6"></polyline>
      </svg>
    </a>
  </div>
</div>