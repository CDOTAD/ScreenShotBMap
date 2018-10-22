from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


"""
BMap_scaleText=['5 公里', '2 公里', '1 公里', '500 米', '200 米', '100 米', '50 米', '20 米’, '10 米', '5 米']
"""

DATAROOT = 'ScreenShot/'


class ScreenShot:

    def __init__(self):

        # load the BMap
        browser = webdriver.Chrome()
        self.browser = browser
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

    # print screen
    def print_screen(self, max_shot_num):

        browser = self.browser

        browser_size = browser.get_window_size()
        step_y = browser_size['height']/4

        for i in range(max_shot_num):
            browser.save_screenshot(DATAROOT+str(i+500)+'.png')
            map_holder = browser.find_element_by_id('MapHolder')
            ActionChains(browser).drag_and_drop_by_offset(map_holder, 0, step_y).perform()
            time.sleep(10)


if __name__ == '__main__':

    screen_shot = ScreenShot()
    screen_shot.print_screen(500)




