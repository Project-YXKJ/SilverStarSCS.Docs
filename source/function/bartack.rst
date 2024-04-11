.. _bartack:

=======
Bartack
=======

Stitch in stitch
================

.. important::
   Before adjustment, make sure that forward stitch length is the same with backward 
   stitch length use the reverse lever.

The time it takes for reverse actuator actions, adjust parameter T01 as the guide
of following figure:

+------------------------------------------+------------------------------------------+
| Decrease T01                             | Increase T01                             |
+==========================================+==========================================+
| .. image:: ../_static/common/sub-T01.svg | .. image:: ../_static/common/add-T01.svg |
+    :scale: 150 %                         +    :scale: 150 %                         +
|                                          |                                          |
+------------------------------------------+------------------------------------------+

The time it takes for reverse actuator releases, adjust parameter T02 as the guide
of following figure:

+------------------------------------------+------------------------------------------+
| Decrease T02                             | Increase T02                             |
+==========================================+==========================================+
| .. image:: ../_static/common/sub-T02.svg | .. image:: ../_static/common/add-T02.svg |
+    :scale: 150 %                         +    :scale: 150 %                         +
|                                          |                                          |
+------------------------------------------+------------------------------------------+

SD Mode
=======

SD mode is a special mode of start/end bartack, used to ensure the seam looks better.

When the SD mode is enabled, the motor will pause at the collagen turning point and 
wait for the time set by :option:`T 11` to ensure that the reverse action in place, 
then the motor continue running.

SD mode can be activated for start bartack or end bartack respectively, 
controlled by :option:`A 20` and :option:`A 22`.

Quick reference
===============

This table summarizes which parameter should be used for bartack:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Speed in Start Bartack                               Technician :option:`S 03`
Speed in End Bartack                                 Technician :option:`S 04`
Reverse Action In Place Time                         Technician :option:`T 01`
Reverse Release In Place Time                        Technician :option:`T 02`
SD Mode Stop Time                                    Technician :option:`T 11` 
SD mode for Start Bartack                            Operator   :option:`A 20`
SD mode for End Bartack                              Operator   :option:`A 22`
Maintain Speed after Start Bartack                   Technician :option:`A 34`
Start Reverse Position                               Technician :option:`D 05`
Stop Reverse Position                                Technician :option:`D 06`
Auto Power-off Reverse                               Technician :option:`O 10`
Reverse Max. Holding Time                            Technician :option:`O 11`
Max. Speed of 1 stitch                               Technician :option:`O 12` 
Max. Speed of 2 stitch                               Technician :option:`O 13`   
Max. Speed of 3 stitch                               Technician :option:`O 14` 
Stitches of Maintain Speed after Start Bartack       Technician :option:`O 41` 
Time(t1)                                             Developer  :option:`T 08`
Duty cycle(t2)                                       Developer  :option:`O 09`
==================================================== ========== ==============

Parameter List
==============

.. option:: S 03
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in bartack at seam begin.

.. option:: S 04
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in bartack at seam end.

.. option:: T 01
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  The time for the reverse solenoid finish the action,unit ms

.. option:: T 02
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  The time for reverse solenoid finish the releasing,unit ms

.. option:: T 08
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Reverse:activation duration of in :term:`time period t1`
                 (100% duty cycle),unit ms
                 
.. option:: T 11
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Motor standby duration at direction change of bartack if SD mode is On.

.. option:: A 20
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Stop at direction change of start tacking in order to the bartack magnet reach the specified position:
     | 0 = Off;
     | 1 = On.

.. option:: A 22
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Stop at direction change of end tacking in order to the bartack magnet reach the specified position:
     | 0 = Off;
     | 1 = On.

.. option:: A 34
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Reverse power on angle
     | For better performance of start bartack:
     | 0 = Off;
     | 1 = On.

.. option:: D 05
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of reverse is activated.
  
.. option:: D 06
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of reverse is deactivated.

.. option:: O 09
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Reverse:duty cycle[%] in :term:`time period t2`.

.. option:: O 10
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether the magnet of reverse automatic power-off after the set time:
     | 0 = Off;
     | 1 = On

.. option:: O 11

   -Max  30
   -Min  5
   -Unit  s
   -Description  If Auto Power-off Reverse is turned on,this parameter sets the power-off time.

.. option:: O 12
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum Speed of 1 stitch when bartack or W-sewing.

.. option:: O 13 
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum Speed of 2 stitch when bartack or W-sewing.

.. option:: O 14
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum Speed of 3 stitch when bartack or W-sewing.

.. option:: O 41
   
   -Max  10
   -Min  0
   -Unit  stitches
   -Description  Number of A-stitches which speed holding after sewing start bartck.
