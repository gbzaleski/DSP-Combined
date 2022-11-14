from Bio import Phylo 

tree = Phylo.read("tree.txt", "newick")
print(tree)
Phylo.draw_ascii(tree)
