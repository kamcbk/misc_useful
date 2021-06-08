### Initializing themes/color in jupyter notebook ###
# Author: Kevin Marroquin

# Instructions: Install jupyterthemes, put this file in .ipython/profile_default/startup/, name this file themes.ipy,
#     run commands on command line to activate

# import jtplot module in notebook
from jupyterthemes import jtplot

# currently installed theme will be used to set plot style if no argiments
# provided
jtplot.style()

# visit https://github.com/dunovank/jupyter-themes for more information on commands to use
# On command line: jt -t oceans16 -fs 12 -cellw 100% -T -N -kl
# Other template from online: jt -t monokai -f roboto -fs 115 -altp -ofs 115 -dfs 11 -tfs 135 -nfs 135 -cellw 99% -N -T -kl
