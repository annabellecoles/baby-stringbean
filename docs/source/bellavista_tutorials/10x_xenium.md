10x Genomics Xenium
===================

This tutorial is for visualizing 10x Genomics Xenium datasets. 

In order to visualize your Xenium dataset in Bella Vista, you will need to create a dataset-specific JSON configuration file containing paths to the Xenium outputs for your dataset. These output files will be processed to generate visualization files for Bella Vista. Creating these visualization files will take a few minutes but only need to be created once. For subsequent runs, `create_inputs` can be set to `False`.

## Configuration JSON file structure

```{eval-rst}
.. code-block:: JSON

    { 
        "system": "xenium", 
        "data_folder": "/path/to/Xenium_dataset_outs",
        "bella_vista_output_folder": "/path/to/Xenium_dataset_outs/bellavista_outs",
        "create_bellavista_inputs": true,

        "visualization_parameters": {
            "plot_image": true,
            "plot_transcripts": true,
            "plot_allgenes": true,
            "plot_cell_seg": true
        },

        "input_files": {
            "images": "morphology.ome.tif",
            "z_plane": 0,
            "transcript_filename": "transcripts.parquet",
            "cell_segmentation": "cell_boundaries.parquet",
            "nuclear_segmentation": "nucleus_boundaries.parquet"
        }
    }
```



## Input file parameters (Xenium)


**transcript_filename**: *string*
: relative path to a Parquet or CSV file containing transcript spatial locations. If None, no transcripts will be prepared

**images**: *string or 1D array of strings*
: relative path to image file(s). Must be an OME-TIFF or TIFF file. If None, no images will be displayed

**z_plane**: *integer, default=0*
: z-plane of image to be used

**cell_segmentation**: *string*
: relative path to Parquet or Zarr file containing cell segmentations. If None, no cell segmentations will be prepared

**nuclear_segmentation**: *string*
: relative path to Parquet or Zarr file containing nuclear segmentations. If None, no nuclear segmentations will be prepared

```{eval-rst}
.. note::

    All input paths *must* be relative paths to :samp:`data_folder`
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

## Sample dataset & JSON

Download sample data: [Xenium mouse brain dataset (replicate 3)](https://www.10xgenomics.com/datasets/fresh-frozen-mouse-brain-replicates-1-standard)
- Copy and save contents below into a new JSON file called `xenium_sample.json`
- The sample JSON file can also be found in the Bella Vista GitHub repository: [https://github.com/pkosurilab/BellaVista/tree/main/sample_json/xenium_sample.json](https://github.com/pkosurilab/BellaVista/tree/main/sample_json/xenium_sample.json)
- Replace the paths in the `data_folder` and `bella_vista_output_folder` properties

Sample JSON file:

```{eval-rst}
.. code-block:: JSON

  { 
      "system": "xenium", 
      "data_folder": "/path/to/Xenium_V1_FF_Mouse_Brain_MultiSection_3_outs",
      "bella_vista_output_folder": "/path/to/Xenium_V1_FF_Mouse_Brain_MultiSection_3_outs/bellavista_outs",
      "create_bellavista_inputs": true,

      "visualization_parameters": {
          "plot_image": true,
          "plot_transcripts": true,
          "plot_allgenes": true,
          "plot_cell_seg": false,
          "plot_nuclear_seg": false,
          "transcript_point_size": 0.75,
          "contrast_limits": [600, 3200],
          "rotate_angle": 180
      },

      "input_files": {
          "images": "morphology_mip.ome.tif",
          "z_plane": 5,
          "transcript_filename": "transcripts.parquet",
          "cell_segmentation": "cell_boundaries.parquet",
          "nuclear_segmentation": "nucleus_boundaries.parquet"
      }
  }
```

In the terminal, run Bella Vista with the Xenium sample JSON:
```{eval-rst}
.. code-block:: python

  bellavista xenium_sample.json
```

Using this JSON file, the displayed output should look similar to this: 

<img src="https://github.com/pkosurilab/BellaVista/blob/pypi-documentation/images/xenium_brain_position0_allgenes.png?raw=true" alt="Initial napari load page" width="600" />



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