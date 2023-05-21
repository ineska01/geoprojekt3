import geopandas as gpd
from shapely.geometry import box


def get_grid(upper_left, lower_right, resolution):
    """
    Funkcja tworząca siatkę o określonym zagęszczeniu w oparciu o podane
    współrzędne lewego górnego i prawego dolnego rogu obszaru.

    Parametry:
    upper_left (tuple): krotka (x, y) zawierająca współrzędne lewego górnego rogu obszaru
    lower_right (tuple): krotka (x, y) zawierająca współrzędne prawego dolnego rogu obszaru
    resolution (float): zagęszczenie siatki (w jednostkach współrzędnych)

    Zwraca:
    GeoDataFrame: obiekt GeoDataFrame z siatką
    """
    ymin, xmax = upper_left
    ymax, xmin = lower_right

    # Oblicz liczbę kolumn i wierszy siatki na podstawie podanych parametrów
    # to do (powiekszyc zeby grid był wiekszy np +10)
    cols = abs(int((xmax - xmin) / resolution) + 2)
    rows = abs(int((ymax - ymin) / resolution) + 2)

    # Utwórz siatkę z obiektów shapely.geometry.box
    grid = gpd.GeoDataFrame(
        geometry=[
            box(
                xmin + i * resolution,
                ymax - j * resolution,
                xmin + (i + 1) * resolution,
                ymax - (j + 1) * resolution,
            )
            for j in range(rows)
            for i in range(cols)
        ]
    )

    return grid
