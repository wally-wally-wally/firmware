# Generated with SMOP  0.41
from smop.libsmop import *
# workspaceBoundsCheck.m

    #not to be confused with the workspace of a 3R arm in general which is just
#a filled in 2D circle with radius L1 + L2 + L3
#workspace of arm poses can be considered to be a 2R semicircle workspace 
#and then offset by the 3R arm
BOUNDS_TOL_UPPER = 0.9999
BOUNDS_TOL_LOWER = 1.0001    
    
@function
def workspaceBoundsCheck(p_sc=None,p_s1=None,*args,**kwargs):
    varargin = workspaceBoundsCheck.varargin
    nargin = workspaceBoundsCheck.nargin

    #define lengths of arm links in m
    L1=0.258
# workspaceBoundsCheck.m:8
    L2=0.191
# workspaceBoundsCheck.m:9
    L3=0.153521
# workspaceBoundsCheck.m:10
    
    R1=L1 - L2
# workspaceBoundsCheck.m:13
    R2=L1 + L2
# workspaceBoundsCheck.m:14
    
    p_1c=[p_sc[0] - p_s1[0],p_sc[1] - p_s1[1],p_sc[2] - p_s1[2]]
# workspaceBoundsCheck.m:17
    
    p_13=[p_sc[0] - p_s1[0],p_sc[1] - p_s1[1],p_sc[2] - p_s1[2]]
# workspaceBoundsCheck.m:20
    p_13[0]=p_1c[0] - L3
# workspaceBoundsCheck.m:21
    r=sqrt(p_13[0] ** 2 + p_13[1] ** 2)
# workspaceBoundsCheck.m:23
    if (r > (R2 + eps) * BOUNDS_TOL_LOWER) or (r < (R1 - eps) * BOUNDS_TOL_UPPER):
        success=1
# workspaceBoundsCheck.m:26
    else:
        success=0
# workspaceBoundsCheck.m:28
    
    
    return success
    
if __name__ == '__main__':
    pass
    
