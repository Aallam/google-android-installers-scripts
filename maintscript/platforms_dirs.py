def generate(dirs,api_level):
    f = open("maintscript/google-android-platform-X-installer.dirs.ex")
    i = f.read()
    o = open(dirs, "w")
    o.write(i.replace("$X",api_level))
    o.close()
    print ":... \033[0;34mGENERATED\033[0m google-android-platform-"+api_level+"-installer.dirs"
