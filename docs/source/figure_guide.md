```{toctree}
:hidden: true
```
# {octicon}`pencil` Figure Guide

Bella Vista can be used to create poster, presentation, and paper-ready figures highlighting spatial discoveries in your data. Figures can also be reproduced between different sessions, different computers, and different users.

## Reproducing sample figures (Xenium)

Below is a step-by-step guide to reproducing the following screenshots from a sample Xenium dataset.

<div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: flex-end;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_0.png" alt="zoom out screenshot" style="width: 45%;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_1.png" alt="zoom in screenshot" style="width: 45%">
</div>

### Download sample data

Download sample data: Xenium mouse brain dataset (replicate 3)
[https://www.10xgenomics.com/datasets/fresh-frozen-mouse-brain-replicates-1-standard](https://www.10xgenomics.com/datasets/fresh-frozen-mouse-brain-replicates-1-standard)

To download the dataset, 10x Genomics may ask you to fill out a questionnaire.

<img src="https://github.com/pkosurilab/BellaVista/blob/main/images/xenium_testdata_location.png?raw=true" alt="Xenium sample data website location" width="600" />

Configuration files needed to reproduce the sample screenshots are available [here on Dropbox](https://www.dropbox.com/scl/fo/5ae35p7nbkct0e0mi92vz/AD38rhAb4M6L36putA4qREU?rlkey=hjnf94fomm5k2rfyzyi7b58u3).

### Load Bella Vista

1. Copy and save contents below into a new JSON file called `sample_figure_xenium_brain.json`
      - This sample JSON can also be found in the Dropbox folder
2. Replace the paths in `data_folder` and `bella_vista_output_folder` parameters
      - JSON files cannot interpret the blackslash character (\\), instead you should use a forward slash (/)

```{eval-rst}
.. code-block:: JSON
  :emphasize-lines: 3-4

  { 
    "system": "xenium", 
    "data_folder": "/path/to/xenium_brain_rep3",
    "bella_vista_output_folder": "/path/to/xenium_brain_rep3/bellavista_outs",
    "create_bellavista_inputs": true,

    "visualization_parameters": {
        "plot_image": true,
        "plot_transcripts": true,
        "plot_allgenes": false,
        "genes_visible_on_startup": true,
        "selected_genes": ["Igfbp5","Igf2","Gjc3","Gad2","Epha4","Dner","Dkk3",
                            "Col1a1","Cntnap4","Clmn","Ccn2","Cbln4","Cbln1",
                            "Car4","Calb2","Calb1","Cacna2d2","Cabp7","Bcl11b",
                            "2010300C02Rik"],
        "transcript_point_size": 0.75,
        "contrast_limits": [0, 5000],
        "rotate_angle": 180
    },
    
    "input_files": {
        "transcript_filename": "transcripts.parquet",
        "images": "morphology_mip.ome.tif",
        "z_plane": 5
    }
  }
```

3. In the terminal, run Bella Vista with the Xenium sample JSON. 
    - The JSON file argument should contain the file path to the JSON file.
```{eval-rst}
.. code-block:: python

  bellavista sample_figure_xenium_brain.json
```

```{eval-rst}
.. note::

    It will take a few minutes to create the required data files. The terminal will print updates & have progress bars for time consuming steps.
```

Once loaded, your napari window should look similar to this. The gene colors displayed will be different, but we'll reassign those later!

<p align="center">
  <picture>
    <img alt="zoom out screenshot" src="_static/sample_figure_screenshots/xenium_brain_initial.png" style="width: 80%">
  </picture>
</p>
<p align="center">

Now that the data has loaded, we can start configuring it to reproduce the example figures. These next steps will all be done in the napari console.

<hr class="custom-line-light">

```{eval-rst}
.. note::

    When taking screenshots on different computers, the content visible may be different due to different display sizes and screen resolutions.
```

Here is a comparison of screenshots taken on different display resolutions:

**4K display**
<div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: flex-end;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_0_4K.png" alt="zoom out screenshot" style="width: 49%;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_1_4K.png" alt="zoom in screenshot" style="width: 49%">
</div>

**Full HD display**
<div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: flex-end;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_0_1920x1080.png" alt="zoom out screenshot" style="width: 49%;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_1_1920x1080.png" alt="zoom in screenshot" style="width: 49%">
</div>

```{eval-rst}
.. tip::

    If you're using a lower-resolution display, you can enhance the quality of saved images by specifying a higher resolution when saving screenshots. In the following tutorial, I will specify a 4K resolution in the :samp:`screenshot_resolution` variable in step 1. 
    
    This parameter can also be used to save screenshots in various sizes, such as square screenshots. 
```

**Full HD display with a save resolution of 4K**
<div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: flex-end;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_0_1920x1080_4K.png" alt="zoom out screenshot" style="width: 49%;">
  <img src="_static/sample_figure_screenshots/xenium_brain_position_1_1920x1080_4K.png" alt="zoom in screenshot" style="width: 49%">
</div>

<hr class="custom-line-light">

### Using the napari console

To take screenshots and save current layer configurations, you can use the napari console.\
The napari console can be found in the bottom left of the gui:

<p align="center">
  <picture>
    <img alt="napari console" src="_static/napari_open_console.png" style="width: 1000px">
  </picture>
</p>
<p align="center">

**Note:** To maximise content visible in the canvas, open the console in a separate window:

<div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: flex-end;">
  <img src="_static/napari_maximize_console.png" alt="maximize console" style="width: 100%;">
  <img src="_static/maximize_button.png" alt="max button" style="width: 20%; margin-left: -300px; margin-top: -300px;">
</div>

<p align="center">
  <picture>
    <img alt="console separate window" src="_static/napari_terminal_window.png" style="width: 1000px">
  </picture>
</p>
<p align="center">

<br/>

### Change settings to match example configuration

#### 1. Set saved image resolution
```{eval-rst}
.. code-block:: python

    import os 
    import pickle

    # to save images at the default resolution of your display, set to None
    save_resolution = (2160, 3840) # 4K resolution
```

#### 2. Change folder paths
```{eval-rst}
.. code-block:: python

    #path to folder containing configuration files
    pkl_dir = '/path/to/BellaVista_Xenium_sample_figure'

    #path to save folder
    screenshot_dir = '/path/to/BellaVista_Xenium_sample_figure/user_screenshots'

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
```

#### 3. Assign gene colors
```{eval-rst}
.. code-block:: python

    with open(os.path.join(pkl_dir, 'xenium_brain_gene_colors_dict.pkl'), 'rb') as f:
        gene_colors_dict = pickle.load(f)
    for gene in gene_colors_dict.keys():
        viewer.layers[gene].face_color = gene_colors_dict[gene]
```

#### 4. Change colormap for DAPI image
```{eval-rst}
.. code-block:: python

    image_layers = [layer for layer in viewer.layers if isinstance(layer, napari.layers.Image)]
    for layer in image_layers:
        layer.colormap = 'dodgerblue'
        layer.gamma = 1.6
```

#### 5. Take zoomed out screenshot
```{eval-rst}
.. code-block:: python

    with open(os.path.join(pkl_dir, 'xenium_brain_position_0.pkl'), 'rb') as f:
        position_0 = pickle.load(f)
    viewer.camera.center, viewer.camera.zoom = position_0['center'], position_0['zoom']
    viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_0.png'), 
                        size = save_resolution)
```

<p align="center">
  <picture>
    <img alt="zoom out screenshot" src="_static/sample_figure_screenshots/xenium_brain_position_0.png" style="width: 80%">
  </picture>
</p>
<p align="center">

#### 6. Zoom in
```{eval-rst}
.. code-block:: python

    with open(os.path.join(pkl_dir, 'xenium_brain_position_1.pkl'), 'rb') as f:
        position_1 = pickle.load(f)
    viewer.camera.center, viewer.camera.zoom = position_1['center'], position_1['zoom']
    viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_1.png'), 
                        size = save_resolution)
```

<p align="center">
  <picture>
    <img alt="zoom out screenshot" src="_static/sample_figure_screenshots/xenium_brain_position_1.png" style="width: 80%">
  </picture>
</p>
<p align="center">

#### 7. Toggle off visibility of gene layers, leaving only DAPI visible
```{eval-rst}
.. code-block:: python

    for layer in viewer.layers:
        if isinstance(layer, napari.layers.Image):
            layer.visible=True
        else:
            layer.visible=False
    viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_1_DAPI.png'), 
                        size = save_resolution)
```

<p align="center">
  <picture>
    <img alt="zoom out screenshot" src="_static/sample_figure_screenshots/xenium_brain_position_1_DAPI.png" style="width: 80%">
  </picture>
</p>
<p align="center">

#### 8. Zoom in further
```{eval-rst}
.. code-block:: python

    with open(os.path.join(pkl_dir, 'xenium_brain_position_2.pkl'), 'rb') as f:
        position_2 = pickle.load(f)
    viewer.camera.center, viewer.camera.zoom = position_2['center'], position_2['zoom']
    viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_2_DAPI.png'), 
                        size = save_resolution)
```

<p align="center">
  <picture>
    <img alt="zoom out screenshot" src="_static/sample_figure_screenshots/xenium_brain_position_2_DAPI.png" style="width: 80%">
  </picture>
</p>
<p align="center">

#### 9. Toggle visibility of all layers on 
```{eval-rst}
.. code-block:: python

    for layer in viewer.layers:
        layer.visible=True
    viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_2.png'), 
                        size = save_resolution)
```

<p align="center">
  <picture>
    <img alt="zoom out screenshot" src="_static/sample_figure_screenshots/xenium_brain_position_2.png" style="width: 80%">
  </picture>
</p>
<p align="center">

<br><br>

(creating-figures)=
## Creating your own figures!

### Using the napari console

To take screenshots and save current layer configurations, you can use the napari console.\
The napari console can be found in the bottom left of the gui:

<p align="center">
  <picture>
    <img alt="napari console" src="_static/napari_open_console.png" style="width: 1000px">
  </picture>
</p>
<p align="center">

**Note:** To maximise content visible in the canvas, open the console in a separate window:

<div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: flex-end;">
  <img src="_static/napari_maximize_console.png" alt="maximize console" style="width: 100%;">
  <img src="_static/maximize_button.png" alt="max button" style="width: 20%; margin-left: -300px; margin-top: -300px;">
</div>

<p align="center">
  <picture>
    <img alt="console separate window" src="_static/napari_terminal_window.png" style="width: 1000px">
  </picture>
</p>
<p align="center">

(useful-figure-commands)=
### Useful commands


Screenshot current canvas:
```{eval-rst}
.. code-block:: python

    # save screenshot to folder
    viewer.screenshot("/path/to/folder/napari_canvas.png")
```

Set saved screenshot resolution:
```{eval-rst}
.. code-block:: python

    # set save resolution to 4K
    save_resolution = (2160, 3840) 

    # save screenshot with 4K resolution to folder
    viewer.screenshot("/path/to/folder/napari_canvas.png", size = save_resolution)
```

Save current camera position & zoom:
```{eval-rst}
.. code-block:: python

    import pickle

    # save current camera state
    position_1 = {'center': viewer.camera.center, 'zoom': viewer.camera.zoom}
    with open('/path/to/folder/position_1.pkl', 'wb') as f:
        pickle.dump(position_1, f)
```
Return to saved position:
```{eval-rst}
.. code-block:: python

    import pickle 

    # load previous camera state
    with open('/path/to/folder/position_1.pkl', 'rb') as f:
        position_1 = pickle.load(f)

    # return to camera state from previous screenshot
    viewer.camera.center, viewer.camera.zoom = position_1['center'], position_1['zoom']
```

Save transcript colors for each gene:
```{eval-rst}
.. code-block:: python

    import pickle 

    # store current transcript colors in a dictionary
    gene_colors_dict = {}
    gene_layers = [layer for layer in viewer.layers if isinstance(layer, napari.layers.Points)]
    for gene_layer in gene_layers:
        gene_colors_dict[gene_layer.name] = gene_layer.face_color[0]

    # save dictionary
    with open('/path/to/folder/gene_colors_dict.pkl', 'wb') as f:
        pickle.dump(gene_colors_dict, f)
```

Load saved transcript colors:
```{eval-rst}
.. code-block:: python

    import pickle

    # load saved transcript colors
    with open('/path/to/folder/gene_colors_dict.pkl', 'rb') as f:
        gene_colors_dict = pickle.load(f)

    # assign gene transcript point colors
    for gene in gene_colors_dict.keys():
        viewer.layers[gene].face_color = gene_colors_dict[gene]
```

