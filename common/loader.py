from PIL import Image, ExifTags
import os


class Loader:
    def __init__(self, path=".", file_extensions=[".jpg"]):
        self.file_extensions = self.check_extension(file_extensions)

        if path is str:
            self.path = [path]
        else: 
            self.path = path

        for p in self.path:
            if not os.path.isdir(os.path.abspath(p)):
                raise NotADirectoryError(
                    f"Could not find directory: {os.path.abspath(p)}")
           
            print(
                f"Importing {self.file_extensions} files from {os.path.abspath(p)} ...")

    def check_extension(self, file_extensions):
        """Strips extension string, adds a dot if not already there 
        and lowercases the extension.
        """

        def _check_ext(extension):
            ext = extension.strip()
            if ext[0] == ".":
                return ext.lower()
            return f".{ext}".lower()

        return [_check_ext(
            ext) for ext in file_extensions]

    def load(self):
        """Loads every file with the given file extensions
        on the given path or below. 
        """
        found_files = []
        for p in self.path:
            for root, dirs, files in os.walk(p):
                for file in files:
                    if os.path.splitext(file)[1].lower() in self.file_extensions:
                        found_files.append(os.path.abspath(
                            "{}/{}".format(root, file)))
        print(f"Loaded {len(found_files)} files.")
        return found_files
