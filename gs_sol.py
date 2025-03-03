import matplotlib.pyplot as plt
import numpy as np
import sys
import xarray as xr

def print_info(ds):

    print("\nprovided data:")

    # dimensions
    print(ds.dims)

    # coordinates
    print(ds.coords)

    # data variables
    print(ds.data_vars)

    # detailed info
    print("\ninfo on dimensions:")
    for dim_name, dim_size in ds.dims.items():
        print(f"{dim_name}: {dim_size}")

    print("\info on coordinates:")
    for coord_name, coord_values in ds.coords.items():
        print(f"{coord_name}: {coord_values.values}")

    print("\ndata variables:")
    for var_name, var_values in ds.data_vars.items():
        print(f"{var_name}: {var_values.attrs}")

    print("\n----------")

# q1
def get_max_hmax_in_location(ds, lon, lat):
    # get all the available time values
    time_vals = ds.coords["time"].values
    # extract all supplied hmax values for the given coordinates
    hmax_vals = [ds["hmax"].sel(longitude=lon, latitude=lat, time=t).values for t in time_vals]
    return max(hmax_vals)

def get_max_hmax_string(ds, lon, lat):
    return f"the highest wave height at coordinates ({lon}, {lat}) is {get_max_hmax_in_location(ds, lon, lat)}."

#q2
def get_points(ds):
    lon_vals = ds.coords["longitude"].values
    lat_vals = ds.coords["latitude"].values
    full_grid = [[float(lon), float(lat)] for lon in lon_vals for lat in lat_vals]
    return np.array(full_grid)

def create_ui(ds):
    points = get_points(ds)
    x, y = points[:, 0], points[:, 1]
    fig, ax = plt.subplots()
    # enable picker
    sc = ax.scatter(x, y, c='blue', picker=True)
    # text 
    txt = ax.text(0.5, 1.05, "click on a point", transform=ax.transAxes, ha="center")

    def on_click(event):
        # get the index of the selected point
        ind = event.ind
        if len(ind) > 0:
            lon, lat = points[ind[0]]
            # update the text
            txt.set_text(get_max_hmax_string(ds, lon, lat))  # Update text
            # redraw
            fig.canvas.draw()

    # connect onclick
    fig.canvas.mpl_connect('pick_event', on_click)
    plt.show()


# filepath
filepath = "waves_2019-01-01.nc" if len(sys.argv) < 2 else sys.argv[1]
ds = xr.open_dataset(filepath)

# uncomment to see info about the input
# print_info(ds)

# q1
print("\nq1:")
lon = 0.000
lat = 0.000
print(get_max_hmax_string(ds, lon, lat))

# q2
print("\nq2:")
print("loading ui...")
create_ui(ds)

# close ds
ds.close()
