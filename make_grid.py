import geopandas as gpd
from shapely.geometry import box
import fiona
from grid_engine import get_grid

class GridMaker:
    def __init__(self, dense, input_files):
        self.dense = dense
        self.input_files = input_files
        self.loaded_geojson = None
        self.get_crs = None
        self.upper_left = None
        self.lower_right = None
        self.merged_geojson = None
        self.grid = None
        
    def load_geojson(self):
        self.loaded_geojson = gpd.read_file(self.input_files)
        self.loaded_geojson = self.loaded_geojson.to_crs('EPSG:3857')
    def get_value(self):
        xmin, ymin, xmax, ymax = self.loaded_geojson.total_bounds
        self.upper_left = ymin, xmax
        self.lower_right = ymax, xmin
        
    def make_grid(self):
        self.grid = get_grid(self.upper_left, self.lower_right, self.dense)
        self.grid.to_file('siatka_23.geojson', driver='GeoJSON')
    
    def merge_grid_with_field(self):
       self.grid.crs = 'EPSG:3857'
       self.merged_geojson = gpd.overlay(
           self.grid, self.loaded_geojson, how='intersection'
       )

    def save_results(self):
        self.merged_geojson.to_file("merge_geojson.geojson", driver='GeoJSON')
    
   
    def do(self):
        self.load_geojson()
        self.get_value()
        self.make_grid()
        self.merge_grid_with_field()
        self.save_results()
    
geojson_1 = GridMaker(200 ,"probny.geojson")
geojson_1.do()

   
