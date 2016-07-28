import re

def generate(postinst,api_level,archive):
    rep = {"$X" : api_level, "$Y" : archive}
    f = open("maintscript/google-android-platform-X-installer.postinst.ex")
    i = f.read()
    o = open(postinst, "w")
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    i = pattern.sub(lambda m: rep[re.escape(m.group(0))], i)
    o.write(i)
    o.close()
    print ":... \033[0;34mGENERATED\033[0m google-android-platform-"+api_level+"-installer.postinst"
