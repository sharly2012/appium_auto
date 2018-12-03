import cv2
import pytesseract
from PIL import Image
from utils.logger import Logger

logger = Logger(logger="ImageUtil").get_log()


class ImageUtil:

    def _get_dynamic_binary_image(self, file_dir, file_name):
        filename = self.path + '/out_img/' + file_name.split('.')[0] + '-binary.jpg'
        img_name = file_dir + '/' + file_name
        print(img_name)
        img = cv2.imread(img_name)
        # 灰值化
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 二值化
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
        cv2.imwrite(filename, img)
        return img

    # 去除边框
    def clear_border(self, img, img_name):
        filename = self.path + '/out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
        h, w = img.shape[:2]
        for y in range(0, w):
            for x in range(0, h):
                if y < 2 or y > w - 2:
                    img[x, y] = 255
                if x < 2 or x > h - 2:
                    img[x, y] = 255

        cv2.imwrite(filename, img)
        return img

    # 干扰线降噪
    def interference_line(self, img, img_name):
        filename = self.path + '/out_img/' + img_name.split('.')[0] + '-interferenceline.jpg'
        h, w = img.shape[:2]
        # ！！！opencv矩阵点是反的
        # img[1,2] 1:图片的高度，2：图片的宽度
        for y in range(1, w - 1):
            for x in range(1, h - 1):
                count = 0
                if img[x, y - 1] > 245:
                    count = count + 1
                if img[x, y + 1] > 245:
                    count = count + 1
                if img[x - 1, y] > 245:
                    count = count + 1
                if img[x + 1, y] > 245:
                    count = count + 1
                if count > 2:
                    img[x, y] = 255
        cv2.imwrite(filename, img)
        return img

    # 点降噪
    def interference_point(self, img, img_name, x=0, y=0):
        """
        9邻域框,以当前点为中心的田字框,黑点个数
        :param x:
        :param y:
        :return:
        """
        filename = self.path + '/out_img/' + img_name.split('.')[0] + '-interferencePoint.jpg'
        # 判断图片的长宽度下限
        cur_pixel = img[x, y]  # 当前像素点的值
        height, width = img.shape[:2]

        for y in range(0, width - 1):
            for x in range(0, height - 1):
                if y == 0:  # 第一行
                    if x == 0:  # 左上顶点,4邻域
                        # 中心点旁边3个点
                        sum = int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum <= 2 * 245:
                            img[x, y] = 0
                    elif x == height - 1:  # 右上顶点
                        sum = int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1])
                        if sum <= 2 * 245:
                            img[x, y] = 0
                    else:  # 最上非顶点,6邻域
                        sum = int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum <= 3 * 245:
                            img[x, y] = 0
                elif y == width - 1:  # 最下面一行
                    if x == 0:  # 左下顶点
                        # 中心点旁边3个点
                        sum = int(cur_pixel) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x, y - 1])
                        if sum <= 2 * 245:
                            img[x, y] = 0
                    elif x == height - 1:  # 右下顶点
                        sum = int(cur_pixel) \
                              + int(img[x, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y - 1])

                        if sum <= 2 * 245:
                            img[x, y] = 0
                    else:  # 最下非顶点,6邻域
                        sum = int(cur_pixel) \
                              + int(img[x - 1, y]) \
                              + int(img[x + 1, y]) \
                              + int(img[x, y - 1]) \
                              + int(img[x - 1, y - 1]) \
                              + int(img[x + 1, y - 1])
                        if sum <= 3 * 245:
                            img[x, y] = 0
                else:  # y不在边界
                    if x == 0:  # 左边非顶点
                        sum = int(img[x, y - 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])

                        if sum <= 3 * 245:
                            img[x, y] = 0
                    elif x == height - 1:  # 右边非顶点
                        sum = int(img[x, y - 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x - 1, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1])

                        if sum <= 3 * 245:
                            img[x, y] = 0
                    else:  # 具备9领域条件的
                        sum = int(img[x - 1, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1]) \
                              + int(img[x, y - 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum <= 4 * 245:
                            img[x, y] = 0
        cv2.imwrite(filename, img)
        return img

    def image_to_string(self, locator):
        # 截取当前网页，该网页有我们需要的验证码
        self.driver.save_screenshot(self.root_path + "/screenshots/" + "All.png")
        img_element = self.find_element(*locator)
        # 获取验证码x,y轴坐标
        location = img_element.location
        # 获取验证码的长宽
        size = img_element.size
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  # 写成我们需要截取的位置坐标
                  int(location['y'] + size['height']))
        i = Image.open(self.root_path + "/screenshots/" + "All.png")
        # 使用Image的crop函数，从截图中再次截取我们需要的区域
        result = i.crop(rangle)
        result.save(self.path + "/screenshots/" + "result.png")
        rgb_im = result.convert('RGB')
        rgb_im.save(self.root_path + "/screenshots/" + "result.jpg")
        img = Image.open(self.root_path + "/screenshots/" + "result.jpg")
        img.convert("L")
        # file_dir = self.path + '/screenshots'
        # img_name = "result.jpg"
        # img = self._get_dynamic_binary_image(file_dir, img_name)
        # img = self.clear_border(img, img_name)
        # img = self.interference_line(img, img_name)
        # img = self.interference_point(img, img_name)
        verify_code = pytesseract.image_to_string(img).strip()
        logger.info("verify code is: " + verify_code)
        return verify_code
