grepfqparser

Rapidly parse fastq format files by inline barcode into separate files in a specified folder.

USAGE

python grepfqparser.py <input_fastq> <barcode_file> <output_folder> <gzipped?>

<gzipped?> ("yes", "no") is optional (default = "yes")


I wrote this utility because I couldn't find a parser that could easily handle barcodes of different lengths.
This parser will handle barcodes of any length, but it is most useful for long, variable length barcodes. 
This parser allows no mismatches, on the assumption that problems in the barcode are often indicative of problems with the whole read.
Note that this parser looks for the barcode starting from the first base of the sequence read.

The parser runs on gzipped or unzipped files (user specified in command line), but it is MUCH faster on unzipped files.

This parser calls the UNIX command grep (or zgrep) for parsing, hence the name.

Try the test data supplied with the code as follows

python grepfqparser.py headfastq.gz bc outFolder "Yes"

David L. Stern Janelia Farm Research Campus 1 June 2013

Copyright 2013 Howard Hughes Medical Institute.
All rights reserved.
Use is subject to Janelia Farm Research Campus Software Copyright 1.1
license terms ( http://license.janelia.org/license/jfrc_copyright_1_1.html ).