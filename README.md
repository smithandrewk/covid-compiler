1. On a Linux machine, open a new terminal
2. Clone repository
```
git clone https://github.com/smithandrewk/covid-compiler.git
```
3. Enter directory
```
cd covid-compiler
```
3. Download and install miniconda
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda*
```
4. Create old conda env (Panoglin maintainters haven't updated)
```
conda create --name pangolin_env python=3.8
```
5. Activate
```
conda activate pangolin_env
```
6. Install pangolin
```
conda install -c bioconda -c conda-forge -c defaults pangolin
```
6. Download sequencing log and place in covid-compiler directoy
7. Download Fasta Files Folders and place in covid compiler directory
Example Directory Structure:
```
(pangolin_env) andrew@tau:~/covid-compiler$ tree
.
├── 2024_COVID-19_sequencing_log.xlsx
├── FastaFiles_01.06.2025
│   └── 01.06.2025.fasta
├── FastaFiles_09.16.2024
│   └── 09.16.2024.fasta
├── main.py
└── README.md

2 directories, 5 files
```
8. Pangolin each folder separately
```
cd FastaFiles_01.06.2025
pangolin 01.06.2025.fasta
cd ../
cd FastaFiles_09.16.2024
pangolin 09.16.2024.fasta
cd ../
```
Directory Structure:
```
(pangolin_env) andrew@tau:~/covid-compiler$ tree
.
├── 2024_COVID-19_sequencing_log.xlsx
├── FastaFiles_01.06.2025
│   ├── 01.06.2025.fasta
│   └── lineage_report.csv
├── FastaFiles_09.16.2024
│   ├── 09.16.2024.fasta
│   └── lineage_report.csv
├── main.py
└── README.md

2 directories, 7 files
```
9. Install dependency
```
pip3 install openpyxl
```
10. Run main.py
```
python3 main.py
```
10. Pray