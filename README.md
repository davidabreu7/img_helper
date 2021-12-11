# img_helper
Resize, rotate and rename multiple image files.

### technologies used:
* python
* argparser
* os.path
* pillow

### Structure
The project is structured in
* a main file __imghelper_main.py__: responsible for parsing arguments and function calls
* a functions file __lib/imghelper_lib.py__ : contains all the functions responsible for file manipulation

### usage:
./imghelper_main.py -r <angle: 90 180 or 270> -s __height__ __width__ [--dir | --file] __read_path__ __save_path__
  
