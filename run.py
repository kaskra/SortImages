import argparse

from common.loader import Loader
from common.image_processor import ImageProcessor


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", nargs="+", type=str, default=".",
                        required=True, help="an input path to a directory")
    parser.add_argument("-o", "--output", type=str, default=".",
                        required=True, help="an output path to a directory")
    parser.add_argument("-e", "--exts", nargs="+", type=str,
                        required=True, help="a list of extensions to work on")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    file_extensions = args.exts

    # import all images found at path and below
    loader = Loader(path=input_path,
                    file_extensions=file_extensions)
    files = loader.load()

    sorter = ImageProcessor(files)
    sorter.out(output_path)
