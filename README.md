![image](http://sophai.github.io/arch_2013/files_2013/Coding/tsca/figure_1.png)

TSCA
====

Two-stage Clustering Algorithm
------------------------------

Copyright(c) 2016-, Po-Jen Hsu (clusterga@gmail.com)                           

Published under GNU General Public License Version 3, 29 June 2007

Author: Po-Jen Hsu

Requirements:

* Linux, Python(>=3.5), and numpy.


How to run:
-----------

1. Put tsca.py and tsca_pref.json in your working directory that contains xyz files.

2. Change the permission of tsca.py by typing `chmod u+rx tsca.py`.

3. Run `python3 tsca.py tsca_pref.json` to perform TSCA.

4. The resulting xyz files will be stored in the xyz folder by default.


Options in tsca_pref.json file:
--------------------------

1. `"mode": "skip"` will skip the job.

2. `"processes": 1` will disable multiprocessing.

3. `"output": "./some_path/"` will specify the output directory.

4. `"usr_threshold": float_value` will assign the USR similarity threshold. 

5. `"pot_key": "eng="` will use `"eng="` to parse the energy keyword in the info line of xyz files. Please refer to example1.xyz.

6. `"use_cluster_id": false` will disable the first stage clustering method that groups the ring/chain H-bond topologies.


Note:
-----

1. Please delete the example*.xyz files before performing TSCA with your own xyz files. TSCA was designed to search for all the .xyz files in the current folder and the sub-folders.

2. You can also change the options from `"filter_name:" ".xyz"` to `"filter_name": ".xyz -example"` in the json file to exclude the example files.
