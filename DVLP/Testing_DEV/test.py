from time import sleep
from tqdm import tqdm
for i in tqdm(range(10), desc="Loading...", ascii=False, ncols=75, bar_format="{l_bar}{bar:20}{r_bar}"):
    sleep(1)