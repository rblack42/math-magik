import os
import json
from mmdesigner.TreeWalker import TreeWalker
from mmdesigner.OpenSCAD import OpenSCAD
from openpyxl import Workbook

count = 0;

class Generator(object):

    def __init__(self, root):
        self.root = os.path.abspath(root)

    def gen_stl(self, param):
        osc = OpenSCAD()
        osc.gen_stl(param)


    def gen_properties(self, param):
        osc = OpenSCAD()
        osc.get_properties(param)

    def run_leaf_stl(self, run_type):
        if run_type == "stl":
            tw = TreeWalker(self.root, "scad", self.gen_stl)
        else:
            tw = TreeWalker(self.root, "stl", self.gen_properties)
        tw.process_leaf_files()

    def run_all(self, run_type):
        if run_type == "stl":
            tw = TreeWalker(self.root, "scad", self.gen_stl)
        else:
            tw = TreeWalker(self.root, "stl", self.gen_properties)
        tw.process_files()

    def print_json(self, param):
        global count

        part = param[len(self.root):]
        with open(param) as fin:
            jdata = json.load(fin)
            if count == 0:
                labels = []
                labels.append("part")
                for key in jdata:
                    labels.append(key)
                self.ws.append(labels)
            row = []
            row.append(part)
            for key in jdata:
                row.append(jdata[key])
            self.ws.append(row)
            count += 1

    def gen_excel(self):
        global count
        wb = Workbook()
        self.ws = wb.active
        tw = TreeWalker(self.root, "json", self.print_json)
        count = 0
        tw.process_files()
        wb.save(os.path.join(self.root, "model.xlsx"))


if __name__ == '__main__':
    root = "tests/test_data/model"
    gen = Generator(root)
    gen.run_all("stl")
    gen.run_all("mass")
    gen.gen_excel()


