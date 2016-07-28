def generate(install,api_level,archive):
    o = open(install, "w")
    o.write("for-postinst/Makefile  usr/share/google-android-platform-"+api_level+"-installer/\n")
    o.write("for-postinst/"+archive+".sha1  usr/share/google-android-platform-"+api_level+"-installer/")
    o.close()
    print ":... \033[0;34mGENERATED\033[0m google-android-platform-"+api_level+"-installer.install"
