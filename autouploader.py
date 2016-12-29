from os import listdir, path
from os.path import isfile, join
from time import localtime, strftime
from sys import argv

script_path = path.dirname(path.realpath(__file__))
if len(argv)>1:
    dir_path = argv[1]
else:
    dir_path = script_path

print dir_path
filelist = [f for f in listdir(dir_path) if path.isfile(path.join(dir_path, f))]

imagelist = []
for f in filelist:
    extension = path.splitext(path.join(dir_path,f))[1]
    if extension.lower()==".jpg" or extension.lower()==".jpeg":
        imagelist.append(f)
    if extension.lower()==".png":
        imagelist.append(f)
print imagelist

template = open(path.join(script_path,"template.html"), 'r')
with open(path.join(dir_path,"gallery.html"), 'w') as gallery:
    for line in template:
        if line == "<!--START_AUTOUPLOADER-->\n":
            for f in imagelist:
                create_time = strftime("%Y%m%d%H%M%S000", localtime())
                gallery.write('<div _canonical_uri="./'+f+'" created="'+create_time+'" modified="'+create_time+'" tags="" title="'+f+'" type="image/jpeg">\n')
                gallery.write('<pre></pre>\n')
                gallery.write('</div>\n')

        gallery.write(line)

gallery.close()
template.close()

print ("Images in "+dir_path+" are uploaded to gallery.html wiki successfully")
