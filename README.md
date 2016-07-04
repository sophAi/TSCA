TSCA

Two-stage Clustering Algorithm

Copyright(c) 2016-, Po-Jen Hsu (clusterga@gmail.com)                           

Published under GNU General Public License Version 3, 29 June 2007

Author: Po-Jen Hsu

Requirements:

Linux, Python(>=3.5), and numpy.

How to run:

1. Put tsca.py and tsca_pref.json in your working directory that contains xyz files.

2. Change the permission of tsca.py by typing "chmod u+rx tsca.py".

3. Run "./tsca.py tsca_pref.json" to perform TSCA for your xyz files.

4. The results will be stored in the xyz folder by default.

Options in pref.json file:

1. "mode": "skip" will skip the job.

2. "processes": 1 will use only one core to perform each job.

3. "output": "./some_path/" will specify the output directory.

4. "usr_threshold": float_value will treat the xyz coordinates that > float_value as duplicated ones.

5. "pot_key": "eng=" enable parsing function to search for the energy keyword in the xyz info lines. Please refer to the example1.xyz.

6. "use_cluster_id": false will disable the first stage clustering method that analyzes ring/chain topology for methanol cluster.


Note:
    Please delete the example*.xyz files before performing TSCA for your xyz coordinates bacause TSCA will search for all the .xyz files in the current folder and the sub-folders.

    You can also change the options from "filter_name:" ".xyz" to "filter_name": ".xyz -example" to exclude those files.
