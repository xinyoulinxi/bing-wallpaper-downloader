from BingWallpaperDownloader import DownloadAllDayBingImg,DownLoadBingImg

import os
def main():
    print(os.listdir("./"))
    if not "bing_bg" in os.listdir("./"):
        os.makedirs("./bing_bg/")
    DownloadAllDayBingImg("./bing_bg/") # path, need last '/' char
    DownLoadBingImg("./")

if __name__ == "__main__":
    main()