from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *
import warnings

if not torch.cuda.is_available():
    print('GPU not available.')
    device.set(device=DeviceId.CPU)
else:
    print('GPU is available.')
    device.set(device=DeviceId.GPU0)

warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic=True)


def colorize(path):
    image_path = None
    if path is not None and path != '':
        print(path)
        # render_factor = 7 - 40
        image_path = colorizer.plot_transformed_image(path=path, render_factor=20,
                                                      compare=True, watermarked=False)
    else:
        print('Provide an image url and try again.')
    return image_path


if __name__ == "__main__":
    source_url = 'https://images.wallpaperscraft.ru/image/single/molniia_oblaka_chb_179050_1400x1050.jpg'
    import time

    st = time.time()
    colorize(source_url)
    print(time.time() - st)
