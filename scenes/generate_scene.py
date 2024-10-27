from diffusers import StableDiffusionPipeline
from PIL import Image

# Load the model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")  # Use CUDA if available

# Generate a scene
prompt = "A futuristic cityscape at night with neon lights"
image = pipe(prompt).images[0]

# Save the generated image
image.save("scenes/futuristic_cityscape.png")
