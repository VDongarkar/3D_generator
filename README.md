# 3D_generator

Step - 1: 
git clone https://github.com/yourusername/3d-model-generator.git
cd 3d-model-generator

Step - 2:
pip install -r requirements.txt

Step - 3:
python image_to_3d.py --input your_image.jpg --output model.obj

Step - 4:
python text_to_3d.py --prompt "a futuristic chair" --output chair.obj

libraries needed :
pip install numpy trimesh torch opencv-python Pillow scipy ipywidgets tqdm git+https://github.com/openai/shap-e.git

