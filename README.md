# README - Coding Exercise

## Purpose

Show how you would solve a relevant real world-problem.

## Problem

This is a real-world problem. The content needing to be manipulated is a set of cyber security controls from the NIST Special Publication 800-171. The original content was copied and pasted from a 125-page PDF into the spreadsheet in this repository. The controls in the spreadsheet need to be transformed into a specific JSON format conforming to a new control catalog format.

The desired out put data format is called OSCAL (Open Security Control Assessment Language) and is a new standard for expressing a collection of cyber security compliance controls. Unfortunately, the NIST 800-171 catalog of controls is not yet available in OSCAL. We need to create the OSCAL version of the 800-171 control catalog.

Your problem is to generate JSON version...or as close as you can get to the format in the allotted time.

You are being asked to only produce the control selection of the OSCAL format.

OSCAL can be expressed in JSON, XML or YAML.

More about OSCAL:

* Example content - https://github.com/usnistgov/OSCAL/tree/master/content/nist.gov/SP800-53
* Home page - https://pages.nist.gov/OSCAL/


## Instructions

Clone this repo into your own GitHub account. Do your work in your account. We will look at your results in your cloned GitHub repository

Write Python (script or class) to transform the data in the spreadsheet into the desired JSON format.

Read the rows in the spreadsheet and transform the data into OSCAL JSON format, or a format that is similar enough OSCAL JSON format to be easily copied and pasted into the OSCAL format.

The file `data/NIST_SP-800-53_rev4_catalog.json` shows what the full OSCAL JSON format looks like. This our (eventual) end-goal.

The file `data/handmade_800-171_rev1_catalog.json` is a version of the desired end product made by copying and pasting a sample set of controls by hand.

It's tedious to make the file by hand. Python would do it better.

There is no right solution to this problem, just solutions that are more resolved and more elegant than others. Performance of your code is not a major issue. You aren't working alone either. If your code makes a good start, your co-workers could always help re-factor and improve the code.

We do *not* need the entire structure of the OSCAL outputted from your script. What you are being asked to do is to produce the control section of the OSCAL format.

Do as much as you can in 45 minutes and stop. You can also stop before 45 minutes.

After you write the code, spend no more than 15 minutes preparing basic instructions on how to use your code. Put this information in a file called README_USAGE.md 

Make sure your code *runs*. Work through the problem iteratively: first reading the spreadsheet, the reading the rows, then outputting JSON to a file, then outputting JSON file that is closer and closer to the desired format.

## Acceptable Solutions

The closer the output is to the OSCAL format, the better the solution.

But don't let perfection be the enemy of the good enough. Getting close to the solution in 15 or 30 minutes is more cost effective than spending 4 hours to get exactly to the solution. It's common to write code that "gets the job done."

## Rules

- It's OK to manipulate the source spreadsheet.
- It's OK to get close to the solution, but not exactly the solution.
- It's OK to hardcode certain values for convenience, provided the hardcoding is friendly to subsequent refactoring for greater flexibility and reuse.

## How Your Solution Will Be Evaluated

There's a range of success in this challenge. Do as much as you can in 45 minutes, plus 15 minutes for documentation.

- Did you use of xlrd library to read the .xlsx file properly? (Alternatively, did you use Python CSV class to read the .csv file properly?)
- Did you transform all the controls in the spreadsheet to a single JSON object?
- Did you save the JSON object to a file?
- How much hardcoding vs configurability is in your code? 
- Did you address any encoding issues that came up? How well will your code deal with smart quotes in the text?
- How reusable is your code? (interpret this as you like)
- How easy is it for someone else to run your code?
- Did you add useful comments in the code? How easy can another developer read and refactor your code?
- Did you organize the controls by "groups" in the output?
- What is the quality and usefulness of your README_USAGE.md instructing someone how to use your code.
- How closely did you adhere to these instructions?
