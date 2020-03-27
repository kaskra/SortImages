from PIL import Image, ExifTags
import os
import time
import shutil

import argparse

from common.loader import Loader


def get_dates(images):
    dates = {}
    for image in images:
        img = Image.open(image)
        exif = {ExifTags.TAGS[k]: v for k,
                v in img._getexif().items() if k in ExifTags.TAGS}

        date = exif['DateTime'][5:]
        date_obj = time.strptime(date, "%m:%d %H:%M:%S")
        key = f"{date_obj.tm_mon}:{date_obj.tm_mday}"
        if key not in dates:
            dates[key] = [(image, date_obj)]
        else:
            dates[key].append((image, date_obj))
    return dates


def image_output(image_at_day, output_path):
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    months = ["Januar", "Februar",
              "März", "April", "Mai",
              "Juni", "Juli", "August",
              "September", "Oktober",
              "November", "Dezember"]

    for key in image_at_day:
        images = image_at_day[key]
        month, _ = key.split(":")
        path = os.path.abspath(output_path + "/" +
                               month + "_" + months[int(month)-1])
        if not os.path.isdir(path):
            os.makedirs(path)
        for image, date in images:
            date = f"{date.tm_mon}{date.tm_mday}_{date.tm_hour}{date.tm_min}{date.tm_sec}"
            image_dst = path + "\\" + date
            if os.path.isfile(image_dst):
                image_dst += "_2"
            image_dst += ".jpg"
            shutil.copy(image, image_dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default=".",
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

    dates = get_dates(files)
    image_output(dates, output_path)
