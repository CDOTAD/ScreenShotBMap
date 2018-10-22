from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

"""
BMap_scaleText=['5 公里', '2 公里', '1 公里', '500 米', '200 米', '100 米', '50 米', '20 米’, '10 米', '5 米']
"""

DATAROOT = 'ScreenShot/'


class ScreenShot:

    def __init__(self):

        # load the BMap
        browser = webdriver.Chrome()
        self.__browser = browser
        browser.maximize_window()
        browser.get("https://map.baidu.com")

        # shift to the satellite map
        mapType_wrapper = browser.find_element_by_id("mapType-wrapper")
        ActionChains(browser).move_to_element(mapType_wrapper).perform()

        earth = browser.find_element_by_css_selector('''div[data-name="earth"]''')
        # hide the road network
        road_network = earth.find_element_by_css_selector('''input[type="checkbox"]''')
        ActionChains(browser).click(road_network).perform()

        # scale the map
        zoom_in = browser.find_element_by_class_name('BMap_stdMpZoomIn')
        bmap_scaletxt = browser.find_element_by_class_name('BMap_scaleTxt')
        while True:
            if bmap_scaletxt.text == '20 米':
                break

            ActionChains(browser).click(zoom_in).perform()
            time.sleep(1)
        time.sleep(10)


    def __get_start_index(self):

        for root, dirs, files in os.walk(DATAROOT):
             latest_shot = files[-1]
        
        latest_index = int(latest_shot.split('.')[0])

        return latest_index

    def __walking(self):

        brower = self.__browser
        brower_size = brower.get_window_size()

        step_x = brower_size['width']/4
        step_y = brower_size['height']/4

        return step_x, step_y

    # print screen
    def print_screen(self, max_shot_num):

        browser = self.__browser

        browser_size = browser.get_window_size()
        
        step_x, step_y = self.__walking()

        latest_index = self.__get_start_index()

        for i in range(max_shot_num):
            browser.save_screenshot(DATAROOT+str(i+latest_index)+'.png')
            map_holder = browser.find_element_by_id('MapHolder')
            ActionChains(browser).drag_and_drop_by_offset(map_holder, step_x, step_y).perform()
            time.sleep(10)


if __name__ == '__main__':

    screen_shot = ScreenShot()
    screen_shot.print_screen(500)





