import pygame 


def load_images(base_path, count, scale_width, scale_height):
    #if count = 0 automatically assume its only 1 image were loading
    if(count == 0):
        image_path = f'{base_path}.png'
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (scale_width,scale_height))
        return image
    else:
        images = []
        for i in range(1, count + 1):
            image_path = f'{base_path}{i}.png'
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (scale_width,scale_height))
            images.append(image)
        return images
