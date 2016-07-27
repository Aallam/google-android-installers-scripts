## Required:
* Pyhton
* Beautiful Soup 4 : `apt install python-bs4`

## Run
* usage: `python fercher.py [-h] [-p -platforms] [-n -ndk] url platforms_installers`
* examples: 
  * Platforms and NDK : `python fetcher.py https://dl.google.com/android/repository/repository-11.xml ~/google-android-platform-installers`
  * Platforms Only: `python fetcher.py -platforms https://dl.google.com/android/repository/repository-11.xml ~/google-android-platform-installers`
  * NDK only `python fetcher.py -ndk https://dl.google.com/android/repository/repository-11.xml`
