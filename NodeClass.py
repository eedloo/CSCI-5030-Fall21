class Node:
   def _init_(self, data, output = None):
      self.left = None
      self.right = None
      self.options = data
      self.output = output
   def PrintTree(self):
      print(self.options)
