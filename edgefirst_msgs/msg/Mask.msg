# Segmentation Mask as sent by the Model message.  Masks can be classical
# segmentation masks or occupancy grids, including voxel grids when using 3D
# masks (width, height, and length are non-zero).

uint32 height       # The height of the mask
uint32 width        # The width of the mask
uint32 length       # The length of the mask when using 3D masks.

string encoding     # The optional encoding for the mask (currently unused).

uint8[] mask        # The segmentation mask

bool boxed          # If the mask is matched to a box for instance segmentation
