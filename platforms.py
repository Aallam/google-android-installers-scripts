import re, os.path, glob

def get(soup,pif):
    pkg_dir = os.path.join(glob.glob(os.path.expanduser(pif))[0], '')
    print pkg_dir
    # Get platforms list
    platforms_list = soup.findAll('platform') 
    # Show results
    for platform in platforms_list:
        print ("- "+platform.description.string)
        api_level = platform.find('api-level').string
        version =  platform.version.string
        archive = platform.archives.archive.url.string
        revision = re.search("_r[0-9]*",archive).group()[2:]
        sha1 =  platform.archives.archive.checksum.string
        binary = "google-android-platform-"+api_level+"-installer"
        install = pkg_dir+"debian/"+binary+".install"
        postinst = pkg_dir+"debian/"+binary+".postinst"
        sha1sum = pkg_dir+"for-postinst/"+archive+".sha1"
        current_sha1sum = ""

        # Update <package>.install
        if os.path.isfile(install):
            f = open(install)
            current_sha1sum = re.search("(android|platform)-[0-9]*_r[0-9]*.zip.sha1",f.readlines()[1]).group()
            f.seek(0)
            match = re.search("[0-9]*_r[0-9]*",f.readlines()[1])
            if match.group() == api_level+"_r"+revision:
                print "\033[0;32mOK\033[0m "+binary+".install"
            else:
                print "\033[0;33mOUTDATED\033[0m "+binary+".install"
                f.seek(0)
                i = f.read()
                o = open(install,"w")
                o.write(re.sub(match.group(), api_level+"_r"+revision, i))
                print "\tUpdated from "+match.group()+" to "+api_level+"_r"+revision
                o.close()
        else:
            print "\033[0;31mNOT EXIST\033[0m "+binary+".install"

        # Update <archive>.sha1
	current_sha1sum_file = pkg_dir+"for-postinst/"+current_sha1sum
        if os.path.isfile(current_sha1sum_file):
            f = open(current_sha1sum_file)
            current_sha1 = re.search(r'\b[0-9a-f]{5,40}\b',f.readlines()[0]).group()
            if current_sha1sum_file != sha1sum:
                # Remove outdated sha1 file
                try:
		    os.remove(current_sha1sum_file)
	        except OSError:
		    pass
                # Generate new sha1 file
                if os.path.isfile(sha1sum):
                    print "\033[0;32mOK\033[0m "+archive+".sha1"
                else:
                    o = open(sha1sum,'w+')
                    o.write(sha1+"  "+archive)
                    print "\t"+archive+".sha1 generated"
                    o.close()
            elif current_sha1 != sha1:
                f.seek(0)
                i = f.read()
                o = open(current_sha1sum_file,"w")
                o.write(re.sub(current_sha1, sha1, i))
                print "\t\033[0;33mUPDATED\033[0m SHA1 checksum"
                o.close()

        # Update <package>.postinst
        if os.path.isfile(postinst):
            f = open(postinst)
            match = re.search(r'\b\d+\b',f.readlines()[5])
            if int(match.group()) == int(revision):
                print "\033[0;32mOK\033[0m "+binary+".postinst"
            else:
                print "\033[0;33mOUTDATED\033[0m "+binary+".postinst"
                f.seek(0)
                i = f.read()
                o = open(postinst,"w")
                o.write(re.sub(match.group(), revision, i))
                print "\tUpdated from revision "+match.group()+" to "+revision
                o.close()
        else:
            print "\033[0;31mNOT EXIST\033[0m "+binary+".postinst"
