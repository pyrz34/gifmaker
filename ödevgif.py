from PIL import Image

# Create a list of images
images = [Image.open(f'image{i}.jpg') for i in range(1, 6)]

# Create a new GIF image
gif = Image.new('RGB', images[0].size)

# Create a new GIF file
gif.save('output.gif', format='GIF', append_images=images, save_all=True, duration=100, loop=0)