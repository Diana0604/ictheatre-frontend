# wrapper to add sys paths without making main ugly
import sys
sys.path.append('./src/constants')
sys.path.append('./src/components/displays')
sys.path.append('./src/components/stock')
sys.path.append('./src/api')
sys.path.append('./src/helpers')
import main


main.init()