import re

def get(soup):
    #Get platforms list
    ndk_archive = soup.ndk.archives.archive.find_next_sibling('archive')
    #Show result
    print "Google Android NDK %s :" % soup.ndk.revision.string
    print "\tRevision: %s" % re.search("android-ndk-r(.+?)-linux-x86_64.zip",ndk_archive.url.string).group(1)
    print "\tArchive: %s" % ndk_archive.url.string
    print "\tSHA1: %s" % ndk_archive.checksum.string
