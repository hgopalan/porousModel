scalar treeCounter=1;
// Here we use a simple box search to put the tree into domain 
// complexPorousTreeModel will include more advanced methods
forAll(treeInfo,i)
{
  scalar treeCounter=0;
  scalar cellBlank=i;
  scalar x=treeCenterX[i];
  scalar y=treeCenterY[i];
  scalar zLower=treeCenterZ[i];
  scalar zUpper=treeCenterZ[i]+treeHeight[i];
  scalar diameter=treeGirth[i];
  scalar z=zLower;
  while(z<=zUpper)
    {
      scalar xstart=x-0.5*diameter;
      while(xstart<=(x+0.5*diameter))
	{
	  scalar ystart=y-0.5*diameter;
	  while(ystart<=(y+0.5*diameter))
	    {		  
	      point treeLoc(xstart,ystart,z);
	      label cellLabel=mesh.findCell(treeLoc);
	      if(cellLabel>0)
		{
		  treeblanking[cellLabel]=cellBlank;
		  treeCounter=treeCounter+1;
		}
	      ystart=ystart+1; // Assumed the mesh size near tree is >= 1m  
	    }
	  xstart=xstart+1; // Assumed the mesh size near tree is >= 1m  
	}
      z=z+1; // Assumed the mesh size near tree is >= 1m  
    }
  if(treeCounter>0)
    Pout<<i<<"  "<<treeCounter<<endl;
}
treeblanking.correctBoundaryConditions();
treeblanking.write();
Info<<"Trees Done"<<endl;
