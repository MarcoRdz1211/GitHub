#!/usr/bin/env python3

# Copyright 2016, 2019 Thomas J. Duck.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Plots field lines for a line and point charge."""

from matplotlib import pyplot
import electrostatics
from electrostatics import PointCharge, LineCharge
from electrostatics import ElectricField, Potential, GaussianCircle
from electrostatics import finalize_plot

# pylint: disable=invalid-name

XMIN, XMAX = -80, 80
YMIN, YMAX = -60, 60
ZOOM = 15
XOFFSET = 0

electrostatics.init(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)

# Set up the charges, electric field, and potential
charges = [LineCharge(1, [-1, -2], [-1, 2]), PointCharge(-1, [1, 0])]
field = ElectricField(charges)
potential = Potential(charges)

# Set up the Gaussian surfaces
g = GaussianCircle(charges[1].x, 0.1)

# Create the field lines
fieldlines = []
for x in g.fluxpoints(field, 12):
    fieldlines.append(field.line(x))
fieldlines.append(field.line([-10, 0]))

# Plotting
pyplot.figure(figsize=(6, 4.5))
field.plot()
potential.plot()
for fieldline in fieldlines:
    fieldline.plot()
for charge in charges:
    charge.plot()
finalize_plot()
pyplot.show()
