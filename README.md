# Date-parser
Objective

To identify the different formats in which dates are represented in a paragraph and then parse them into a usable format. Here, the format chosen is YYYY-MM-DD. 


Concepts and Language Used

Date Parsing, Named Entity Recognition, Python(packages like datefinder, pandas)


Description

Date Formats: The common date formats are classified into six categories
Formal
eg: “1978-01-28”, “01/02/1980”, “2/28/79”
Relaxed
eg:  “The 31st of April in the year 2002”, “Jan 21,’97”, “Sun, Nov 21”
Relative
eg: “Next Thursday”, “Last Wednesday”, “Tomorrow”
Prefixes
eg: “Day after”, “Day before”, “two Monday’s before”
Date Alternatives
eg: “Next Wed or Thur”, “Oct 3rd or 4th”
Single Component Date
eg: “January”, “1987”, “March”

I have identified dates in various formats in a given paragraph using the datefinder package. It will output all the dates in the text in the format “YYYY-MM-DD”.

     2.  datefinder: A python module for locating dates inside text. This package can be used to extract all sorts of date-like strings from a document and turn them into datetime objects.This module finds the likely datetime strings and then uses dateutil to convert to the datetime object. The function I used from the datefinder package is find_dates().
        
Syntax: datefinder.find_dates(text,source=false,index=false,strict=false,base_date=NONE)
Parameters: 
text(str|unicode)- A string that contains one or more natural language or literal datetime strings.
source(boolean)- Return the original string segment 
index(boolean)- Return the indices where the datetime string was located text.
strict(boolean)-Only return datetime with complete date information. For example: July 2016 of Monday will not return datetimes. May 16,2015 will return datetimes.
base_date(datetime)-Set a default when parsing incomplete dates.

Returns: Returns a generator that produces datetime.datetime object ,or a tuple with the source text and index ,if requested

     3.  Named Entity Recognition(NER): NER, also called entity identification or entity extraction is a natural language processing (NLP) technique that automatically identifies named entities in a text and classifies them into predefined categories​. Entities can be names of people, organizations, locations, times, quantities, monetary values, percentages, and more​. I have used the concept of NER in our project to point out the various entities in a date like Year, Day, Month number, Month. This is done so as to increase the understandability. 

I have implemented NER using the Python package pandas. 


    4.  pandas: pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. It allows us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets, and make them readable and relevant. In our project pandas is used for pointing out the major entities from the Formal Date format into which all dates in a paragraph are parsed into.
The functions used for this are 
DataFrame(): DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. We used this function to get the output in the form of a table with columns:
start (date in the YYYY-MM-DD)
date
year
day
month(Month number)
em(Name of the month) 
 
   II. 	DatetimeIndex().date: Pandas DatetimeIndex.date attribute outputs an Index object containing the date values present in each of the entries of the DatetimeIndex object.

   III.     DatetimeIndex().year: Pandas DatetimeIndex.year attribute outputs an Index object containing the value of years present in the Datetime object.
  
   IV.     DatetimeIndex().day: Pandas DatetimeIndex.day attribute outputs an Index object containing the days in each of the entries of the DatetimeIndex object.

   V.      DatetimeIndex().month: Pandas DatetimeIndex.month attribute outputs an Index object containing numeric values corresponding to each entry in the DatetimeIndex object. It outputs the month as January=1, December=12 and corresponding numeric values for each month in between.
