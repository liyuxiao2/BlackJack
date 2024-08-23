import pygame 

def load_images(base_path, count, scale_width, scale_height):
    # If count is 0, automatically assume we're loading only 1 image
    if count == 0:
        image_path = f'{base_path}.png'
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (scale_width, scale_height))
        return image
    else:
        images = []
        for i in range(count):
            # Construct the file name with leading zeros (assuming 5 digits like 'tile00000.png')
            image_path = f'{base_path}{str(i).zfill(5)}.png'
            try:
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, (scale_width, scale_height))
                images.append(image)
            except FileNotFoundError:
                print(f"File not found: {image_path}")
                continue
        return images

