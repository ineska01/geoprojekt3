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
        
    def load_geojson(self):
        self.loaded_geojson = gpd.read_file(self.input_files)
        self.loaded_geojson = self.loaded_geojson.to_crs('EPSG:3857')
    def get_value(self):
        xmin, ymin, xmax, ymax = self.loaded_geojson.total_bounds
        self.upper_left = ymin, xmax
        self.lower_right = ymax, xmin
        
    def make_grid(self):
        grid = get_grid(self.upper_left, self.lower_right, self.dense)
        grid.to_file('siatka_18.geojson', driver='GeoJSON')
    def merge_grid_with_field(self):
        pass
    
    def save_results(self):
        pass
   
    def do(self):
        self.load_geojson()
        self.get_value()
        self.make_grid()
        self.merge_grid_with_field()
        self.save_results()
    

geojson_1 = GridMaker(35 ,"probny.geojson")
geojson_1.do()
   
