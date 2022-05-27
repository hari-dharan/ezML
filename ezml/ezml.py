from os import remove
from .processing import remove_groupby_outliers

class EasyML(object):
    def __init__(self):
        pass

    def test(self):
        print("hi")
    
    def remove_groupby_outliers(self, df, by, col, scale):
        return remove_groupby_outliers(df, by, col, scale)

    def groupby_fillna(self):
        pass