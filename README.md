# proekti_2

Project: Macedonia Weather and Astronomical Data Visualization (2024)
Description

This project visualizes daily weather trends and astronomical phenomena for Macedonia in 2024. Using Python's matplotlib library, the script processes weather data from a CSV file and plots key metrics such as temperatures, sunrise, and sunset times. It also integrates full moon dates and highlights them with annotations to create an insightful and visually engaging representation.
Features

    Data Sources:
        Weather Data:
            Extracts daily high and low temperatures from a CSV file.
            Processes sunrise and sunset times, converting them into fractional hours for plotting.
        Astronomical Data:
            Predefined full moon dates and their traditional names are incorporated for context.

    Data Visualization:
        Temperature Plot:
            Plots daily high temperatures in red and low temperatures in blue.
            Fills the area between high and low temperatures with a light blue shade to emphasize the range.
            Highlights full moon dates with purple markers for both high and low temperatures.
        Sunrise and Sunset Plot:
            Plots sunrise times in orange and sunset times in purple.
            Annotates full moon dates with their respective names and dates for clarity.

    User-Friendly Outputs:
        Clear, descriptive titles and axis labels.
        Annotated moon phase events for added insight.
        Formatted date labels on the x-axis for readability.

    Error Handling:
        Handles missing or invalid data gracefully by printing debugging messages to the console.

How It Works

    Data Extraction:
        CSV File:
            Reads a CSV file (Macedonia_2024_Formatted.csv) containing:
                Dates (YYYY-MM-DD format).
                High and low temperatures in Celsius.
                Sunrise and sunset times in ISO format.
        Astronomical Data:
            A dictionary maps full moon dates to their names.

    Data Processing:
        Converts date strings into datetime objects for accurate plotting.
        Parses temperature values as floating-point numbers.
        Converts sunrise and sunset times into fractional hours for better visualization.

    Plotting:
        Temperature Plot:
            Plots daily high and low temperatures.
            Highlights full moon dates with markers.
        Sunrise and Sunset Plot:
            Plots daily sunrise and sunset times.
            Annotates full moon dates with their names and positions.

    Annotations:
        Adds full moon names above the corresponding sunset markers.
        Displays full moon dates below the markers for additional context.

    Error Handling:
        Skips rows with invalid data and logs the issue.



    Project: Global Earthquake Visualization (23.10.2024 to 23.11.2024)
Description

This project visualizes global earthquake data over a one-month period (from 23 October 2024 to 23 November 2024) with magnitudes greater than 1. Using Python's plotly library, the script generates an interactive map to display the location, magnitude, and details of each earthquake. The visualization provides a global perspective, highlighting areas with seismic activity during the specified time frame.
Features

    Data Sources:
        Earthquake Data:
            Reads a GeoJSON file (1.0_month.geojson.json) containing earthquake details such as:
                Magnitude.
                Coordinates (longitude and latitude).
                Titles with detailed descriptions.

    Data Visualization:
        Interactive Map:
            Plots earthquake locations on a world map using latitude and longitude.
            Sizes markers based on earthquake magnitude.
            Colors markers according to magnitude, using the Viridis color scale.
            Allows users to hover over points to view additional details (e.g., earthquake titles).

    User-Friendly Outputs:
        Clear and descriptive map title.
        A color legend for earthquake magnitudes.
        Interactive features such as zooming, panning, and tooltips for detailed earthquake information.

    Customizable Visualization:
        Supports dynamic scaling of marker size and color based on magnitude.
        Uses the natural earth map projection for accurate global representation.

How It Works

    Data Extraction:
        Reads a GeoJSON file containing earthquake data for the specified date range.
        Extracts relevant information from the GeoJSON structure:
            Magnitudes from the properties dictionary.
            Coordinates (longitude and latitude) from the geometry dictionary.
            Titles from the properties dictionary.

    Data Processing:
        Iterates through all earthquake entries in the dataset.
        Stores magnitudes, coordinates, and titles in separate lists for plotting.

    Plotting:
        Uses plotly.express.scatter_geo() to create an interactive scatter plot on a world map.
        Configures plot elements:
            Marker size and color based on earthquake magnitude.
            Tooltips to display earthquake titles when hovered over.
            The Viridis color scale to represent magnitude intensity visually.

    Displaying the Map:
        Launches an interactive browser-based visualization using plotly.
        The map is displayed with default zoom and projection settings but can be interacted with for closer inspection.
