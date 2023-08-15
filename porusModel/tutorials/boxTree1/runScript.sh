blockMesh
decomposePar -copyZero -force
cd constant
python3 createTrees.py
cd ..
mpirun -np 48 snappyHexMesh -parallel -overwrite
mpirun -np 48 boxPorousTreeModel -parallel 
mpirun -np 48 foamToVTK -parallel  
