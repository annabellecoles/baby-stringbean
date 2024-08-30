MERFISH - MERlin
================

This in-depth tutorial is for visualizing datasets from custom (home-built) MERFISH setups processed via the [MERlin](https://github.com/emanuega/MERlin) pipeline. Our aim was to make the Bella Vista package as lightweight as possible and make it easy for users to customize the code for custom setups, analyses, and needs. Check out the [napari website](https://napari.org/) for further documentation and features you can implement!


### MERlin pipeline outputs

Standard MERlin output file organization:
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

To visualize tissue images, individual field-of-views (FOVs) must be stitched together. Currently Bella Vista does not include a stitching pipeline. Stitching can be accomplished using image processing utilizing python packages such as [NumPy](https://numpy.org/) and [Dask](https://www.dask.org/) or software such as [BigStitcher](https://imagej.net/plugins/bigstitcher/) 

FOV images can be found in the `FiducialCorrelationWarp/Images` folder. The output stitched image must be a TIFF image, with individual images for each channel you wish to visualize

Transcript locations and cell/nuclear segmentations exported by MERlin can be processed directly by Bella Vista

### MERlin input files for JSON

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

    All input paths *must* be relative paths to :samp:`data_folder`
```


### Example JSONs

##### Transcripts only
```{eval-rst}
.. code-block:: JSON

  {
    "system": "MERlin",
    "data_folder": "/path/to/dataset",
    "bella_vista_output_folder": "path/to/dataset/bellavista_outs",
    "create_bellavista_inputs": true,
    
    "parameters": {
        "plot_transcripts": true,
    },
  
    "input_files": {
        "codebook": "codebook.csv",
        "transcript_filename": "ExportBarcodes/barcodes.csv",
    }
  } 
```

##### Image & transcripts
```{eval-rst}
.. code-block:: JSON

  {
    "system": "MERlin",
    "data_folder": "/path/to/dataset",
    "bella_vista_output_folder": "path/to/dataset/bellavista_outs",
    "create_bellavista_inputs": true,
    
    "parameters": {
        "plot_image": true,
        "plot_transcripts": true,
    },
  
    "input_files": {
        "microscope_parameters": "microscope.json",
        "codebook": "codebook.csv",
        "positions_list": "positions.csv",
        "images": ["stitched_polyT.tif","stitched_DAPI.tif"]
        "transcript_filename": "ExportBarcodes/barcodes.csv",
    }
  } 
```

##### All inputs (image, transcripts, segmentations)

```{eval-rst}
.. code-block:: JSON

  {
    "system": "MERlin",
    "data_folder": "/path/to/dataset",
    "bella_vista_output_folder": "path/to/dataset/bellavista_outs",
    "create_bellavista_inputs": true,
    
    "parameters": {
        "plot_image": true,
        "plot_transcripts": true,
        "plot_cell_seg": true
    },
  
    "input_files": {
        "microscope_parameters": "microscope.json",
        "codebook": "codebook.csv",
        "positions_list": "positions.csv",
        "z_plane": 2,
        "images": ["stitched_polyT.tif","stitched_DAPI.tif"]
        "transcript_filename": "ExportBarcodes/barcodes.csv",
        "cell_segmentation": "RefineCellDatabases/features"
    }
  } 
```

##### All inputs + custom parameters

```{eval-rst}
.. code-block:: JSON

  {
    "system": "MERlin",
    "data_folder": "/path/to/dataset",
    "bella_vista_output_folder": "path/to/dataset/bellavista_outs",
    "create_bellavista_inputs": true,
    
    "parameters": {
        "plot_image": true,
        "plot_transcripts": true,
        "plot_cell_seg": true,
        "plot_allgenes": false,
        "selected_genes": ["Gene1", "Gene2"],
        "transcript_point_size": 0.75,
        "contrast_limits": [10000, 25000]
    },
  
    "input_files": {
        "microscope_parameters": "microscope.json",
        "codebook": "codebook.csv",
        "positions_list": "positions.csv",
        "z_plane": 2,
        "images": ["stitched_polyT.tif","stitched_DAPI.tif"]
        "transcript_filename": "ExportBarcodes/barcodes.csv",
        "cell_segmentation": "RefineCellDatabases/features"
    }
  } 
```

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