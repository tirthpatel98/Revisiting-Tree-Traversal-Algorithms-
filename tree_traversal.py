import sys

class Node:
	def __init__(self,value=None):
		self.value = value
		self.left_child = None
		self.right_child = None 

class BST:
	def __init__(self):
		self.root = None

	def insert(self,value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value,self.root)


	def _insert(self,value,curr_root):
		if value<=curr_root.value:
			if curr_root.left_child!=None:
				self._insert(value,curr_root.left_child)
			else:
				curr_root.left_child = Node(value)

		else:
			if curr_root.right_child!=None:
				self._insert(value,curr_root.right_child)
			else:
				curr_root.right_child = Node(value)

	def inorder_print_tree(self):
		if self.root!= None:
			self._inorder_print_tree(self.root)

	def _inorder_print_tree(self,curr_root):
		if curr_root.left_child!=None:
			self._inorder_print_tree(curr_root.left_child)
		print(curr_root.value)
		if curr_root.right_child!=None:
			self._inorder_print_tree(curr_root.right_child)

	def pre_search(self):
		if self.root != None:
			self._pre_search(self.root)

	def _pre_search(self,curr_root):
		print(curr_root.value)
		if curr_root.left_child != None:
			self._pre_search(curr_root.left_child)
		if curr_root.right_child != None:
			self._pre_search(curr_root.right_child)

	def post_search(self):
		if self.root!=None:
			self._post_search(self.root)

	def _post_search(self, curr_root):
		if curr_root.left_child != None:
			self._post_search(curr_root.left_child)
		if curr_root.right_child != None:
			self._post_search(curr_root.right_child)
		print(curr_root.value)

	def dfs(self):
		if self.root != None:
			stack = []
			stack.append(self.root)
			self._dfs(self.root,stack)
	def _dfs(self,curr_root,stack):
		if curr_root.right_child!=None:
			stack.append(curr_root.right_child)
		if curr_root.left_child!=None:
			stack.append(curr_root.left_child)
		print(curr_root.value)
		stack.remove(curr_root)
		if len(stack)!=0:
			next_root = stack[-1]
			self._dfs(next_root,stack)

	def bfs(self):
		if self.root != None:
			queue = []
			queue.append(self.root)
			self._bfs(self.root,queue)
	def _bfs(self,curr_root,queue):
		print(curr_root.value)
		if curr_root.left_child != None:
			queue.append(curr_root.left_child)
		if curr_root.right_child != None:
			queue.append(curr_root.right_child)
		queue.remove(curr_root)
		if len(queue)!= 0:
			next_root = queue[0]
			self._bfs(next_root,queue)



if __name__ == '__main__':
	bst = BST()
	flag = 0
	while True:
		print("Select one of the following \n"
		 " 1. Insert \n"
		 " 2. Inorder Print \n"
		 " 3. Preorder Print \n"
		 " 4. Postorder Print \n"
		 " 5. DFS \n"
		 " 6. BFS \n"
		 " 7. Exit"
		 )
		for line in sys.stdin:
			in_val = line.rstrip()
			
			if in_val == '7': 
				flag = 1
				break
			elif in_val == '1':
				print("enter val")
				for line1 in sys.stdin:
					bst.insert(int(line1.rstrip()))
					break
			elif in_val == '2':
				print("Printing inorder tree")
				bst.inorder_print_tree()
			elif in_val == '3':
				print("Printing pre-order tree")
				bst.pre_search()
			elif in_val == '4':
				print("Printing post-order tree")
				bst.post_search()
			elif in_val == '5':
				print("Printing DFS")
				bst.dfs()
			elif in_val == '6':
				print("Printing BFS")
				bst.bfs()

		if flag == 1:
			break 

