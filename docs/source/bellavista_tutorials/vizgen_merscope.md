Vizgen MERSCOPE
===============

This tutorial is for visualizing Vizgen MERSCOPE datasets. 

In order to visualize your MERSCOPE dataset in Bella Vista, you will need to create a dataset-specific JSON configuration file containing paths to the MERSCOPE outputs for your dataset. These output files will be processed to generate visualization files for Bella Vista. Creating these visualization files will take a few minutes but only need to be created once. For subsequent runs, `create_inputs` can be set to `False`.

## Configuration JSON file structure

```{eval-rst}
.. code-block:: JSON

    { 
        "system": "MERSCOPE", 
        "data_folder": "/path/to/MERSCOPE_dataset_outs",
        "bella_vista_output_folder": "/path/to/MERSCOPE_dataset_outs/bellavista_outs",
        "create_bellavista_inputs": true,

        "visualization_parameters": {
            "plot_image": true,
            "plot_transcripts": true,
            "plot_allgenes": true,
            "plot_cell_seg": true
        },

        "input_files": {
            "transcript_filename": "detected_transcripts.csv",
            "um_to_px_transform": "micron_to_mosaic_pixel_transform.csv",
            "images":  "mosaic_DAPI_z0.tif",
            "z_plane": 0,
            "cell_segmentation": "cell_boundaries"
        }
    }
```

## Input file parameters (MERSCOPE)


**transcript_filename**: *string*
: relative path to CSV file containing transcript spatial locations. If None, no transcripts will be prepared

**um_to_px_transform** *string*
: relative path to CSV file containing micron to pixel transformations

**images**: *string or 1D array of strings*
: relative path to image file(s). Must be a TIFF file. If None, no images will be displayed

**z_plane**: *integer, default=0*
: z-plane of cell segmentations to plot. We suggest this match the z-plane of the image you are visualizing 

**cell_segmentation**: *string*
: relative path to cell segmentations. This must be a Parquet file (MERSCOPE v232 or later) or a folder containing HDF5 files (pre v232). If None, no cell segmentations will be prepared

**nuclear_segmentation**: *string*
: relative path to nuclear segmentations. This must be a Parquet file (MERSCOPE v232 or later) or a folder containing HDF5 files (pre v232). If None, no nuclear segmentations will be prepared


```{eval-rst}
.. note::

  All input paths *must* be relative paths to :samp:`data_folder`
  
    If you are missing some input files, remove those input file parameters from the JSON file. Bella Vista will skip the visualization of these data.

    For example, if you do not have cell segmentations, the input file parameters in your JSON file might look like this: 

    .. code-block:: JSON

            "input_files": {
                "transcript_filename": "detected_transcripts.csv",
                "um_to_px_transform": "micron_to_mosaic_pixel_transform.csv",
                "images":  "mosaic_DAPI_z0.tif"
            }

```

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

Download sample data: MERSCOPE mouse brain dataset (Slice 1, Replicate 1)
[https://info.vizgen.com/mouse-brain-map](https://info.vizgen.com/mouse-brain-map)

To download the dataset, Vizgen may ask you to fill out a questionnaire.

<p align="center">
  <picture>
    <img src="../_static/tutorials/merscope/vizgen_testdata_location.png" alt="MERSCOPE sample data website location" width="600" />
  </picture>
</p>
<p align="center">

For this example, you only need to download:
- `detected_transcripts_S1R1.csv`
- `cell_boundaries/`
- `mosaic_DAPI_z3.tif` found inside `images/`

<p align="center">
  <picture>
    <img src="../_static/tutorials/merscope/vizgen_testdata_bucket.png" alt="MERSCOPE sample data google cloud console"/>
  </picture>
</p>
<p align="center">

```{eval-rst}
.. note::

  To download the `cell_boundaries` folder, you may need to use gsutil (Google Cloud Console will prompt you if this is the case).
  
  Here is some information on how to use gsutil: https://cloud.google.com/storage/docs/gsutil_install


```

### Load Bella Vista

- Copy and save contents below into a new JSON file called `merscope_sample.json`
- The sample JSON file can also be downloaded from the Bella Vista GitHub repository: [https://github.com/pkosurilab/BellaVista/tree/main/sample_json/merscope_sample.json](https://github.com/pkosurilab/BellaVista/tree/main/sample_json/merscope_sample.json)
- Replace the paths in the `data_folder` and `bella_vista_output_folder` properties

```{eval-rst}
.. code-block:: JSON

  { 
      "system": "merscope", 
      "data_folder": "/path/to/Vizgen_BrainReceptorShowcase_Slice1_Replicate1",
      "bella_vista_output_folder": "/path/to/Vizgen_BrainReceptorShowcase_Slice1_Replicate1/bellavista_outs",
      "create_bellavista_inputs": true,

      "visualization_parameters": { 
          "plot_image": true,
          "plot_transcripts": true,
          "plot_allgenes": false,
          "selected_genes": ["Fgfr2","Tmem108","Glp2r","Slc47a1","Tacr1","Th","Ntsr1",
                              "Sstr3","S1pr3","Sstr1","Ptgfr","Qrfpr","Gpr101","Drd5","Chat"],
          "plot_cell_seg": true,
          "transcript_point_size": 0.75,
          "contrast_limits": [0, 26000]
      },
      
      "input_files": {
          "um_to_px_transform": "datasets_mouse_brain_map_BrainReceptorShowcase_Slice1_Replicate1_images_micron_to_mosaic_pixel_transform.csv",
          "images":  "mosaic_DAPI_z3.tif",
          "z_plane": 3,
          "transcript_filename": "datasets_mouse_brain_map_BrainReceptorShowcase_Slice1_Replicate1_detected_transcripts_S1R1.csv",
          "cell_segmentation": "cell_boundaries"
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