import Image
import os
from Image import EXTENT

filelist = os.listdir('./myimage')


for img in filelist:
	tmp = Image.open('myimage/' + img)
	if tmp.size[0] > tmp.size[1]:
		offset = int(tmp.size[0] - tmp.size[1]) / 2
		result = tmp.transform((tmp.size[1], tmp.size[1]), EXTENT, (offset, 0, int(tmp.size[0] - offset), tmp.size[1]))
	else:
	    offset = int(tmp.size[1] - tmp.size[0]) / 2
	    result = tmp.transform((tmp.size[0], tmp.size[0]), EXTENT, (0, offset, tmp.size[0], (tmp.size[1] - offset)))
	result.save('thumb/' + img)