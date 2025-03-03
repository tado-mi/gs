# Read me

## Q1 & Q2 

* how to run:

```
# prereqs:
pip install xarray netCDF4
pip install mathplotlib

# filepath defaults to waves_2019-01-01.nc
python gs_sol.py <filepath.nc>

```

* output:
```            
q1:
the highest wave height at coordinates (0.0, 0.0) is 2.3259894847869873.

q2:
loading ui...
```

* chat gpt contribution on [Q1](https://chatgpt.com/share/67c2a4d9-63dc-8013-b760-e2606dd5df47) and on [Q2](https://chatgpt.com/share/67c53fef-c618-8013-be90-e4e42d092959)


## Q3

On a high level, we need to sort large amount of data and get its max. The code provided for Q1 would work for any .nc file that has the same coordinates and variable names, but it might be sub-optimal. The main point of concern is processing a large amount of data, and my hunch is that there are likely tools already available.

I'd go about this question by 1. understanding the usecase and 2. researching the tools already available.

By "understanding the usecase", I mean I'd want to know more details about what the users need. For example, will the users frequently need to know the max of any arbitrary range? Or are they usually interested in the max on a single day and the max so far?

If the second is the case, "max on a single day" can be computed daily and maintained as a location and day level variable and "max so far" can be maintained as a location-level variable. I thought of introducing a data structure for sorting and a relational database for maintaining computed values, but I am going to guess that's likely to be duplicate effort - so first I'd want to learn more about .nc files, what kind of information they store, and what tools are already available in python.

If the first is the case - the problem becomes a lot harder. We may need to do lots of real time calculations - to grab the data of the required range and to compute the local max. Here, I'd still be interested to learn more about the existing tools and .nc files. 

1. For example, I am thinking of Cloud Watch graphing tools that allow you to zoom in and can find local max / min - perhaps something like that can be levaraged or partially re-implemented.

1. I am thinking that .nc files might already come with some sorting - if the sorting is by time, or by coordinates - that can be leveraged as well.
