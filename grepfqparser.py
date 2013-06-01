#!/usr/bin/env python


"""
Parse fastq file containing inline barcodes into separate files

DEPENDENCIES

Python 2.7

USAGE

python grepfqparser.py <input_fastq> <barcode_file> <output_folder> <gzipped?>

<gzipped?> ("yes", "no") is optional (default = "yes")

e.g.

python grepfqparser.py test.fq bc.txt parsed_files yes


David L. Stern
Janelia Farm Research Campus
28 May 2013

/*
 * Copyright 2013 Howard Hughes Medical Institute.
 * All rights reserved.
 * Use is subject to Janelia Farm Research Campus Software Copyright 1.1
 * license terms ( http://license.janelia.org/license/jfrc_copyright_1_1.html ).
 */

"""


import os,sys
import getopt
import subprocess

def main():
        #parse command line options
        try:
                opts, arg = getopt.getopt(sys.argv[1:],"h", ["help"])
        except getopt.error, msg:
                print msg
                print "for help use --help"
                sys.exit(2)
        # process options
        for o, a in opts:
                if o in ("-h", "--help"):
                        print __doc__
                        sys.exit(0)
        if len(arg) < 3:
                print "\nUsage: python grepfqparser.py <input_fastq> <barcode_file> <output_folder> <gzipped?> <ignore_case?>\m"                
                sys.exit(0)
        #process arguments

        fqFile = arg[0]
        bcFile = arg[1]
        OutFolder = arg[2]
        if len(arg) > 3:
                gzbool = arg[3]
                gzbool = gzbool.upper()
        else:
                gzbool = "YES"


        if os.path.isdir(OutFolder):
                print "Directory %s exists" %(OutFolder)
        else:
               os.mkdir(OutFolder)
        
        print "fastq file = %s" %(fqFile)
        print "barcode file = %s" %(bcFile)
        print "Folder of parsed sequences = %s" %(OutFolder)
        print "fq file gzipped? = %s" %(gzbool)        

        bc = open(bcFile,'r')
        for line in bc:
                lineItems = line.split()
                barcode = lineItems[0]
                barcode_up = barcode.upper()
                name = lineItems[1]
                print barcode
                
                if gzbool == "YES":
                                procBC = subprocess.Popen(["zgrep", "-B 1", "-A 2", "^" + barcode_up, fqFile], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                        
                else:
                                procBC = subprocess.Popen(["grep", "-B 1", "-A 2", "^" + barcode_up, fqFile], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                                
                procStrip = subprocess.Popen(["grep", "-v", "^--"],stdin=procBC.stdout,stdout=subprocess.PIPE)
                procBC.stdout.close()
                #proc = subprocess.Popen(["samtools", "flagstat", indiv + ".bam"], 0, None, subprocess.PIPE, subprocess.PIPE,None)
                output_file = open(OutFolder + "/indiv" + name + "_" + barcode,'w')                        
                for l in procStrip.stdout.readlines():
                       output_file.write(l)                        
                output_file.close()
        

  
if __name__ == "__main__":
        sys.exit(main())
