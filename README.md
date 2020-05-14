im6A-TS-cnn
====
Description:
------------
im6A-TS-cnn is able to identify multi-tissues in Human, Mouse and Rat.

Installation:
-------------
- <span  style="color: #5bdaed; font-weight: bold">python3.6</span>
- pandas==1.0.3
- tensorflow-cpu==2.1.0
- numpy==1.18.3
``` 
pip install pandas==1.0.3 tensorflow-cpu==2.1.0 numpy==1.18.3
``` 
``` 
pip install -r yours/requirement.txt
``` 
Optional arguments:
-------------------
```
  -h, --help            show this help message and exit
  --addresses ADDRESSES
                        Liukeweiaway@hotmail.com
  -i INPUTFILE, --inputFile INPUTFILE
                        -i input.txt (The input file is a complete Fasta
                        format sequence.)
  -o OUTPUTFILE, --outputFile OUTPUTFILE
                        -o output.html (Results are saved under results
                        folder.)
  -s SPECIES, --species SPECIES
                        -m Human/Mouse/Rat (Choose one from three species to
                        use.)
  -m TISSUES, --tissues TISSUES
                        brain/liver/kidney/heart/testis (We can choose testis you want)
  -ts THRESHOLDS, --thresholds THRESHOLDS
                        low/normal/high (We offer 3 options based on the difference in specificity, which are low, normal and high.)
```
Example:
--------
```
python im6A-TS-cnn.py -i sequence.txt -o ccc.html -s Human -t brain  -ts normal
```
***
Version number：V0.1.2 <br>
Updated date：2020-05-03 <br>
Email: Liukeweiaway@hotmai.com 
***
