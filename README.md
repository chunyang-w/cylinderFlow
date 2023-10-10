# 🌀 2D Cylinder Flow

This repo contains the code for numeric simulation for the flow around a cylinder in a 2D context. The project was powered by the 'OpenFOAM' framework.

## Problem setup

+ The programme aims to simulate the flow around a cylinder in a 2D context, using DNS (Direct Numerical Simulation) method.
+ The computational domain is a 2D square with consomisable size (can be set in the `blockMeshDict` file, i.e. `length` variable).
+ The cylinder is located at the center of the domain, its diameter can be set in the `blockMeshDict` file, i.e. `small_r` variable.
+ Boundary conditions:
  + No-slip condition is set for the wall, including the cylinder surface and the upper and lower boundaries.
  + The inlet is has a constant velocity, and the outlet is set to have zero pressure condition.
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


## Visualization

### Computational Mesh

The computational domain is devided into 4 subdomains. With finer mesh near the cylinder and the wall to provide more accurate results.

<div align="center">
<img src="https://raw.githubusercontent.com/chunyang-w/cylinderFlow/main/assets/mesh.png" alt="mesh" width="20%;" />
</div>

### DNS simulation

The following animation shows the velocity field of the DNS simulation. The intial velocity is 1.0 m/s. The diameter of the cylinder is 0.1 m.

<div align="center">
<img src="https://raw.githubusercontent.com/chunyang-w/cylinderFlow/main/assets/DNS.gif" alt="mesh" width="50%;" />
</div>

### P.S.

Additional pre-run files can be found in the `results` folder.
