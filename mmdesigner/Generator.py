import os
import json
from mmdesigner.TreeWalker import TreeWalker
from mmdesigner.OpenSCAD import OpenSCAD
from openpyxl import Workbook

count = 0


class Generator(object):
    """Management class for generating analysis files"""

    def __init__(self, root):
        """Class constructor normalizes input model path"""
        self.root = os.path.abspath(root)
        self.ext = '.scad'

    def gen_stl(self, param):
        """Generate a single STL file"""
        osc = OpenSCAD()
        osc.gen_stl(param)

    def gen_property(self, param):
        """Generate a single mass property file"""
        osc = OpenSCAD()
        osc.get_properties(param)

    def process_parts(self, run_type):
        """Process only part files"""
        if run_type == "stl":
            tw = TreeWalker(self.root, "scad", self.gen_stl)
        else:
            tw = TreeWalker(self.root, "stl", self.gen_property)
        tw.process_leaf_files()

    def process_all(self, run_type):
        """Generate part and assembly files"""
        if run_type == "stl":
            tw = TreeWalker(self.root, "scad", self.gen_stl)
        else:
            tw = TreeWalker(self.root, "stl", self.gen_property)
        tw.process_files()

    def gen_json(self, param):
        """Load JSON data file"""
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
                row.append(float(jdata[key]))
            self.ws.append(row)
            count += 1

    def gen_excel(self, model_name):
        """Generate design Excel file"""
        global count
        wb = Workbook()
        self.ws = wb.active
        fname = os.path.join(self.root, model_name)
        fname += ".xlsx"
        tw = TreeWalker(self.root, "json", self.gen_json)
        count = 0
        tw.process_files()
        print("Workbook:", fname)
        wb.save(fname)

    def count_inv(self, ext):
        pass

    def inventory(self):
        """scan model directory counting files"""
        num_assemblies = 0
        num_parrs = 0
        num_data = 0
        num_stl = 0
        num_json = 0

        for dirpath, dirnames, filenames in os.walk(self.root):
            for f in filenames:
                path = os.path.abspath(os.path.join(dirpath, f))


if __name__ == '__main__':
    root = "tests/test_data/model"
    gen = Generator(root)
    gen.process_all("stl")
    gen.process_all("mass")
    gen.gen_excel("model")
