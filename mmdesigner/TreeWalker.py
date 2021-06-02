import os


class TreeWalker(object):
    """Model tree action class"""

    def __init__(self, model_path, ext='', callback=None):
        """Register user model path, extension, and callback"""
        self.model_path = self.check_path(model_path)
        self.callback = callback
        self.ext = ext

    def check_path(self, model_path):
        """Confirm proposed model path contains at least one .scad file"""
        if os.path.isdir(model_path):
            files = os.listdir(model_path)
            for f in files:
                if f.endswith(".scad"):
                    return model_path
        else:
            return None

    def get_model_path(self):
        """Return current model path"""
        return self.model_path

    def get_extension(self):
        """Return current extension"""
        return self.ext

    def get_callback(self):
        """Return the current callback"""
        return self.callback

    def get_file_list(self):
        """Return list of files with selected extension"""
        files = []
        for dirpath, dirnames, filenames in os.walk(self.model_path):
            for f in filenames:
                path = os.path.abspath(os.path.join(dirpath, f))
                if path.endswith(self.ext):
                    files.append(path)
        return files

    def get_leaf_file_list(self):
        """Return list of leaf files (parts)"""
        llist = []
        for dirpath, dirnames, filenames in os.walk(self.model_path):
            if len(dirnames) != 0: continue
            for f in filenames:
                path = os.path.abspath(os.path.join(dirpath, f))
                if path.endswith(self.ext):
                    llist.append(path)
        return llist

    def process_files(self):
        """Run callback on all selected files"""
        files = self.get_file_list()
        for f in files:
            self.callback(f)


    def process_leaf_files(self):
        """Run callback on only leaf files"""
        files = self.get_leaf_file_list()
        for f in files:
            print("Processing:", f)
            self.callback(f)


    def clean(self, ext):
        """delete files with specified extension from tree"""
        current_ext = self.ext
        self.ext = ext
        files = self.get_file_list()
        for f in files:
            os.remove(f)
        self.ext = current_ext


count = 0
def bump_count(path):
    global count

    count += 1  # pragma: no cover

if __name__ == "__main__":
    tw = TreeWalker("../tests/test_data/model","scad",bump_count)
    print(tw.get_model_path)
    files = tw.get_leaf_file_list()
    print(files)
    count = 0
    tw.process_files()
    print(count)

