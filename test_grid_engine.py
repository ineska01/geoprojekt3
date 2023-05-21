from grid_engine import get_grid
from geopandas import GeoDataFrame
import geopandas as gpd

def test_can_make_grid_type():
    
    upper_left = (3456, 5678)
    lower_right = (4567, 8765) 

    grid = get_grid(upper_left, lower_right,12)
    print(type(grid))
    assert isinstance(grid, GeoDataFrame)
    
def test_can_make_grid_value():
    
    upper_left = (3456, 5678)
    lower_right = (4567, 8765) 

    grid = get_grid(upper_left, lower_right,12)
    print(grid.area.sum())
    assert grid.area.sum() == 3451680.0
    
if __name__ == '__main__':
    test_can_make_grid_type()
    test_can_make_grid_value()