# Dependencies
import numpy as np
import pandas as pd
from geopy.distance import geodesic
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


#Input information from user
#print("Search room for rent")
#lat1 = float(input("Input Latitude: "))
#lon1 = float(input("Input Longitude: "))
#query = input("Input Query: ")
#dist1 = float(input("Input distance in miles: "))

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#Code to return filtered rent table information
#Function to find distance in between two (lat, lon) locations 
def dist2(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).miles
    
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        query = request.form["Query"]
        lat1 = float(request.form["Lat"])
        lon1 = float(request.form["Lon"])
        dist1 = float(request.form["Dist"])
        
        #Read CSV data into panda dataframe
        rent_pd = pd.read_csv("AB_NYC_2019.csv")

        # Convert Latitude and Longitude to float
        rent_pd['latitude'] = pd.to_numeric(rent_pd['latitude'],errors='coerce')
        rent_pd['longitude'] = pd.to_numeric(rent_pd['longitude'],errors='coerce')
        #Drop NA data for latitude, longitude and name
        rent_pd = rent_pd.dropna(subset=['latitude', 'longitude', 'name'])
        rent_pd = rent_pd.fillna({'last_review':"No Reviews", 'reviews_per_month':0}, inplace=True)
        #Create new column
        rent_pd.insert(8, "Distance", np.nan)
        #Reset Index
        rent_pd = rent_pd.reset_index(drop=True)

        # Fill Distance column with calculated distance in miles
        rent_pd['Distance'] = np.vectorize(dist2)(lat1, lon1, rent_pd['latitude'], rent_pd['longitude'])

        #Filter rent panda dataframe based on distance and query
        if dist1:
            rent_pd = rent_pd.loc[rent_pd["Distance"] <= dist1]
        if query:
            rent_pd = rent_pd[rent_pd["name"].str.contains(query)]
        #Sort Filtered Data based on 
        filter_rent_pd = rent_pd.sort_values(by="Distance")
        filter_rent_pd.set_index(['name'], inplace=True)
        print (filter_rent_pd.head())
        return render_template('table.html', tables=[filter_rent_pd.to_html(classes='data', header="true")])

    return render_template("form.html")

if __name__ == "__main__":
    app.run()