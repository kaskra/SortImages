from PIL import Image, ExifTags
import time
import tqdm
import shutil
import os

from common.template.processor import Processor


class ImageProcessor(Processor):

    def __init__(self, data):
        super().__init__(data)
        self.EXTENSIONS = [".jpg", ".png", ".jpeg"]

        self.processed_data = None

        self.validate_data()

    def validate_data(self):
        super().validate_data()
        all_extensions = list(map(lambda p: '.'+p.split('.')
                                  [-1], self.data))
        exts_in_data = [e in self.EXTENSIONS for e in all_extensions]

        # Print warning any other than the approved extensions were found.
        if not all(exts_in_data):
            print(
                f"WARNING: {type(self).__name__} can only handle {self.EXTENSIONS} extensions.")
            print("WARNING: Moving forward with approved extensions only.")
            self.data = [p for p in self.data if '.' +
                         p.split('.')[-1] in self.EXTENSIONS]
            print(f"WARNING: Reduced data set to {len(self.data)} files.")

    def process(self):
        print("Begin processing...")
        processed_data = {}
        for image in tqdm.tqdm(self.data):
            img = Image.open(image)
            if img._getexif() is None:
                print(f"Skipped image {image}")
                continue
            exif = {ExifTags.TAGS[k]: v for k,
                    v in img._getexif().items() if k in ExifTags.TAGS}

            date = exif['DateTime'][5:]
            date_obj = time.strptime(date, "%m:%d %H:%M:%S")
            key = f"{date_obj.tm_mon}:{date_obj.tm_mday}"
            if key not in processed_data:
                processed_data[key] = [(image, date_obj)]
            else:
                processed_data[key].append((image, date_obj))
        print("Finished processing.")
        return processed_data

    def out(self, output_path):
        if not self.processed_data:
            print("Starting automatic processing.")
            self.processed_data = self.process()

        if not os.path.isdir(output_path):
            os.makedirs(output_path)

        # TODO extract to config file
        months = ["Januar", "Februar",
                  "März", "April", "Mai",
                  "Juni", "Juli", "August",
                  "September", "Oktober",
                  "November", "Dezember"]

        counter = 0
        print("Outputing...")
        for key in tqdm.tqdm(self.processed_data):
            images = self.processed_data[key]
            month, _ = key.split(":")
            path = os.path.abspath(output_path + "/" +
                                   month + "_" + months[int(month)-1])
            if not os.path.isdir(path):
                os.makedirs(path)
            for image, date in images:
                date = f"{date.tm_mon}{date.tm_mday}_{date.tm_hour}{date.tm_min}{date.tm_sec}"
                image_dst = path + "\\" + date
                # TODO extension should not be constant here
                if os.path.isfile(image_dst+".jpg"):
                    image_dst += "_2"
                # TODO extension should not be constant here
                image_dst += ".jpg"
                shutil.copy(image, image_dst)
                counter += 1
        print(f"Output {counter} files to {output_path}.")
