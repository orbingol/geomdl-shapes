"""
.. module:: analytic
    :platform: Unix, Windows
    :synopsis: Provides common analytic geometries

.. moduleauthor:: Onur Rauf Bingol <orbingol@gmail.com>

"""

import math
from geomdl import abstract
from geomdl import linalg


class Freeform(abstract.Geometry):
    """ n-dimensional freeform geometry """
    def __init__(self, **kwargs):
        super(Freeform, self).__init__(**kwargs)
        self.name = "Freeform geometry"

    def evaluate(self, **kwargs):
        """ Sets points that form the freeform geometry.

        Keyword Arguments:
            * ``points``: sets the points
        """
        self._eval_points = kwargs.get('points', self._init_array())


class Circle(abstract.Geometry):
    r""" Analytic circle geometry

    Finds the points on a circle using the following equation:

    .. math::

        x &= x_{0} + r \cos{\theta} \\
        y &= y_{0} + r \sin{\theta}

    Keyword Arguments:
        * ``radius``: radius of the circle. *Default: 1*
        * ``origin``: coordinates of the circle center. *Default: (0, 0)*
    """
    def __init__(self, **kwargs):
        super(Circle, self).__init__(**kwargs)
        self.name = "Analytic circle"
        self._radius = kwargs.get('radius', 1.0)
        self._origin = kwargs.get('origin', (0.0, 0.0))

    def evaluate(self, **kwargs):
        """ Evaluates the circle.
        
        Keyword Arguments:
            * ``start``: start angle :math:`\\theta` in degrees. *Default: 0*
            * ``stop``: stop angle :math:`\\theta` in degrees. *Default: 360*
            * ``jump``: angle :math:`\\theta` increment in degrees. *Default: 1*
        """
        start = kwargs.get('start', 0.0)
        stop = kwargs.get('stop', 360.0)
        jump = kwargs.get('jump', 1.0)
        points = []
        for t in linalg.frange(start, stop, jump):
            t_r = math.radians(t)
            pt = [
                self._origin[0] + (self._radius * math.cos(t_r)), 
                self._origin[1] + (self._radius * math.sin(t_r))
            ]
            points.append(pt)
        self._eval_points = points


class Sphere(abstract.Geometry):
    r""" Analytic sphere geometry

    Finds the points on a sphere using the following equation:

    .. math::

        x &= x_{0} + r \sin{\phi} \cos{\theta} \\
        y &= y_{0} + r \sin{\phi} \sin{\theta} \\
        z &= z_{0} + r \cos{\phi}
    
    Keyword Arguments:
        * ``radius``: radius of the sphere. *Default: 1*
        * ``origin``: coordinates of the sphere center. *Default: (0, 0, 0)*
    """
    def __init__(self, **kwargs):
        super(Sphere, self).__init__(**kwargs)
        self.name = "Analytic sphere"
        self._radius = kwargs.get('radius', 1.0)
        self._origin = kwargs.get('origin', (0.0, 0.0, 0.0))

    def evaluate(self, **kwargs):
        """ Evaluates the sphere.
        
        Keyword Arguments:
            * ``start_theta``: start angle :math:`\\theta` in degrees. *Default: 0*
            * ``stop_theta``: stop angle :math:`\\theta` in degrees. *Default: 360*
            * ``jump_theta``: angle :math:`\\theta` increment in degrees. *Default: 1*
            * ``start_phi``: start angle :math:`\\phi` in degrees. *Default: 0*
            * ``stop_phi``: stop angle :math:`\\phi` in degrees. *Default: 180*
            * ``jump_phi``: angle :math:`\\phi` increment in degrees. *Default: 1* 
        """
        start_theta = kwargs.get('start_theta', 0.0)
        stop_theta = kwargs.get('stop_theta', 360.0)
        jump_theta = kwargs.get('jump_theta', 1.0)
        start_phi = kwargs.get('start_phi', 0.0)
        stop_phi = kwargs.get('stop_phi', 180.0)
        jump_phi = kwargs.get('jump_phi', 1.0)
        points = []
        for tt in linalg.frange(start_theta, stop_theta, jump_theta):
            tt_rad = math.radians(tt)
            for tp in linalg.frange(start_phi, stop_phi, jump_phi):
                tp_rad = math.radians(tp)
                pt = [
                    self._origin[0] + (self._radius * math.sin(tp_rad) * math.cos(tt_rad)), 
                    self._origin[1] + (self._radius * math.sin(tp_rad) * math.sin(tt_rad)),
                    self._origin[2] + (self._radius * math.cos(tp_rad))
                ]
                points.append(pt)
        self._eval_points = points
