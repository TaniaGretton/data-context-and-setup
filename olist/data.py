import os
import pandas as pd


class Olist:
    def get_data(self):

        """This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "csv")
        #creating file_names list
        all_files_names = os.listdir(path = csv_path,)
        file_names = list(filter(lambda f: f.endswith('.csv'), all_files_names))
        #creating key_names list
        key_names = []
        for x in file_names:
            if x[0:5] == "olist":
                key_names.append(x.replace("olist_","").replace("_dataset.csv",""))
            else:
                key_names.append(x.replace(".csv",""))

        #creating a dictionary
        data = {}
        for key,file in zip(key_names,file_names):
            data[key] = pd.read_csv(os.path.join(csv_path, file))

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
