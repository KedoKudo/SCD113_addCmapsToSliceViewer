# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

import os

Load(Filename='data/SXD23767.raw',
     OutputWorkspace='SXD23767',
     LoaderName='LoadRaw',
     LoaderVersion='3')
ConvertToDiffractionMDWorkspace(InputWorkspace='SXD23767',
                                OutputWorkspace='SXD23767MD',
                                OneEventPerBin='0')
FindSXPeaks(InputWorkspace='SXD23767',
            PeakFindingStrategy='AllPeaks',
            AbsoluteBackground=2000,
            ResolutionStrategy='AbsoluteResolution',
            XResolution=200,
            PhiResolution=3,
            TwoThetaResolution=3,
            OutputWorkspace='peaks')
