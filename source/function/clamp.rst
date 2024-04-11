.. _thread_clamp:

============
Thread clamp
============

Thread clamp at seam start
--------------------------

Switch on at position set by :option:`D 07`, switch off at position set by :option:`D 08`.

Action only during the first stitch, reset after thread trim.

Thread clamp at turning back
----------------------------

Switch on during turning back, the Max. permissible time is set by :option:`T 15`
to protect from damage.

Thread clamp at sewing foot lifting
-----------------------------------

Switch on during foot lifting, the Max. permissible time is set by :option:`T 15`
to protect from damage.

Quick reference
===============

This table summarizes which parameter should be used for clamp:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Thread clamp                                         Operator   :option:`A 10`
Action Time of Clamp                                 Technician :option:`T 15`
Auto Mode for Clamp                                  Technician :option:`A 29`
Start Clamp Position                                 Technician :option:`D 07`
Stop Clamp Position                                  Technician :option:`D 08`
PrePressure duiring Clamp                            Technician :option:`O 42`
Duty cycle(t2)                                       Developer  :option:`O 48`
==================================================== ========== ==============

Parameter List
==============

.. option:: T 15
   
   -Max  2000
   -Min  1
   -Unit  ms
   -Description  Action time of clamp when lifting the foot or lifting the needlebar after trim.

.. option:: A 10
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread clamp:
     | 0 = Off;
     | 1 = On.

.. option:: A 29
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | 0 = actions when start sewing;
     | 1 = actions when start sewing and lifting the needle after trim;
     | 2 = actions when start sewing and lifting the foot;
     | 3 = both 1&2.

.. option:: D 07
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of clamp is activated.

.. option:: D 08
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of clamp is deactivated.

.. option:: O 42
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Reduce the sewing foot pressure during the clamping cycle:
     | 0 = Off;
     | 1 = On.  

.. option:: O 48
   
   -Max  100
   -Min  0
   -Unit  %
   -Description  Clamp:duty cycle[%] in :term:`time period t2`.
