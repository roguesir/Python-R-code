# coding:utf-8


import networkx as nx 
import matplotlib.pyplot as plt
import csv

with open('node-8.csv','rb') as csvfile:
	reader = csv.DictReader(csvfile)
	column = [row['b'] for row in reader]
	id_tag0 = [row['id'] for row in reader]
#print column
id_tag = []
for item in id_tag0:
	id_tag.append(int(item))

# =================Setting node parameters====================
node_0 = []
node_1 = []
node_2 = []
node_3 = []
node_color = []
node_color_y = []
node_color_r = []
node_color_g = []
node_color_b = []
node_shape = []
node_shape_0 = []
node_shape_1 = []
node_shape_2 = []
node_shape_3 = []

for i in range(len(column)):
	if int(column[i]) == 0:
		pass
	elif int(column[i]) == 1:
		color = 'r'
		shape = 'o'
		node_1.append(i)
		node_color_r.append(color)
		node_shape_1.append(shape)
	elif int(column[i]) == 2:
		color = 'g'
		shape = 'o'
		node_2.append(i)
		node_color_g.append(color)
		node_shape_2.append(shape)
	else:
		color = 'b'
		shape = '*'
		node_3.append(i)
		node_color_b.append(color)
		node_shape_3.append(shape)
	node_color.append(color)
	node_shape.append(shape)
# ==============================================================


with open('node-8.csv','rb') as csvfile:
	reader = csv.DictReader(csvfile)
	column1 = [row['b'] for row in reader]
	id_tag1 = [row['id'] for row in reader]
#print column
id_tag11 = []
for item in id_tag1:
	id_tag11.append(int(item))



edge = []
with open('edge-8.txt','r') as f:  
	data = f.readlines()  
	for line in data:
		#print line
		line = tuple(line.replace('\r','').replace('\n','').replace('\t','').split(','))
		edge.append(line)
#print edge

# ===============Setting edge parameters=========================
edge_color = []
edge_style = []
'''
for item in edge:
	#print item
	if int(column1[int(item[0])]) == 0 or int(column1[int(item[1])]) == 0:
		pass
	elif int(column1[int(item[0])]) == 1 or int(column1[int(item[1])]) == 1:
		color = 'r'
		#style0 = 'dashdot'
		#color_r_list.append(color)
	elif int(column1[int(item[0])]) == 2 or int(column1[int(item[1])]) == 2:
		color = 'g'
		#style0 = 'dashed'
		#color_r_list.append(color)
	else:
		color = 'b'
		#style0 = 'dotted'
		#color_b_list.append(color)
	edge_color.append(color)
	#edge_style.append(style0)
'''

G = nx.Graph()
G.add_nodes_from(id_tag)
G.add_edges_from(edge)

#nx.draw(G,pos=nx.random_layout(G), nodelist = node_0, node_color = node_color_y, node_size=120, node_shape=node_shape_0)
#nx.draw(G,pos=nx.random_layout(G), nodelist = node_1, node_color = node_color_r, node_size=120, node_shape=node_shape_1)
#nx.draw(G,pos=nx.random_layout(G), nodelist = node_2, node_color = node_color_g, node_size=120, node_shape=node_shape_2)
#nx.draw(G,pos=nx.random_layout(G), nodelist = node_3, node_color = node_color_b, node_size=120, node_shape=node_shape_3)

nx.draw_networkx(G,pos=nx.random_layout(G),alpha=1,node_color=node_color,node_size=10,node_shape='o',edge_color='c',width=0.3,style='solid',font_size=10) 
#nx.draw_networkx(G,pos=nx.random_layout(G),nodelist = node_1,node_color=node_color,node_size=100,node_shape='o',style='dashdot') 
#nx.draw_networkx(G,pos=nx.random_layout(G),node_color=color_g_list,node_size=150,node_shape='^',style='dashed') 
#nx.draw_networkx(G,pos=nx.random_layout(G),node_color=color_b_list,node_size=150,node_shape='*',style='dotted') 

#plt.legend()
#nx.draw_networkx(G)
plt.show()



