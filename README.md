# 🌀 2D Cylinder Flow

This repo contains the code for numeric simulation for the flow around a cylinder in a 2D context. The project was powered by the 'OpenFOAM' framework.

## Run this project

### Prerequisites

+ OpenFOAM 11
+ Paraview 5.1.0

### Commands

```bash
blockMesh
decomposePar
mpirun -np 4 pimpleFoam -parallel
reconstructPar
foamToVTK
```

or Simply run the `./Allrun` script.

Please run `./Allclean` before each run to clean the previous results.


### Visualize the results

#### DNS simulation
![](https://raw.githubusercontent.com/chunyang-w/cylinderFlow/main/assets/DNS.gif)


#### RANS simulation
![](https://raw.githubusercontent.com/chunyang-w/cylinderFlow/main/assets/RANS.gif)