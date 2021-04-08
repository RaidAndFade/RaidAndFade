import glob
import os

icons = {}

for x in os.walk("icons"):
    for y in glob.glob(os.path.join(x[0], '*.svg')):
        iconpath,iconfile = os.path.split(y)
        iconcategory=iconpath[6:]

        if iconcategory not in icons: icons[iconcategory]=[]

        icons[iconcategory].append(iconfile[:-4])

categories = ['languages','technologies','applications','environments']

for cat in categories:
    print(f"### {cat[0].upper()}{cat[1:]}")
    for i in icons[cat]:
        iname = i.split("-")[-1]
        print(f"<img src='./icons/{cat}/{i}.svg' height=32 title='{iname}'>",end=" ")
    print("\n")