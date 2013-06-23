grepfqparser

Rapidly parse fastq format files by inline barcode into separate files in a specified folder.


USAGE

python grepfqparser.py <input_fastq> <barcode_file> <output_folder> 

This is a fast inine parser that will parse fastq files with barcodes of variable lengths. 
This parser allows no mismatches, on the assumption that problems in the barcode are often 
indicative of problems with the whole read. The parser looks for the barcode starting from 
the first base of the sequence read. Unparsed reads are saved in a separate file called nomatches.

The parser runs on gzipped or unzipped files.

This parser calls the UNIX command grep for parsing, hence the name.


Try the test data supplied with the code as follows:

python grepfqparser.py headfastq.gz bc outFolder



David L. Stern Janelia Farm Research Campus 1 June 2013

Copyright 2013 Howard Hughes Medical Institute.
All rights reserved.
Use is subject to Janelia Farm Research Campus Software Copyright 1.1
license terms ( http://license.janelia.org/license/jfrc_copyright_1_1.html ).
