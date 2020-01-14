import re
txt='''
.bash_profile # Δεν κάνει match
workspace.doc # Δεν κάνει match
img0912.jpg # group(1)--> 'img0912', group(2) --> 'jpg'
updated_img0912.png # group(1)--> 'updated_img0912', group(2) --> 'png'
documentation.html # Δεν κάνει match
favicon.gif # group(1)--> 'favicon', group(2) --> 'gif'
img0912.jpg.tmp # Δεν κάνει match
'''
matches=re.finditer(r'(.*)\.(jpg|png|gif)',txt)
for match in matches:
    print('group(1)--->',match.group(1),'group(2)--->',match.group(2))