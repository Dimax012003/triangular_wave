# triangular_wave
A project that uses analogread to read the voltage of a 555 timer.
You will need a 555timer,3 resistors ,3 capasitors,jumper wires and you will follow the connections given in the schematic.
In the output of the 555 timer is connected a low pass filter tha integrates the output and gives instead of a pulse a triangular wave.
You will need to connect the output of the low pass filter to an analog pin of your microcontroller.In my case i use an arduino mega board an that reads the output voltage every 1ms and sents it through Serial port to a python program.
The python program creates a plot and it gives a graph that has a triangular shape with noise
