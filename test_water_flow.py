import unittest
from water_flow1 import (
    density_of_water,
    dynamic_viscosity_of_water,
    reynolds_number,
    pressure_loss_from_fittings,
    pressure_loss_from_pipe_reduction,
)


class TestWaterFlow(unittest.TestCase):

    def test_density_of_water(self):
