Title: Designing a simple time-series database
Slug: time-series-database
Date: 2017-02-02
Category: Blog
Author: Julian Wergieluk
Tags: quant-finance, market-data
Summary: simple market data system design

This is a kind of a functional requirements spec and developer documentation.

* Explain the NoSQL names: collection, document

## References

* http://jmoiron.net/blog/thoughts-on-timeseries-databases/
* https://www.xaprb.com/blog/2014/06/08/time-series-database-requirements/



This document describes a simple database schema for storing financial market
data. 


## IO format

When I talk about an (financial) instrument I have the following data structure in mind. 
Most of the objects observed on financial markets have some set of labels, which are
traditionally called "ticker". 



  {
    "_id" : <...>,
    "tickers": [
      [ "source_1", "ticker_1" ],
      [ "source_2", "ticker_2" ]
    ],
    "properties": {
      "property_name_1": <value1>,
      "property_name_2": <value2>,
      "category": "category_name"
    },
    "series": {
      "series_name": [
        [ "time_stamp_1", <observation_1> ],
        [ "time_stamp_2", <observation_2> ]
      ]
    }
  }


## Representation in the database

To store arbitrary number of the instruments defined above as well as history of the
changes we need the following collections: 

* 'refs' defines the link between tickers and other parts of an instrument.
* 'paths' holds the history of objects such as properties (i.e. objects that
  usually do not change over time) (1-dimensional)
* 'sheets' holds the history for the time-series. (2-dimensional)
* 'spaces' holds the history of the scenario set, i.e. object that have both
  time and space dimension. (3-dimensional)

The "refs" collection contains the pointers to the stored objects allows to label
the instruments with "tickers". A reference document has the following form:

    {
        "_id" : <...>,
        "source": "...",
        "ticker": "...",
        "valid_from": <utc_time>,
        "valid_until": <utc_time>,
        "props": <path_key_1>,
        "series": <path_key_2>,
        "scenarios": <path_key_3>    
    }

"r" is the revision time. "t" is the observation or "market" time. Both are fields holding UTC date and time.

#### Paths collection

    {
        "_id" : <...>,
        "k" : <key>,
        "r" : <utc_time>,
        "v" : <value object>
    }

#### Series collection

    {
        "_id" : <...>,
        "k" : <key>,
        "r" : <utc_time>,
        "t" : <utc_time>,
        "v" : <value object>
    }

#### Scenarios collection

    {
        "_id" : <...>,
        "k" : <key>,
        "r" : <utc_time>,
        "t" : <utc_time>,
        "s" : <scenario_id>,
        "v" : <value object>
    }



## Command-line interface

The library provides a simple command-line interface. 





