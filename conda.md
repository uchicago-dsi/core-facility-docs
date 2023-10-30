
## Libmamba Solver
The conda solver can sometimes take a really long time. This is frustrating for students (especially on deep learning projects) since they are often trying to manage environments with a lot of packages. 

There is a new version of the conda solver that has a much more reasonable protocol for looking for package conflicts than the default solver. This seems to resolve most issues where "solving environment" takes forever and sometimes never completes.

To switch to the new solver:
```
conda update -n base conda
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```