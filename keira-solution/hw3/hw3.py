import random

class CountMinCut:

	def __init__(self):
		self.vertices_list = {}
		self.edge_list = []

	def _construct_graph(self, vertices_input):
		for vertices in vertices_input:
			nodes = vertices.strip().split("\t")
			node1 = str(nodes[0])
			current_vertix_edge = []
			for i in range(1, len(nodes)):
				edge = node1 + "_" + str(nodes[i])
				edge_rev = str(nodes[i]) + "_" + node1
				if (edge not in self.edge_list and edge_rev not in self.edge_list):
					self.edge_list.append(edge)
				elif (edge_rev in self.edge_list):
					edge = edge_rev
				current_vertix_edge.append(edge)
			self.vertices_list[node1] = current_vertix_edge
		# print(self.vertices_list)

	def _contraction(self):
		random.seed(2)
		s = random.randint(0, len(self.edge_list))
		del_edge = self.edge_list[s]
		print(del_edge)


if __name__ == "__main__":
	GRAPH_FILENAME = "../data/kargerMinCut.txt"
	in_file = open(GRAPH_FILENAME, 'r')
	with in_file as f:
		vertices_input = [str(line.strip()) for line in f.readlines()]
	count_min_cut = CountMinCut()
	count_min_cut._construct_graph(vertices_input)
	count_min_cut._contraction()