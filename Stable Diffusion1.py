from diffusers import PNDMScheduler, DDIMScheduler, LMSDiscreteScheduler

# scheduler = PNDMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", skip_prk_steps=True)
scheduler = DDIMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
# scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
import mediapy as media
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"
remove_safety = False


pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16, revision="fp16", use_auth_token=True)
if remove_safety:
  pipe.safety_checker = lambda images, clip_input: (images, False)
pipe = pipe.to(device)


prompt = "spacewarriors in a lake in minecraft"
num_images = 1

prompts = [prompt] * num_images
with autocast("cuda"):
  images = pipe(prompts, guidance_scale=7.5, num_inference_steps=100)["sample"]

media.show_images(images)
images[0].save("output.png")