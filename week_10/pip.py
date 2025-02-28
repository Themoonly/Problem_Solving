import networkx as nx
import matplotlib.pyplot as plt
network = nx.Graph() # สร้างกราฟเปล่า
color_list = ["gold","red","violet","purple","green"] # สร้างตัวแปรกำหนดสี 
plt.figure(figsize=(8, 6)) #กำหนดขนาด
plt.title("Example of graph representtion", size=15) 

network.add_nodes_from([1, 2, 3, 4, 5]) # เพิ่ม node
network.add_edge(1,2) # add edge 1 to 2
network.add_edge(1,3) # add edge 1 to 2
network.add_edge(2,3) # add edge 1 to 2
network.add_edge(4,5) # add edge 1 to 2
network.add_edge(4,3) # add edge 1 to 2
network.add_edge(5,3) # add edge 1 to 2





print(f"This network has now {network.number_of_nodes()} nodes.") # แสดงข้อความใน commandline
# output (name graph, color, node_name)
nx.draw_networkx(network,node_color=color_list, with_labels=True)
plt.show() # วาดกราฟ