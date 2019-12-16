'''
Created on Nov 24, 2019
=> Google Interview:
    -> Ceo needs to find the total time for all 
    -> employees to recieve the news he sends out
    -> Each employee has a time value. Find Total Time! 
@author: thann
'''
class Node(self, children, time):
	self.children = children
	self.time = time
	

def get_total_time(node, time):
	if node.children is None:
		return time
	highestTime = node.child[0].time
	highestNode = node.child[0]
	for i in node.children:
		if get_total_time(node.child[i], time+=node.child[i].time) > highestTime:
			highestTime = get_total_time(node.child[i], time+=node.child[i].time)
			highestNode = node.child[i]

	return highestTime #get_total_time(highestNode, highestTime)
