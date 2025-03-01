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

def get_max_hmax_in_location(ds, lon, lat):
    # get all the available time values
    time_vals = ds.coords["time"].values
    # extract all supplied hmax values for the given coordinates
    hmax_vals = [ds["hmax"].sel(longitude=lon, latitude=lat, time=t).values for t in time_vals]
    return max(hmax_vals)

# filepath
filenpath = "waves_2019-01-01.nc" if len(sys.argv) < 2 else sys.argv[1]
ds = xr.open_dataset(filepath)

# uncomment to see info about the input
# print_info(ds)

# q1
print("\nq1:")
lon = 0.000
lat = 0.000
print(f"the highest wave height at coordinates ({lon}, {lat}) is {get_max_hmax_in_location(ds, lon, lat)}.")

# close ds
ds.close()
