from shap_e.util.notebooks import decode_latent_mesh
from shap_e.models.download import load_model
import torch

def text_to_3d(prompt, output_path='output.obj'):
    # 1. Load pre-trained model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = load_model('text300M', device=device)
    
    # 2. Generate 3D from text
    latent = model.sample_latents(batch_size=1, text=[prompt])
    
    # 3. Convert to mesh
    mesh = decode_latent_mesh(model, latent[0]).tri_mesh()
    
    # 4. Save as OBJ
    with open(output_path, 'w') as f:
        mesh.write_obj(f)
    print(f"Saved 3D model to {output_path}")

# Example usage
text_to_3d("a small toy car", "car.obj")