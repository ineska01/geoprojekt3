import geopandas as gpd
from shapely.geometry import box
import fiona
from grid_engine import get_grid
import pandas as pd

class GridMaker:
    def __init__(self, dense, input_files):
        self.dense = dense
        self.input_files = input_files
        self.loaded_geojson = None
        self.get_crs = None
        self.upper_left = None
        self.lower_right = None
        self.merged_geojson = None
        
    def load_geojson(self):
        self.loaded_geojson = gpd.read_file(self.input_files)
        self.loaded_geojson = self.loaded_geojson.to_crs('EPSG:3857')
    def get_value(self):
        xmin, ymin, xmax, ymax = self.loaded_geojson.total_bounds
        self.upper_left = ymin, xmax
        self.lower_right = ymax, xmin
        
    def make_grid(self):
        grid = get_grid(self.upper_left, self.lower_right, self.dense)
        grid.to_file('siatka_22.geojson', driver='GeoJSON')
    
    def merge_grid_with_field(self):
       grid = gpd.read_file('siatka_22.geojson')
       grid.to_crs('EPSG:3857')
       field = gpd.read_file('probny.geojson')
       field.to_crs('EPSG:3857')
       self.merged_geojson = gpd.overlay(grid, field, how='intersection')

#self.merged_geojson = gpd.GeoDataFrame(pd.concat([grid, field], ignore_index=True))
    def save_results(self):
        self.merged_geojson.to_file("merge_3_geojson.geojson", driver='GeoJSON')
    
   
    def do(self):
        self.load_geojson()
        self.get_value()
        self.make_grid()
        self.merge_grid_with_field()
        self.save_results()
    
geojson_1 = GridMaker(35 ,"probny.geojson")
geojson_1.do()

   
