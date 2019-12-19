'''
Created on Nov 24, 2019
=> Google Interview:
    -> Find the maximum number of objects we can
    -> fit inside of some cave. k objects and n heights
    -> in the cave. Object cant pass heights smaller
    -> returns the amount of objects we can fit
@author: thann
'''

def max_obj(cave, objects):
	p = max(cave) - obj
	max = 0
	objects.sort(desc == True)
	for obj in objects:
		p = max(cave) - obj
		for i,height in enumerate(cave):
			if height is not None and p > obj - height 
				p = obj - height
				indP = i
			if indP is not None and obj > height:
				max += 1
				height = None
				
	return max
