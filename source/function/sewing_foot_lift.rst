.. _sewing_foot_lift:

================
Sewing foot lift
================

Features
========

Foot is raised
--------------

* **On the seam** : By pedal back(:term:`POSITION -1`) or automatically with A14 setted to 1;
* **After thread has been cut** : By pedal back(:term:`POSITION -1` or :term:`POSITION -2`) or 
  automatically with :option:`A15` setted to 1.

Holding force of the raised foot
--------------------------------

The foot lifting is raised by full activation, then it switches automatically
to partial activation to reduce the load on the controller and the connected 
magnets.

The full activation period is set with :option:`T07` and holding force during partial 
activation is set with :option:`O05`.

Timeout release
---------------

In order to reduce heat generation, timed release can be set. 

if parameter :option:`O06` is set to 1, the maximum time the foot lifter can keep 
raised is determined by parameter :option:`O07`.

Delay time
----------

When the sewing foot is the raised, in order to ensure that the sewing material is 
pressed tightly before the machine starts running, a tiem lag will be inserted after
step the pedal forwards, which is controlled by parameter :option:`T06`.

Quick reference
===============

This table summarizes which parameter should be used for sewing foot:

============================================================= ========== ==============
Parameter                                                     Authority  See also
============================================================= ========== ==============
Sewing foot lift                                              Operator   :option:`A09`
Debouncing of Lifting Foot                                    Technician :option:`T05`
Foot Drop Time                                                Technician :option:`T06`
Delay Time Before Auto Foot                                   Technician :option:`T10`
Sewing Foot Lift at Sewing Stop                               Technician :option:`A14`
Sewing Foot Lift after Trim/at Seam End                       Technician :option:`A15`
Auto Power-off Foot                                           Technician :option:`O06`
Foot Max. Lifting Time                                        Technician :option:`O07`
Soft Foot Falling                                             Technician :option:`O39`
Time(t1)                                                      Developer  :option:`T07`
Duty cycle(t2)                                                Developer  :option:`O05`
Effect of Soft Foot Falling                                   Technician :option:`O40`
Effect of PrePressure duiring Clamping(Without Start Bartack) Technician :option:`O53`
Effect of PrePressure duiring Clamping(Soft Start)            Technician :option:`O54`
Effect of PrePressure duiring Clamping                        Technician :option:`O55`
============================================================= ========== ==============

Parameter List
==============

.. option:: A09
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Sewing Foot lift:
     | 0 = Off;
     | 1 = On.

.. option:: T05
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  To avoid unexpected foot lifting when step backwards for trim, the tim
                 is less and the sensitivity is higher.

.. option:: T06

   -Max  500
   -Min  1
   -Unit  ms
   -Description  Lag time,make sure the foot has pressed the material, after which, sewing
                 can start.

.. option:: T10
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Lag time,after which,sewing foot is automatically activated 
                 if the function is On.

.. option:: A14
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Automatic lifting sewing foot when stop in the middle of seam:
     | 0 = Off;
     | 1 = On.

.. option:: A15
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Automatic lifting sewing foot after trim or at seam end:
     | 0 = Off;
     | 1 = On.

.. option:: O06
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the magnet of foot automatic power-off after the set time:
     | 0 = Off;
     | 1 = On.

.. option:: O07
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  If Auto Power-off Foot is turned on, this parameter sets the power-off time.

.. option:: O39
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Decrease the falling speed of the foot by PWM control:
     | 0 = Off;
     | 1 = On.

.. option:: T07
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Foot lifter:activation duration of in :term:`time period t1`
                 (100% duty cycle).

.. option:: O05

   -Max  100
   -Min  1
   -Unit  %
   -Description  Foot: duty cycle[%] in :term:`time period t2`
   


.. option:: O40
   
   -Max  9
   -Min  1
   -Unit  --
   -Description  The larger value, the slower foot falls.

.. option:: O53
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping without start bartack

.. option:: O54
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping with soft start


.. option:: O55
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping
