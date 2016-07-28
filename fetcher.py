import urllib3, sys, argparse
import platforms, ndk
from bs4 import BeautifulSoup

#Metadata
progversion = "0.1"
progname="platforms-fetcher"
progdesc="Parser for repository-11.xml to fetch SDK Platforms list"

parser = argparse.ArgumentParser(prog=progname, description=progdesc)
parser.add_argument("url", metavar="url", type=str, nargs=1,
                    help="repository-11.xml mirror")
parser.add_argument("pi", metavar="pi", type=str, nargs=1,
                    help="google-android-platform-installers folder")
parser.add_argument("-platforms", metavar="-p", action='store_const',
                    const=platforms, help="XML file name for output")
parser.add_argument("-ndk", metavar="-n", action='store_const',
                    const=ndk, help="XML file name for output")
args = parser.parse_args()

#Fetch XML File
hdr = {"User-Agent": "Mozilla/5.0"}
print(("Fetching "+args.url[0]))
http = urllib3.PoolManager()
req = http.request('GET',args.url[0],headers=hdr)
if req.status != 200:
   print("HTTP Error: %s" % req.status)
   quit()

soup = BeautifulSoup(req.data, "xml")

#Get results
if args.platforms:
    platforms.get(soup,args.pi[0])
elif args.ndk:
    ndk.get(soup)
else:
    platforms.get(soup)
    ndk.get(soup)
