import os

os.environ["CUDA_LAUNCH_BLOCKING"]="1" 
os.environ["TORCH_USE_CUDA_DSA"] = "1"

from transformers import AutoProcessor, AutoTokenizer, Gemma3ForConditionalGeneration
from PIL import Image
import torch

# Define the local model path
local_model_path = "D:\Development\GenAI\HuggingFace\models\Gemma3-4b-it"

# Load the model, processor, and tokenizer
#model = Gemma3ForConditionalGeneration.from_pretrained(local_model_path)
model = Gemma3ForConditionalGeneration.from_pretrained(local_model_path, torch_dtype=torch.bfloat16)
processor = AutoProcessor.from_pretrained(local_model_path, use_fast=True,trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(local_model_path, use_fast=True)


# Move the model to GPU if available
#device = "cuda" if torch.cuda.is_available() else "cpu"
#model = model.to(device)
model.to(torch.device('cuda'))
# Define the prompt and image path
prompt = "<start_of_image> Write a detailed description of this image"
image_path = "D:\Development\GenAI\HuggingFace\images\photo.jpg"  # Replace with your image file path

# Load and process the image
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Error: The image file at {image_path} was not found.")
    exit()


# Prepare inputs for the model
model_inputs = processor(text=prompt, images=image, return_tensors="pt").to(torch.device('cuda'))#.to(device)

# Generate a response
outputs = model.generate(**model_inputs, max_new_tokens=250, disable_compile=True)
 
#decoded = processor.decode(outputs[0], skip_special_tokens=True)
#print(decoded)

# Decode the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the response
print(response)
