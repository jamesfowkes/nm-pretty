# nm-pretty
A small Python utility to pretty up the output from nm

## Usage with Arduino IDE:

* Make symlinks to nm-pretty.py and avr-nm-wrapper in your Arduino AVR bin folder (/your/arduino/install/folder/hardware/tools/avr/bin)
* Copy-and-paste the following lines into /your/arduino/install/folder/hardware/arduino/avr/platform.txt:
  * recipe.hooks.objcopy.postobjcopy.1.pattern="{compiler.path}avr-nm-wrapper" "{build.path}/{build.project_name}.elf" "{build.path}/{build.project_name}.prof"
  * recipe.hooks.objcopy.postobjcopy.2.pattern="{compiler.path}nm-printer.py" "{build.path}/{build.project_name}.prof" "{build.path}/{build.project_name}.html"

Start the Arduino IDE, turn on verbose compilation and try to build the blank sketch.

You should see two extra lines at the bottom of the output corresponding to the two lines above.
