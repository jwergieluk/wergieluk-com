Title: Designing a simple time-series database
Slug: time-series-database
Date: 2017-02-02
Category: Blog
Author: Julian Wergieluk
Tags: quant-finance
Summary: simple market data system design



## References


* http://jmoiron.net/blog/thoughts-on-timeseries-databases/
* https://www.xaprb.com/blog/2014/06/08/time-series-database-requirements/


This document describes a simple database schema for storing financial market
data. 


## IO format

  {
    "properties": {
      "property_name_1": "value1",
      "property_name_2": "value2",
      "category": "category_name"
    },
    "tickers": [
      [ "ticker_name_1", "ticker_value_1" ],
      [ "ticker_name_2", "ticker_value_2" ]
    ],
    "series": {
      "series_name": [
        [ "time_stamp_1", "observation_1" ],
        [ "time_stamp_2", "observation_2" ]
      ]
    }
  }


## Representation in the database

To store arbitrary number of the instruments defined above as well as history of
changes we need the following collections: 

* 'refs' defines the link between tickers and other parts of an instrument.
* 'paths' holds the history of objects such as properties (i.e. objects that
  usually do not change over time) (1-dimensional)
* 'sheets' holds the history for the time-series. (2-dimensional)
* 'spaces' holds the history of the scenario set, i.e. object that have both
  time and space dimension. (3-dimensional)


The "refs" collection contains the pointers to the stored objects allows to label
the instruments with "tickers". A referece document



The "tickers" collection

{
    "_id" : ObjectId("[...]"),
    "instr_id" : ObjectId("[...]"),
    "source" : "source_name",
    "ticker" : "ticker_name"
}


{
    "_id" : ObjectId("588bae8c41ebcc626239abf1"),
    "t" : ISODate("2010-12-09T17:30:00.000Z"),
    "k" : ObjectId("588bae8c41ebcc626239abe7"),
    "v" : 163.0
}


## Command-line interface

The library provides a simple command-line interface. 





