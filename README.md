# BME547 - TSH Test Data Convertion

Please run tsh.py for the function, and check folder "bme547tsh" for Sphinx document.

## Features of the modules

* Read the file containing TSH test data
* Diagnose hyperthyroidism and hypothyroidism according to given standard
* Convert the data into separate files for each patient, and show progress after each finished
* Able to sort TSH data in ascending numeric order


### Please note:

No user interface. The module takes "test\_data.txt" as input, so please name the data file strictly as this.

If a patient has middle names, only the first name and the last name will be kept.

In TSH data result line, no space allowed after each comma.

Assuming there is no result contains both figures greater than 4 and figures smaller than 1.

The demension of patient information must align. All of them should have four aspects of information in the order of Name - Age - Gender - TSH result.

There is only one test function to test the diagnosing function. Other functions have complicated output, making it very hard to test.

## One Problem:

"No build" under my travis project for this repository. However, I didn't know that my travis is not working until I read the feedback for the last assignment yesterday, and I don't think I can figure it out before deadline. I apologize for that and I will keep working on it.

My guess is that it's because this repo was private and just made public today. In an attempt to fix this, I made more commits, but didn't work.
