.. _bartack:

=======
Bartack
=======

**Stitch in stitch**

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

**SD Mode**

SD mode is a special mode of start/end bartack, used to ensure the seam looks better.

When the SD mode is enabled, the motor will pause at the collagen turning point and 
wait for the time set by `T 11`_ to ensure that the reverse action in place, 
then the motor continue running.

SD mode can be activated for start bartack or end bartack respectively, 
controlled by `A 20`_ and `A 22`_ .

Parameter List
==============

S 03
----
.. dropdown:: Speed in Start Bartack <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in bartack at seam begin.

S 04
----
.. dropdown:: Speed in End Bartack <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in bartack at seam end.

T 01
----

.. dropdown:: Reverse Action In Place Time <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  The time for the reverse solenoid finish the action,unit ms

T 02
----

.. dropdown:: Reverse Release In Place Time <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  The time for reverse solenoid finish the releasing,unit ms

T 08
----

.. dropdown:: Time(t1) <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Reverse:activation duration of in :term:`time period t1`
                 (100% duty cycle),unit ms
                 
T 11
----
.. dropdown:: SD Mode Stop Time <...> 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Motor standby duration at direction change of bartack if SD mode is On.

A 20
----

.. dropdown:: SD mode for Start Bartack <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Stop at direction change of start tacking in order to the bartack magnet reach the specified position:
     | 0 = Off;
     | 1 = On.

A 22
----

.. dropdown:: SD mode for End Bartack <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Stop at direction change of end tacking in order to the bartack magnet reach the specified position:
     | 0 = Off;
     | 1 = On.

A 34
----

.. dropdown:: Maintain Speed after Start Bartack <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Reverse power on angle
     | For better performance of start bartack:
     | 0 = Off;
     | 1 = On.

D 05
----

.. dropdown:: Start Reverse Position <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of reverse is activated.
  
D 06
----

.. dropdown:: Stop Reverse Position <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of reverse is deactivated.

O 09
----

.. dropdown:: Duty cycle(t2) <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Reverse:duty cycle[%] in :term:`time period t2`.

O 10
----

.. dropdown:: Auto Power-off Reverse <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether the magnet of reverse automatic power-off after the set time:
     | 0 = Off;
     | 1 = On

O 11
----

.. dropdown:: Reverse Max. Holding Time <...>
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  If Auto Power-off Reverse is turned on,this parameter sets the power-off time.

O 12
----

.. dropdown:: Max. Speed of 1 stitch <...> 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum Speed of 1 stitch when bartack or W-sewing.

O 13 
----

.. dropdown:: Max. Speed of 2 stitch <...>  
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum Speed of 2 stitch when bartack or W-sewing.

O 14
----

.. dropdown:: Max. Speed of 3 stitch <...> 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum Speed of 3 stitch when bartack or W-sewing.

O 41
----

.. dropdown:: Stitches of Maintain Speed after Start Bartack <...> 
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  stitches
   -Description  Number of A-stitches which speed holding after sewing start bartck.
