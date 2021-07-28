import time
from tqdm import tqdm

def loading():
    for perc in tqdm(range(100), desc="Loading...", ascii=False, ncols=75):
        time.sleep(0.10)
    print("Loading successfully!")

if __name__ == "__main__":
    loading()