# room_for_rent

Build an interactive dashboard to find room for rent 

## Step 1 - Reading of CSV data into Panda Dataframe for cleaning, filtering and sorting
* Convert Latitude and Longitude to float
* Drop NA data for latitude, longitude and name
* Create new Distance column in the pandas dataframe this will be used to store the distance calculated between two (lat, lon) points
* Used geopy to calculate the shortest distance between two (lat,lon) points
* Sort the dataframe based on distance value 
* This dataframe is used by Flask API to render tabular template


## Step 2 - Flask API

Used Flask to design an API for dataset and to serve the HTML required for your dashboard page. Note: We read the CSV data directly into Pandas DataFrames in this project. 

* First, create a template called `index.html` for your dashboard landing page. Used Bootstrap grid system to create the structure of the dashboard page.

* Next, create the following routes for your api.

* Next, create the following routes for your api.

```python
@app.route("/")
    """Return the dashboard homepage."""
```
```python
@app.route('/send') GET method
    """Form containing Location details.

    Returns a form with Location details information such as 
     1. Latitude
     2. Longitude
     3. Distance in miles
     4. Query  eg: two bedroom, near empire state building 


    """
```
```python
@app.route('/send') POST method
    """Table containing rooms information.

    Returns a table based on 
    1. Sorted Distance from the desired latitude and longitude
    2. Name filtered based on query information provided
    3. Also has other information such as price per night, ratings etc
   
    """
```
