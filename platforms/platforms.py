import urllib3, sys, argparse
from bs4 import BeautifulSoup

#Metadata
progversion = "0.1"
progname="platforms-fetcher"
progdesc="Parser for repository-11.xml to fetch SDK Platforms list"

parser = argparse.ArgumentParser(prog=progname, description=progdesc)
parser.add_argument("url", metavar="url", type=str, nargs=1,
                    help="repository-11.xml mirror")
args = parser.parse_args()

#Fetch XML File
hdr = {"User-Agent": "Mozilla/5.0"}
print("Fetching "+args.url[0])
http = urllib3.PoolManager()
req = http.request('GET',args.url[0],headers=hdr)
if req.status != 200:
   print "HTTP Error: %s" % req.status
   quit()

soup = BeautifulSoup(req.data, "xml")

#Get platforms list
platforms_list = soup.findAll('platform') 

for platform in platforms_list:
    print "- %s" % platform.description.string
    print "\tAPI-Level: %s" % platform.find('api-level').string
    print "\tVersion: %s" % platform.version.string
    print "\tRevision: %s" % platform.revision.string
    print "\tArchive: %s" % platform.archives.archive.url.string
    print "\tSHA1: %s" % platform.archives.archive.checksum.string
