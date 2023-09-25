.. _sewing_foot_lift:

================
Sewing foot lift
================

**Foot is raised**

- on the seam
  
  by pedal back(:term:`POSITION -1`) or automatically with A14 setted to 1

- after thread has been cut: 
  
  by pedal back(:term:`POSITION -1` or :term:`POSITION -2`) or automatically 
  with `A 15`_ setted to 1

**Holding force of the raised foot**

the foot lifting is raised by full activation, then it switches automatically
to partial activation to reduce the load on the controller and the connected 
magnets.

The full activation period is set with `T 07`_ and holding force during partial 
activation is set with `O 05`_.

**Timeout release**

In order to reduce heat generation, timed release can be set. 

if parameter `O 06`_ is set to 1, the maximum time the foot lifter can keep 
raised is determined by parameter `O 07`_.

**Delay time**

When the sewing foot is the raised, in order to ensure that the sewing material is 
pressed tightly before the machine starts running, a tiem lag will be inserted after
step the pedal forward, which is controlled by parameter `T 06`_.

Parameter List
==============

T 05
----

.. dropdown:: Debouncing of Lifting Foot <...>
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  To avoid unexpected foot lifting when step backward for trim, the tim
                 is less and the sensitivity is higher.

T 06
----

.. dropdown:: Foot Drop Time <...>
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  Lag time,make sure the foot has pressed the material, after which, sewing
                 can start.

T 07
----

.. dropdown:: Time(t1) <...>
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Foot lifter:activation duration of in :term:`time period t1`
                 (100% duty cycle).

T 10
----

.. dropdown:: Delay Time Before Auto Foot <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Lag time,after which,sewing foot is automatically activated 
                 if the function is On

A 09
----

.. dropdown:: Sewing foot lift <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Sewing Foot lift:
     | 0 = Off;
     | 1 = On.

A 14
----

.. dropdown:: Sewing Foot Lift at Sewing Stop <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Automatic lifting sewing foot when stop in the middle of seam:
     | 0 = Off;
     | 1 = On.

A 15
----

.. dropdown:: Sewing Foot Lift after Trim/at Seam End <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Automatic lifting sewing foot after trim or at seam end:
     | 0 = Off;
     | 1 = On.

O 05
----

.. dropdown:: Duty cycle(t2) <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Foot: duty cycle[%] in :term:`time period t2`
   
O 06
----

.. dropdown:: Auto Power-off Foot <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the magnet of foot automatic power-off after the set time:
     | 0 = Off;
     | 1 = On.

O 07
----

.. dropdown:: Foot Max. Lifting Time <...>
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  If Auto Power-off Foot is turned on, this parameter sets the power-off time.

O 39
----

.. dropdown:: Soft Foot Falling <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Decrease the falling speed of the foot by PWM control:
     | 0 = Off;
     | 1 = On.

O 40
----

.. dropdown:: Effect of Soft Foot Falling <...>
   :animate: fade-in-slide-down
   
   -Max  9
   -Min  1
   -Unit  --
   -Description  The larger value, the slower foot falls.

O 53
----

.. dropdown:: Effect of PrePressure duiring Clamping(Without Start Bartack) <...>
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping without start bartack

O 54
----

.. dropdown:: Effect of PrePressure duiring Clamping(Soft Start) <...>
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping with soft start


O 55
----

.. dropdown:: Effect of PrePressure duiring Clamping <...>
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  Duty cycle of foot during clamping
