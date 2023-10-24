"""

Reading Data From JSON


"""
from dotenv import load_dotenv
from functools import lru_cache
import os
import json

load_dotenv()

root_dir = (
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        + "\\"
        + "features"
)


class ObjFromJson:

    @staticmethod
    @lru_cache
    def open_json_file_return_data() -> dict:
        """Opens the json files and return data"""
        with open(root_dir + "\\" + "objectsrepository" + "\\" + "shopping.json") as f:
            data = json.load(f)
        f.close()
        return data

    def get_selected_locator(self, value):
        return self.open_json_file_return_data()[value]

