.. _sewing_foot_lift:

================
Sewing foot lift
================

Features
========

Foot is raised
--------------

* on the seam
  
  by pedal back(:term:`POSITION -1`) or automatically with A14 setted to 1

* after thread has been cut: 
  
  by pedal back(:term:`POSITION -1` or :term:`POSITION -2`) or automatically 
  with :option:`A 15` setted to 1

Holding force of the raised foot
--------------------------------

The foot lifting is raised by full activation, then it switches automatically
to partial activation to reduce the load on the controller and the connected 
magnets.

The full activation period is set with :option:`T 07` and holding force during partial 
activation is set with :option:`O 05`.

Timeout release
---------------

In order to reduce heat generation, timed release can be set. 

if parameter :option:`O 06` is set to 1, the maximum time the foot lifter can keep 
raised is determined by parameter :option:`O 07`.

Delay time
----------

When the sewing foot is the raised, in order to ensure that the sewing material is 
pressed tightly before the machine starts running, a tiem lag will be inserted after
step the pedal forwards, which is controlled by parameter :option:`T 06`.

Quick reference
===============

This table summarizes which parameter should be used for sewing foot:

============================================================= ========== ==============
Parameter                                                     Authority  See also
============================================================= ========== ==============
Sewing foot lift                                              Operator   :option:`A 09`
Debouncing of Lifting Foot                                    Technician :option:`T 05`
Foot Drop Time                                                Technician :option:`T 06`
Delay Time Before Auto Foot                                   Technician :option:`T 10`
Sewing Foot Lift at Sewing Stop                               Technician :option:`A 14`
Sewing Foot Lift after Trim/at Seam End                       Technician :option:`A 15`
Auto Power-off Foot                                           Technician :option:`O 06`
Foot Max. Lifting Time                                        Technician :option:`O 07`
Soft Foot Falling                                             Technician :option:`O 39`
Time(t1)                                                      Developer  :option:`T 07`
Duty cycle(t2)                                                Developer  :option:`O 05`
Effect of Soft Foot Falling                                   Technician :option:`O 40`
Effect of PrePressure duiring Clamping(Without Start Bartack) Technician :option:`O 53`
Effect of PrePressure duiring Clamping(Soft Start)            Technician :option:`O 54`
Effect of PrePressure duiring Clamping                        Technician :option:`O 55`
============================================================= ========== ==============

Parameter List
==============

.. option:: T 05
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  To avoid unexpected foot lifting when step backwards for trim, the tim
                 is less and the sensitivity is higher.

.. option:: T 06

   -Max  500
   -Min  1
   -Unit  ms
   -Description  Lag time,make sure the foot has pressed the material, after which, sewing
                 can start.

.. option:: T 07

.. dropdown::  <...>
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Foot lifter:activation duration of in :term:`time period t1`
                 (100% duty cycle).

.. option:: T 10
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Lag time,after which,sewing foot is automatically activated 
                 if the function is On

.. option:: A 09
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Sewing Foot lift:
     | 0 = Off;
     | 1 = On.

.. option:: A 14
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Automatic lifting sewing foot when stop in the middle of seam:
     | 0 = Off;
     | 1 = On.

.. option:: A 15
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Automatic lifting sewing foot after trim or at seam end:
     | 0 = Off;
     | 1 = On.

.. option:: O 05

   -Max  100
   -Min  1
   -Unit  %
   -Description  Foot: duty cycle[%] in :term:`time period t2`
   
.. option:: O 06
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the magnet of foot automatic power-off after the set time:
     | 0 = Off;
     | 1 = On.

.. option:: O 07
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  If Auto Power-off Foot is turned on, this parameter sets the power-off time.

.. option:: O 39
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Decrease the falling speed of the foot by PWM control:
     | 0 = Off;
     | 1 = On.

.. option:: O 40
   
   -Max  9
   -Min  1
   -Unit  --
   -Description  The larger value, the slower foot falls.

.. option:: O 53
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping without start bartack

.. option:: O 54
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping with soft start


.. option:: O 55
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping
