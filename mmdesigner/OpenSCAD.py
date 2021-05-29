import subprocess

class OpenSCAD(object):

    def __init__(self):
        pass

    def get_version(self):
        result = subprocess.run(['openscad','--version'], capture_output=True)
        version = result.stderr.decode().split()[2]
        return version

if __name__ == '__main__':
    mgr = OpenSCAD()
    mgr.get_version()


