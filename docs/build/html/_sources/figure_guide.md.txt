```{toctree}
:hidden: true
```
# {octicon}`pencil` Figure Guide

Bella Vista can be used to create poster, presentation, and paper-ready figures highlighting spatial discoveries in your data. Figures can also be reproduced between different sessions, different computers, and different users.

**Saving screenshots:**

```{eval-rst}
.. code-block:: python

    # saves a screenshot of the canvas to filepath
    viewer.screenshot("/screenshots/position_1.tif", canvas_only=True)
```

```{eval-rst}
.. tip::

    To maximise content visible in the canvas, open the console in a separate window
```

**Creating reproducible figures:**

Save current camera position & zoom:
```{eval-rst}
.. code-block:: python

    import pickle

    # take screenshot of current canvas
    viewer.screenshot("/screenshots/position_1.tif", canvas_only=True)

    # save current camera state
    position_1 = {'center': viewer.camera.center, 'zoom': viewer.camera.zoom}
    with open('/screenshots/position_1.pkl', 'wb') as f:
        pickle.dump(position_1, f)
```
Return to saved position:

```{eval-rst}
.. code-block:: python

    # return to camera state from previous screenshot
    viewer.camera.center, viewer.camera.zoom = position_1['center'], position_1['zoom']
```

**Reproducing figures in different sessions/computers/users:**

Session 1:
```{eval-rst}
.. code-block:: python

    import pickle

    #take screenshot of current canvas
    viewer.screenshot("/screenshots/position_1.tif", canvas_only=True)

    # save current camera state
    position_1 = {'center': viewer.camera.center, 'zoom': viewer.camera.zoom}
    with open('/screenshots/position_1.pkl', 'wb') as f:
        pickle.dump(position_1, f)

    # save current point color for each gene layer
    gene_colors_dict = {}
    gene_layers = [layer for layer in viewer.layers if isinstance(layer, napari.layers.Points)]
    for gene_layer in gene_layers:
        gene_colors_dict[gene_layer.name] = gene_layer.face_color[0]

    with open('/screenshots/gene_colors_dict.pkl', 'wb') as f:
        pickle.dump(gene_colors_dict, f)
```

Session 2:

```{eval-rst}
.. code-block:: python

    import pickle

    # assign gene transcript point colors from session 1
    with open('/screenshots/gene_colors_dict.pkl', 'rb') as f:
        gene_colors_dict = pickle.load(f)
    for gene in gene_colors_dict.keys():
                    viewer.layers[gene].face_color = gene_colors_dict[gene]

    # reproduce screenshot from session 1
    with open('/screenshots/position_1.pkl', 'rb') as f:
                    position_1 = pickle.load(f)
    # return to camera state from previous screenshot
    viewer.camera.center, viewer.camera.zoom = position_1['center'], position_1['zoom']

    # take screenshot of current canvas -- this should be the same image from session 1
    viewer.screenshot("/screenshots/position_1_session2.tif")
```

<!-- TODO CHANGE FIGURE IMAGE!! -->
Example from [Xenium mouse brain dataset (replicate 3)](https://www.10xgenomics.com/datasets/fresh-frozen-mouse-brain-replicates-1-standard):

:::{image} _static/reproducibility.png
:alt: Figure reproducibility 
:align: center
:width: 800px
:::


JSON & pickle files to reproduce the above screenshot can be found [here](https://github.com/pkosurilab/BellaVista)

```{eval-rst}
.. note::

    When taking screenshots on different computers, the content visible may be different due to a difference in display size
```

