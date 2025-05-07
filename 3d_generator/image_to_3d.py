import cv2
import numpy as np
import trimesh

def image_to_3d(image_path, output_path='output.obj'):
    # 1. Load image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Create fake depth (simplified approach)
    depth = cv2.GaussianBlur(img, (25, 25), 0)
    depth = cv2.normalize(depth, None, 0, 1, cv2.NORM_MINMAX)
    
    # 3. Generate 3D grid
    h, w = img.shape
    x = np.linspace(0, 1, w)
    y = np.linspace(0, 1, h)
    x, y = np.meshgrid(x, y)
    z = depth * 0.2  # Scale depth
    
    # 4. Create mesh
    vertices = np.vstack([x.ravel(), y.ravel(), z.ravel()]).T
    faces = []
    for i in range(h-1):
        for j in range(w-1):
            v0 = i * w + j
            v1 = v0 + 1
            v2 = (i + 1) * w + j
            faces.extend([[v0, v1, v2], [v1, v2, (i+1)*w + j + 1]])
    
    # 5. Save as OBJ
    trimesh.Trimesh(vertices=vertices, faces=faces).export(output_path)
    print(f"3D model saved to {output_path}")

# Run it
image_to_3d('chair.jpg', 'my_model.obj')