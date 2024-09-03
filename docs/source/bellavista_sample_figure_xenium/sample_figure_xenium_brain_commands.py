import os
import pickle

pkl_dir = '/Users/kosuri_lab/BellaVista_Xenium_sample_figure' #replace with path to folder containing sample pickles (download from dropbox)
screenshot_dir = '/Users/kosuri_lab/BellaVista_Xenium_sample_figure/user_screenshots' #replace with path to save folder for screenshots

if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# assign gene colors 
with open(os.path.join(pkl_dir, 'xenium_brain_gene_colors_dict.pkl'), 'rb') as f:
    gene_colors_dict = pickle.load(f)
for gene in gene_colors_dict.keys():
    viewer.layers[gene].face_color = gene_colors_dict[gene]

# assign DAPI colormap & gamma
image_layers = [layer for layer in viewer.layers if isinstance(layer, napari.layers.Image)]
for layer in image_layers:
    layer.colormap = 'dodgerblue'
    layer.gamma = 1.6

# take zoomed out screenshot 
with open(os.path.join(pkl_dir, 'xenium_brain_position_0.pkl'), 'rb') as f:
    position_0 = pickle.load(f)
viewer.camera.center, viewer.camera.zoom = position_0['center'], position_0['zoom']
viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_0.png'))

# zoom in
with open(os.path.join(pkl_dir, 'xenium_brain_position_1.pkl'), 'rb') as f:
    position_1 = pickle.load(f)
viewer.camera.center, viewer.camera.zoom = position_1['center'], position_1['zoom']
viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_1.png'))

# make only DAPI layer visible
for layer in viewer.layers:
    if isinstance(layer, napari.layers.Image):
        layer.visible=True
    else:
        layer.visible=False
    
viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_1_DAPI.png'))

# zoom in more
with open(os.path.join(pkl_dir, 'xenium_brain_position_2.pkl'), 'rb') as f:
    position_2 = pickle.load(f)
viewer.camera.center, viewer.camera.zoom = position_2['center'], position_2['zoom']
viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_2_DAPI.png'))

# make all layers visible
for layer in viewer.layers:
    layer.visible=True
viewer.screenshot(os.path.join(screenshot_dir, 'xenium_brain_position_2.png'))