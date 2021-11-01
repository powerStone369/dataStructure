from LinkedBinaryTree import LinkedBinaryTree

test = LinkedBinaryTree()
root = test._add_root(37)
r_l = test._add_left(root,20)
r_l_r = test._add_right(r_l,34)
r_l_r_l = test._add_left(r_l_r,25)
r_r = test._add_right(root,46)
r_r_l = test._add_left(r_r,39)
r_r_r = test._add_right(r_r,60)
r_r_r_l = test._add_left(r_r_r,55)
r_r_r_r = test._add_right(r_r_r,72)

for p in test.positions():
    print(p.element())
