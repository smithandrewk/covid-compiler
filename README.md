1. Don't think the pangolin install works on mac
2. On Linux
3. Download and install miniconda
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda*
```
4. Create old conda env
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

6. Download sequencing log
7. Download Fasta Files Folders
8. Pangolin each folder separately
9. Run main.ipynb
10. Pray