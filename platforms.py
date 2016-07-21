
def get(soup):
    #Get platforms list
    platforms_list = soup.findAll('platform') 
    #Show results
    for platform in platforms_list:
        print "- %s" % platform.description.string
        print "\tAPI-Level: %s" % platform.find('api-level').string
        print "\tVersion: %s" % platform.version.string
        print "\tRevision: %s" % platform.revision.string
        print "\tArchive: %s" % platform.archives.archive.url.string
        print "\tSHA1: %s" % platform.archives.archive.checksum.string
