import cv2
import numpy as np


class ProportionException(Exception):

    pass


class BezelMaker:

    def __init__(self, img_path, proportion=(4, 5), background_color=(255, 255, 255)):
        self._proportion = proportion
        self._background_color = background_color
        
        self._load_img(img_path)
        self._check_proportion()
        
    def _check_proportion(self):
        img_proportion = self.width / (2 * self.height)
        rounded_img_proportion = round(img_proportion, 3)
        if rounded_img_proportion != (self._proportion[0] / self._proportion[1]):
            raise ProportionException('Oopsie')

    def _load_img(self, img_path):
        self.img = cv2.imread(img_path)
        self.height, self.width, _ = self.img.shape

    def _pic1(self):
        horizontal_bezel_size = int(self.width * .025)
        vertical_total_size = int(
            (self._proportion[1] / self._proportion[0]) *
            (2 * horizontal_bezel_size + self.width)
        )
        vertical_bezel_size = int((vertical_total_size - self.height) / 2)

        border = cv2.copyMakeBorder(
            self.img,
            top=vertical_bezel_size,
            bottom=vertical_bezel_size,
            left=horizontal_bezel_size,
            right=horizontal_bezel_size,
            borderType=cv2.BORDER_CONSTANT,
            value=self.background_color
        )

        return border

    def _pic2(self):
        pic2 = self.img[:, :int(self.width / 2)]
        return pic2

    def _pic3(self):
        pic3 = self.img[:, int(self.width / 2):]
        return pic3
    
    def get_imgs(self):
        return (self._pic1(), self._pic2(), self._pic3())

    '''
    def test(self):
        pic2 = self.img[:, :int(self.width / 2)]
        pic3 = self.img[:, int(self.width / 2):]
        result = np.concatenate((pic2, pic3), axis=1)
        cv2.imwrite('test_result.png', result)
    '''


bezel_maker = BezelMaker('AA028_0.png')