import os
import json

MODEL = "/Users/rblack/_dev/math-magik-lpp/scad/math-magik-lpp"

class WeightBalance(object):

    def __init__(self, model_path):
        self.model_path = os.path.abspath(model_path)
        assert os.path.isdir(self.model_path)

    def _scan(self):
        print("processing", self.model_path)
        self.model_weight = 0
        for dirpath, dirnames, filenames in os.walk(self.model_path):
            parts = dirpath.split('/')
            indent = len(parts) * "  "
            component = parts[-1]
            if len(dirnames) > 0:
                ctype = 'assembly'
            else:
                ctype = 'part'
            print(indent, ctype, component)
            if ctype == "part":
                data_path = dirpath + '/' + component + '_data.scad'
                json_path = dirpath + '/' + component + '.json'
                density = float(self.get_density(data_path))
                volume = float(self.get_volume(json_path))
                print(indent, density, volume)
                self.model_weight += density / (12*12*12)* 493 * abs(volume)

            print("Calculated weight:", self.model_weight)

    def get_density(self, data_path):
        density = 0
        try:
            fin = open(data_path,'r')
        except:
            print("No data file found:", data_path)
            return -1
        lines = fin.readlines()
        for line in lines:
            if "density" in line:
                d,density = line.split("=")
                density.strip()
        return density[:-2]

    def get_volume(self, json_path):
        volume = 0
        try:
            fin = open(json_path,'r')
        except:
            print("No mass data file found:", json_path)
            return -1
        with open(json_path) as fin:
            data = json.load(fin)
            volume = data["volume"]
        return volume

    def run(self):
        self._scan()

if __name__ =='__main__':
    wb = WeightBalance(MODEL)
    wb.run()

