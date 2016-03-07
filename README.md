Geokr
=====

School project for a real-time localization of recents Flickr images.

Objectives
----------

Goal's project is to worldwide draw a map with dot on it. Dot size is scaled on number Flickr images.

### Settings

Following options will be available for visitors.

#### Tags

Can filter results with a specific tag.

#### Time frame

Users are able to choose a start and an end date.

#### Crop map

Restrict map to display results only for a specific area.

#### Statistic values

Visitor will be able to display :

 * The number of images.
 * The number of active users.
 * The number of images per user.
 
Requirements
------------

### Configuration file

You must have the *.config* file in the same directory. This file is a json file containing :

```json
{
    // Ask your api key on https://www.flickr.com/services/api/misc.api_keys.html
    "API_KEY": <flickr_api_key>
}
```

### Python and basic packages

> Python is a programming language that lets you work quickly and integrate systems more effectively

Install [Python](https://www.python.org/) thanks to this link <https://www.python.org/downloads/>

#### Required python packages

 * json
 * requests
 * numpy
 * scipy.cluster.vq
 * matplotlib.pyplot
 * IPython.display
 * sklearn.cluster
 * sklearn

### Notebook Python

> The IPython Notebook is an interactive computational environment, in which you can combine code execution, rich text, mathematics, plots and rich media

Install [Notebook](http://ipython.org/notebook.html) with this link <http://jupyter.readthedocs.org/en/latest/install.html>

### Folium

> Make beautiful maps with Leaflet.js & Python

Install [Folium](https://pypi.python.org/pypi/folium) with following bash command.

```bash
pip install folium
```

Usefull links
-------------

 * [Flickr API](https://www.flickr.com/services/api/)
 * [Pandas visualization API](http://pandas.pydata.org/pandas-docs/stable/visualization.html)
 * [Google Chart API](https://google-developers.appspot.com/chart/interactive/docs/gallery)
 * [Google Map Python](https://github.com/googlemaps/google-maps-services-python)
 * [D3](https://d3js.org)
 * [KMeans JS](https://www.npmjs.com/package/kmeans-js)
 * [Google geocoding](https://developers.google.com/maps/documentation/geocoding/intro#ReverseGeocoding)
* [Folium GitHub] (https://github.com/python-visualization/folium)
 
Contributors
------------

 * Maxime PICHOU
 * Marwin DAMIS
 * Pierre PÉRONNET

