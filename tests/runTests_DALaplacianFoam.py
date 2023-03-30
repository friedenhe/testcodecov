#!/usr/bin/env python
"""
Run Python tests for DASolidDisplacementFoam
"""

from mpi4py import MPI
from dafoam import PYDAFOAM, optFuncs
import sys
import os
from pygeo import *
from pyspline import *
from idwarp import *
import numpy as np
from testFuncs import *

gcomm = MPI.COMM_WORLD

os.chdir("./input/flange")

TRef = 1.0

# test incompressible solvers
aeroOptions = {
    "designSurfaces": ["patch1"],
    "solverName": "DALaplacianFoam",
    "useAD": {"mode": "fd"},
    "objFunc": {
        "HF": {
            "part1": {
                "type": "wallHeatFlux",
                "source": "patchToFace",
                "patches": ["patch4"],
                "scale": 1.0,
                "addToAdjoint": True,
            }
        },
    },
    "debug": False,
    "primalMinResTol": 1e-16,
}
DASolver = PYDAFOAM(options=aeroOptions, comm=MPI.COMM_WORLD)
DASolver()
