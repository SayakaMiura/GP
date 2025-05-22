import pandas as pd
from ete3 import Tree, TreeStyle, TextFace
import sys

def clone_tree(presence, tree_file,clone_path,samp_tree):
 cpdf = pd.read_csv(presence, sep='\t', index_col='Tumor')
 tree = Tree(tree_file)
 row_tree = Tree(samp_tree)
 ordered_rows = [leaf.name for leaf in row_tree.iter_leaves()]
 ordered_rows = [row for row in ordered_rows if row in cpdf.index]
 cpdf = cpdf.loc[ordered_rows]

 tcn = cpdf.columns[0]
 fsn = None
 for leaf in tree.iter_leaves():
    if leaf.name in cpdf.columns:
        prd = cpdf[leaf.name].dropna()

        fv = prd.iloc[0]
        sn = prd.name

     #   print("First value:", fv)
    #    print("Series name:", sn)

        if fsn is None:
            fsn = sn

     #   print("First series name encountered:", fsn)

        tcn = fsn
        i = 0
        for t, p in prd.items():
            if leaf.name == tcn:
                # Add Tumor ID (always black)
                id_face = TextFace(f"{t}", fgcolor="black")
                id_face.margin_bottom = 1
                leaf.add_face(id_face, column=i, position="aligned")
              #  i += 1

            # Add value with conditional coloring
            val_color = "black" if p > 0 else "white"
            val_face = TextFace(f"{p:.3f}", fgcolor=val_color)
            val_face.margin_bottom = 5
            val_face.margin_top = 5
            val_face.margin_right = 10

            leaf.add_face(val_face, column=i, position="aligned")
            i += 1

 ts = TreeStyle()
 ts.show_scale = True
 ts.show_leaf_name = True
 ts.show_branch_length = False
 ts.show_branch_support = False

 tree.render(clone_path, tree_style=ts)


def tumor_tree(presence, tree_file,tree_path):
    cpdf = pd.read_csv(presence, sep='\t', index_col='Tumor')
    cpdf = cpdf.T
    tree = Tree(tree_file)
    fsn = None
    for leaf in tree.iter_leaves():
        if leaf.name in cpdf.columns:
            prd = cpdf[leaf.name].dropna()

            fv = prd.iloc[0]
            sn = prd.name

            print("First value:", fv)
            print("Series name:", sn)

            if fsn is None:
                fsn = sn

            print("First series name encountered:", fsn)

            tcn = fsn
            i = 0
            for t, p in prd.items():
                color = "blue" if p > 0 else "black"

                l = f"{p:.3f}"

                if leaf.name == tcn:
                    l = f" {t}\n{l}"

                pf = TextFace(l, fgcolor=color)
                pf.margin_bottom = 5
                pf.margin_top = 5
                pf.margin_right = 10

                leaf.add_face(pf, column=i,
                              position="aligned")
                i += 1

    ts = TreeStyle()
    ts.show_scale = False
    ts.show_leaf_name = True
    ts.show_branch_length = True
    ts.show_branch_support = True
    tree.render(tree_path, tree_style=ts)

