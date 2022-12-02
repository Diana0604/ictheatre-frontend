# wrapper to add sys paths without making main ugly
import sys

sys.path.append('./src/constants')
sys.path.append('./src')
sys.path.append('./src/components')
sys.path.append('./src/components/labels')
sys.path.append('./src/components/displays')
sys.path.append('./src/components/stock')
sys.path.append('./src/components/sellers')
sys.path.append('./src/tabs')
sys.path.append('./src/api')
sys.path.append('./src/helpers')

import main

window = main.init()
main.run(window)
#main.end(window)