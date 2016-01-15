from constants import FOREGROUND_PIXEL_COLOR


def get_pix(img, y, x):
    """
    Safe access to a pixel in a matrix
    """
    if y >= img.shape[0] or y < 0 or x >= img.shape[1] or x < 0:
        return None
    return img[y][x]


def get_neighbour_pixel(img, cur_y, cur_x):
    """
    Return the number of pixel around a specific pixel
    """
    count = 0
    for y in range(3):
        for x in range(3):
            if x == 1 and y == 1:
                continue
            new_pix_x = (cur_x + x) - 1
            new_pix_y = (cur_y + y) - 1
            if get_pix(img, new_pix_y, new_pix_x) == FOREGROUND_PIXEL_COLOR:
                count += 1
    return count


def get_pixels_around(img, cur_x, cur_y):
    """
    Return a generator containing pixel around a specific pixel
    """
    for y in range(3):
        for x in range(3):
            if x == 1 and y == 1:
                continue
            new_pix_x = (cur_x + x) - 1
            new_pix_y = (cur_y + y) - 1
            if get_pix(img, new_pix_y, new_pix_x) == FOREGROUND_PIXEL_COLOR:
                yield Pixel(new_pix_x, new_pix_y)
