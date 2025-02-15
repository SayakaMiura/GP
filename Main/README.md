**Setup the software**

_Download the whole folder of GP that contains Main and Input folders_

Make sure you know where you can find GP.py in the Main folder in your PC. This GP.py file location in your PC is [path to GP.py], e.g., C:\Users\LabCompu\Desktop\GP-main\GP-main\Main.

_Install Miniconda_

https://docs.anaconda.com/miniconda/

_Open Anaconda Prompt and type:_

conda create -n GP -c conda-forge python=3.11.11 r-base=4.3.3

conda activate GP

cd [path to GP.py]

conda env update -f environment.yml

conda install anaconda::graphviz

conda install conda-forge::r-picante

**Test the installation**

Test datasets can be found in the Input folder.

python GP.py --driver_mutation_file [path to gp5_driver.txt]\gp5_driver.txt snv [path to GP5_CF_input.tsv]\GP5_CF_input.tsv [path to control.txt]\control.txt

**Input files**

_1.	Driver mutation._ E.g., gp5_driver.txt. Please list gene name (Diver Gene) and chromosomal position (Mutation Summary) for each driver mutation.
   
Driver Gene	ref>alt	Mutation Summary

HNF1A	G>T	chr12:120993588

BRCA2	->A	chr13:32338208

BRCA2	->A	chr13:32338209

_2.	Read counts._ E.g., GP5_CF_input.tsv. Please list chromosome (CHR), genomic position (Position), reference base (Wild), alternate base (Mutant), trinucleotide of the genomic position (Trinucletide), and reference and alternate read count of each sample (e.g., S1:ref and S1:alt for S1 sample) for each SNV. The minimum number of samples is four. 

CHR	Position	Wild	Mutant	Trinucletide	S1:ref	S1:alt	S2:ref	S2:alt	S3:ref	S3:alt	S4:ref 	S4:alt	

chr1	950995	C	T	ACG	101	2	69	0	78	0	99	0	

chr1	1128714	C	T	ACG	64	29	50	23	59	20	78	38	

_3.	Expected mutational signatures._ E.g., control.txt. Please change only the line of “Signature List.”

…

Signature List	SBS1,SBS2,SBS13,SBS18

…

**How to use**

python GP.py --driver_mutation_file [path to “Driver mutation” file]\gp5_driver.txt snv [path to “Read counts” file]\GP5_CF_input.tsv [path to “Expected mutational signatures”]\control.txt

**Output files**

All output files can be found in the same directory as the input files.

_1.	Main output files._
   
a.	[input file ID]_CloneTree.png. A figure showing clone phylogeny and clone frequencies.

b.	[input file ID]snv_CloneFinder.meg , [input file ID]snv_CloneFinder.nwk , and [input file ID]snv_CloneFinder.txt. Inferred clone genotype, phylogeny, and frequency. “meg” and “nwk” files can be open using MEGA (https://www.megasoftware.net/). In “meg” file, “A” and “T” represents a wild and mutant base, respectively.

c.	[input file ID]_Mutation.png. A figure showing mutational signature, mutational pattern, and driver mutations at each branch of the inferred clone phylogeny.

d.	[input file ID]_Metastasis.png. A figure showing history of tumor cell migration events between samples.

e.	[input file ID]_SampleTree_unifrac.nwk and [input file ID] _SampleTree_comdistntW.nwk. Inferred sample trees using unifrac and comdistnt (weighted by clone frequency).

_2.	Other output files._ The other files that are not essential are found in [input file ID]_output directory. 

