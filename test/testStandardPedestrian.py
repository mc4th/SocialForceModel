'''
Created on 13 Oct 2015

@author: RolandGuichard
'''
import unittest

import numpy as np

from entities.pedestrians.standardPedestrian import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStandardPedestrianWithPedestrian(self):
        numberOfEntities = 20
        position = np.array([5., 5., 5.])
        target = np.array([10., 10., 10.])
        velocity = np.array([1., 1., 1.])
        pedtype = 'standardPedestrian'
        id       = 10
        initialConditions = 'defined'
        returnedPedestrian = standardPedestrian(numberOfEntities, pedtype, id, initialConditions, position, target, velocity)
        errorMessage = "Wrong input value for pedestrian"
        self.assertEqual(returnedPedestrian.type, pedtype, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedPedestrian.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedPedestrian.initialConditions, initialConditions, errorMessage)
#         errorMessage = "Wrong input value for position"
#         self.assertEqual(returnedPedestrian.position.all(), position.all(), errorMessage)
#         errorMessage = "Wrong input value for velocity"
#         self.assertEqual(returnedPedestrian.velocity.all(), velocity.all(), errorMessage)
#         errorMessage = "Wrong input value for target"
#         self.assertEqual(returnedPedestrian.target.all(), target.all(), errorMessage)
        errorMessage = "Wrong input value for desired velocity"
        self.assertEqual(returnedPedestrian.desiredVelocity, v0, errorMessage)
        errorMessage = "Wrong input value for relaxtion time"
        self.assertEqual(returnedPedestrian.relaxationTime, tauAlpha, errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStandardPedestrian']
    unittest.main()