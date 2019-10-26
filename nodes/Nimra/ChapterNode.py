# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import os
import shutil

from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types
from lm.common.util.Utils import Utils

from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Path import Path

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ChapterNode(HierNode):
    # def add(self, child):
    #     return super().add(Types.assertType(child, [
    #         ChapterNode,
    #         # HierNode,
    #         LeafNode,
    #     ]))
    # def liftChapters(self):
    #     new_children = []
    #     for child in self.children:
    #         if Types.isType(child, ChapterNode):
    #             child.liftChapters()
    #             new_children.extend(child.children)
    #         else:
    #             new_children.append(child)
    #     self.children = []
    #     self.tag_map = {}
    #     [self.add(a) for a in new_children]
    def addTopicGroup(self, new_nodes, topic_group):

        if len(topic_group) == 0:
            return

        # (
        #     pa()
        #     .addx("new_nodes", new_nodes)
        #     .addx("topic_group", topic_group)
        #     .ppprint()
        # )

        new_node = ChapterNode(self.getPathname())
        [new_node.add(a) for a in topic_group]
        new_nodes.append(new_node)

        topic_group.clear() # = []

    def liftChapters(self):

        new_nodes = []
        topic_group = []

        for child in self.children:
            if Types.isType(child, ChapterNode):
                self.addTopicGroup(new_nodes, topic_group)
                for lifted_node in child.liftChapters():
                    new_node = ChapterNode("%s%s" % (
                        self.getPathname(),
                        lifted_node.getPathname(),
                    ))
                    [new_node.add(a) for a in lifted_node.children]
                    new_nodes.append(new_node)
                    # pa().addx("new_node", new_node).ppprint()
                    # print("** chapter title = %s **" % new_node.title)
            else:
                topic_group.append(child)
        self.addTopicGroup(new_nodes, topic_group)

        # >>> hack >>>
        if len(new_nodes) == 0:
            new_nodes.append(self)
        # <<<

        return new_nodes
    # def toNbf(self, top_dirname, sub_prefix_index):
    #     leaf_nodes = self.getLeafs()
    #     [a.toNbf(top_dirname, i, self.getPathname())
    #      for i, a in enumerate(leaf_nodes)]
    def toNbf(self, top_dirname, sub_prefix_index, sub_prefix_str = None):

        # leaf_paths = self.getLeafPaths(Path())
        # if len(leaf_paths) == 0:
        #     return super().toNbf(top_dirname, sub_prefix_index, sub_prefix_str)

        # ~~~~~~~~ verify top dir ~~~~~~~~
        if not os.path.isdir(top_dirname):
            Utils.todo("Directory not found.")

        # ~~~~~~~~ remove/create sub dir ~~~~~~~~
        sub_dirname = os.path.join(
            top_dirname,
            self.getPrefixname(sub_prefix_index, sub_prefix_str),
        )
        shutil.rmtree(sub_dirname, True)
        os.mkdir(sub_dirname)

        print("processing '%s'" % sub_dirname)

        # ~~~~~~~~ children ~~~~~~~~
        # leaf_nodes = self.getLeafs()
        # [a.toNbf(sub_dirname, i) for i, a in enumerate(leaf_nodes)]
        
        leaf_paths = list(filter(
            lambda a : Types.isType(a.getLeaf(), LeafNode),
            self.getLeafPaths(Path()),
        ))
        # if len(leaf_paths) > 0:
        #     pa().addx("leaf_paths", leaf_paths).ppprint()
        for index, path in enumerate(leaf_paths):
            path_strs = [a.getPathname() for a in path.nodes]
            path_strs = path_strs[1:-1] if len(path_strs) <= 3 else path_strs[1:-2]
            path_str = "_".join(path_strs) if len(path_strs) else None
            # if path_str:
            #     pa().addx("path_strs", path_strs).ppprint()
            leaf = path.getLeaf()
            leaf.toNbf(sub_dirname, index, path_str)

        # # ~~~~~~~~ debug ~~~~~~~~
        # pa().add(
        #     "top_dirname", top_dirname,
        #     "sub_dirname", sub_dirname,
        # ).ppprint()


# eof
