from diffusers import DiffusionPipeline
import torch
import numpy as np
import matplotlib.pyplot as plt

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
                                         torch_dtype=torch.float16,
                                         use_safetensors=True,
                                         variant="fp16")
pipe.to("cuda")

prompt = ["one horse sitting down the sky",
          "an astronaut riding a lion on Mars",
          "team of people playing football into the ocean", 
          "panda eating the moon happily"]

image1 = pipe(prompt=prompt[0]).images[0]
image2 = pipe(prompt=prompt[1]).images[0]
image3 = pipe(prompt=prompt[2]).images[0]
image4 = pipe(prompt=prompt[3]).images[0]

fig = plt.figure(figsize=(10,7))

rows, colomns = 2, 2

fig.add_subplot(rows, colomns, 1)

plt.imshow(image1)
plt.axis("off")
plt.title(prompt[1])

fig.add_subplot(rows, colomns, 2)

plt.imshow(image2)
plt.axis("off")
plt.title(prompt[2])

fig.add_subplot(rows, colomns, 3)

plt.imshow(image3)
plt.axis("off")
plt.title(prompt[3])

fig.add_subplot(rows, colomns, 4)

plt.imshow(image4)
plt.axis("off")
plt.title(prompt[4])

image1.save(prompt[0]+".jpg")
image2.save(prompt[1]+".jpg")
image3.save(prompt[2]+".jpg")
image4.save(prompt[3]+".jpg")