# validation-component-bootstrap-utils
Code for bootstrapping software modules for validating tab-delimited and comma-separated files

# Implementation Objectives

## Completed

1. Implement support for parsing the tab-delimited file

2. Implement support for writing unique values in each column to a column-specific file<br>
2.1. number of unique values<br>
2.2. number of total values<br>

3. Implement support for writing a percentage breakdown<br>
3.1. percent of unique values breakdown<br>

4. Implement support to generate the [file_type]/validator.py<br>
4.1. Should use jinja2 templating<br>

5. Implement support to generate the [file_type]/record.py<br>
5.1. Should use jinja2 templating<br>

6. Implement support to generate the Enum classes.<br>

7. Implement support to add the equality checks for the values in the classmethods.<br>

## In-Progress

## To-Do

8. Implement support to determine the datatype of each column e.g.: int, float, str, bool<br>
8.1. For integers and floats, determine the range of allowable values<br>
8.2. For strings, determine the longest common prefix and the longest common suffix<br>
