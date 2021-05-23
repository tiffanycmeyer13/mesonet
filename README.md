# mesonet
Python plots, to plot Oklahoma Mesonet data

1. Clone repo: 

git clone git@github.com:tiffanycmeyer13/mesonet.git

2. Download data: http://www.mesonet.org/index.php/weather/daily_data_retrieval

Stations:	NRMN
Parms:	TMAX TMIN DMAX DMIN HMAX HMIN PDIR WSMX WSMN RAIN

Download file, unzip it

vi file, find and replace "
%s/"//g
set ff=unix


333. Enable conda environment

cd mesonet
~/anaconda/bin/conda env create -f mesonet.yml

~/anaconda3/bin/conda init bash

~/anacondarbin/conda activate mesonet


Use this for picking colors
https://matplotlib.org/stable/gallery/color/named_colors.html
