from selenium import webdriver
from time import sleep
import pandas as pd


def get_ramen_data(ramen_data_list):
    name_list = driver.find_elements_by_class_name('name')
    rank_list = driver.find_elements_by_class_name('rank')
    point_list = driver.find_elements_by_class_name('point')

    for name, rank, point in zip(name_list, rank_list, point_list):
        ramen_data_list.append([name.text, rank.text, point.text])



driver = webdriver.Chrome('/Users/ogurayuudai/Desktop/personal-dev/map-application/chromedriver_mac_arm64/chromedriver')

sleep(1)
n = 1
for i in range(1):
    ramen_data_list = []
    page = 1+i*n
    p = n+i*n
    while page <= p:
        """
        if page == 1:
            page += 1
            continue
        """
        driver.get(f'https://ramendb.supleks.jp/rank?page={page}')
        sleep(1)
        name_list = driver.find_elements_by_class_name('name')
        rank_list = driver.find_elements_by_class_name('rank')
        point_list = driver.find_elements_by_class_name('point')

        for name, rank, point in zip(name_list[3:51], rank_list[1:51], point_list[3:51]):
            ramen_data_list.append([name.text, rank.text, point.text])
        page += 1

    ramen_data_df = pd.DataFrame(ramen_data_list, columns=['name', 'rank', 'point'])
    ramen_data_df.to_csv(f"ramen_data{p-(n-1)}to{p}.csv", index=False)