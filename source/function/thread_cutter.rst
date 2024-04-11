.. _thread_cutter:

=============
Thread cutter
=============

*Thread cutting procedure:*

Thread cutting singnal is switched on when the angle value :option:`D 03` has been reached,
the switched off when the angle value :option:`D 04` . If the position is not reached because
of a mechanical error, the thread cutter signal is switched off after 500ms for protect
the magnet from damage.

Quick reference
===============

This table summarizes which parameter should be used for thread cutter:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Thread Trim                                          Operator   :option:`A 06`
Trimming Speed                                       Technician :option:`S 07`
Short Thread Cutter                                  Technician :option:`A 42`
Short Thread Cutter Stitches                         Technician :option:`A 67`
Start trim position                                  Technician :option:`D 03`
Stop trim position                                   Technician :option:`D 04`
Start Movable Knife Position(STC)                    Technician :option:`D 17`
Stop Movable Knife Position(STC)                     Technician :option:`D 18`  
Start Reverse Position(STC)                          Technician :option:`D 19` 
Stop Reverse Position(STC)                           Technician :option:`D 20`
Start Zero Stitch Length Position(STC)               Technician :option:`D 21`
Stop Zero Stitch Length Position(STC)                Technician :option:`D 22`
Pedal Reset After Trim                               Technician :option:`O 38`
Time(t1)                                             Developer  :option:`O 95`
Duty cycle(t2)                                       Developer  :option:`O 96`
==================================================== ========== ==============

Parameter List
==============

.. option:: S 07

   -Max  300
   -Min  150
   -Unit  spm
   -Description  Speed of the machine during trimming

.. option:: A 06
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread trim:
     | 0 = Off;
     | 1 = On.

.. option:: A 42
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Feature for specific models:
     | 0 = Off;
     | 1 = On.     

.. option:: A 67
   
   -Max  10
   -Min  0
   -Unit  stitches
   -Description  When short thread cutter active,number of short length stitches before trim.

.. option:: D 03
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of thread cutter is activated.


.. option:: D 04
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of thread cutter is deactivated.

.. option:: D 17
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of movable knife(short thread cutter) is activated.

.. option:: D 18
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of movable knife(short thread cutter) is deactivated.

.. option:: D 19
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of the reverse(short thread cutter) is activated.

.. option:: D 20
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of the reverse(short thread cutter) is deactivated.

.. option:: D 21
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of zero stitch length(short thread cutter) is activated.

.. option:: D 22
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of zero stitch length(short thread cutter) is deactivated.
   
.. option:: O 38
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the pedal need to return Position 0 before restart a new seam after trim:
     | 0 = Off;
     | 1 = On.

.. option:: O 95
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Short thread zero length:activation duration of in :term:`time period t1`
                 (100% duty cycle).

.. option:: O 96
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Short thread zero length:duty cycle[%] in :term:`time period t2`.
