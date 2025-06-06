from krita import Krita

# Initialize the Krita instance
app = Krita.instance()

# Retrieve the list of available filter names
filter_names = app.filters()  # This returns a list of filter names

# Loop through each filter, retrieve its configuration, and print available properties
for filter_name in filter_names:
    filt = app.filter(filter_name)  # Get the filter instance using its name
    config = filt.configuration()   # Retrieve the configuration for this filter
    properties = config.properties()  # Get a list (or dict) of available properties
    
    print("=" * 60)
    print("Filter:", filter_name)
    print("Available Properties:")
    
    # If properties() returns an iterable list or dict keys, loop through them:
    if isinstance(properties, dict):
        for key, value in properties.items():
            print("  {} : {}".format(key, value))
    else:
        for prop in properties:
            print("  ", prop)
    
    print("=" * 60, "\n")
