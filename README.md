# pythonBoids2D
Implementation of Craig Reynold's Boids program in object-oriented python. A flock of birds follow three basic rules of behavior:
- <b>Avoidance</b>: Birds will keep a minimum distance to other birds
- <b>Alignment</b>: Birds will attempt to match the velocity of nearby birds
- <b>Cohesion</b>: Birds will move closer to nearby birds as long as it does not conflict with Avoidance

### Dependencies

The program has been tested with `python 2.7.3` and needs `python-mathplotlib` installed for visualization. For generating movies (optional) a recent version of `ffmpeg` is required.  

### Quick how-to

The default parameters are tuned to give flocking behavior. Run the program from the root folder by  
```bash
    mkdir png
    python ./run
```
The program should output a real-time visual representation of the positions of the birds and the predator looking like 
the picture below.
<div style="text-align:center">
<img src ="/doc/example.png" width="600" />
</div>
The black arrows represent normal birds and the red arrow represents the predator. 

### Adjustable parameters

The following parameters can be adjusted in the `Bird` class in order to change flocking characteristics. Note that extreme values might break the simulation alltogether.
- <b>nd</b>: Neighborhood radius
- <b>dd</b>: Desired minimum distance to other birds
- <b>pd</b>: Desired minimum distance to predators
- <b>sepmult</b>: Scaling factor for the separation rule
- <b>almult</b>: Scaling factor for the alignment rule
- <b>cohmult</b>: Scaling factor for the cohesion rule
- <b>premult</b>: Scaling factor for predator avoidance
- <b>alpha</b>: Number between -1 and 1 determining cone of vision

### Making movies

The program will generate a PNG image in the subfolder PNG for every time the flock updates. A bash script is provided for generating an AVI movie file from the sequence of pictures. To run this:
```bash
    chmod +x genmovie
    ./genmovie
```
