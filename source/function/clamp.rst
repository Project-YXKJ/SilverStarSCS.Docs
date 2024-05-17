.. _thread_clamp:

============
Thread clamp
============

Features
========

Thread clamp at seam start
--------------------------

Switch on at position set by :option:`D07`, switch off at position set by :option:`D08`.

Action only during the first stitch, reset after thread trim.

Thread clamp at turning back
----------------------------

Switch on during turning back, the Max. permissible time is set by :option:`T15`
to protect from damage.

Thread clamp at sewing foot lifting
-----------------------------------

Switch on during foot lifting, the Max. permissible time is set by :option:`T15`
to protect from damage.

Quick reference
===============

This table summarizes which parameter should be used for clamp:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Thread clamp                                         Operator   :option:`A10`
Action Time of Clamp                                 Technician :option:`T15`
Auto Mode for Clamp                                  Technician :option:`A29`
Start Clamp Position                                 Technician :option:`D07`
Stop Clamp Position                                  Technician :option:`D08`
PrePressure duiring Clamp                            Technician :option:`O42`
Duty cycle(t2)                                       Developer  :option:`O48`
==================================================== ========== ==============

Parameter List
==============

.. option:: A10
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread clamp:
     | 0 = Off;
     | 1 = On.

.. option:: T15
   
   -Max  1000
   -Min  1
   -Unit  ms
   -Description  Action time of clamp when lifting the foot or lifting the needlebar after trim.

.. option:: A29
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | 0 = actions when start sewing;
     | 1 = actions when start sewing and lifting the needle after trim;
     | 2 = actions when start sewing and lifting the foot;
     | 3 = both 1&2.

.. option:: D07
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of clamp is activated.

.. option:: D08
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of clamp is deactivated.

.. option:: O42
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Reduce the sewing foot pressure during the clamping cycle:
     | 0 = Off;
     | 1 = On.  

.. option:: O48
   
   -Max  100
   -Min  0
   -Unit  %
   -Description  Clamp:duty cycle[%] in :term:`time period t2`.
