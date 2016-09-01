![image](http://sophai.github.io/arch_2013/files_2013/Coding/tsca/figure_1.png)

TSCA
====

Two-stage Clustering Algorithm
------------------------------

Copyright(c) 2016-, Po-Jen Hsu (clusterga@gmail.com)                           

Published under GNU General Public License Version 3, 29 June 2007

Author: Po-Jen Hsu

Requirements:

Linux, Python(>=3.5), and numpy.

How to run:
-----------

* Put tsca.py and tsca_pref.json in your working directory that contains xyz files.

* Change the permission of tsca.py by typing `chmod u+rx tsca.py`.

* Run `./tsca.py tsca_pref.json` to perform TSCA for your xyz files.

* The results will be stored in the xyz folder by default.

Options in pref.json file:
--------------------------

* "mode": "skip" will skip the job.

* "processes": 1 will use only one core.

* "output": "./some_path/" will specify the output directory.

* "usr_threshold": float_value will assign the USR similarity threshold. 

* "pot_key": "eng=" will use "eng=" to parse the energy keyword in the info line of xyz files. Please refer to example1.xyz.

* "use_cluster_id": false will disable the first stage clustering method that groups the ring/chain H-bond topologies.


Note:
-----

* Please delete the example*.xyz files before performing TSCA for your xyz coordinates. TSCA will search for all the .xyz files in the current folder and the sub-folders.

* You can also change the options from "filter_name:" ".xyz" to "filter_name": ".xyz -example" to exclude the example files.
