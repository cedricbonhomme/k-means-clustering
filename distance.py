#! /usr/bin/python
#-*- coding:utf-8 -*

# ***** BEGIN LICENSE BLOCK *****
# This file is part of Adaptive Conference Companion.
# Copyright (c) 2015 Luxembourg Institute of Science and Technology.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2015/08/31$"
__revision__ = "$Date: 2015/08/31 $"
__copyright__ = "Copyright (c) Luxembourg Institute of Science and Technology"
__license__ = ""

from math import sqrt

def pearson(v1, v2):
    sum1 = sum(v1)
    sum2 = sum(v2)

    sum1Sq = sum([pow(v, 2) for v in v1])
    sum2Sq = sum([pow(v, 2) for v in v2])

    pSum = sum([v1[i]*v2[i] for i in range(len(v1))])

    # Calculate r (Pearson score)
    num = pSum - (sum1*sum2/len(v1))
    den = sqrt((sum1Sq-pow(sum1, 2)/len(v1)) * (sum2Sq-pow(sum2, 2)/len(v1)))

    if den == 0:
        return 0
    return 1.0-num/den

def tanamoto(v1,v2):
  c1,c2,shr=0,0,0

  for i in range(len(v1)):
    if v1[i]!=0: c1+=1 # in v1
    if v2[i]!=0: c2+=1 # in v2
    if v1[i]!=0 and v2[i]!=0: shr+=1 # in both

  return 1.0-(float(shr)/(c1+c2-shr))
