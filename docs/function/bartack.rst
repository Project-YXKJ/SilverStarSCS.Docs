.. _bartack:

=======
Bartack
=======

**Stitch in stitch**

Parameter List
==============

P00
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.

S03
---
.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Speed in bartack at seam begin

S04
---
.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Speed in bartack at seam end


T01
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Reverse solenoid action time

T02
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Reverse solenoid release time

D05
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Reverse power on angle
     | The description can also start on the next line.
     | value1: text;
     | value2: text.
  
D06
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Reverse power off angle

A20
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Reverse power on angle
     | Ornamental-stitch bartack at seam start:
     | 0 = Off;
     | 1 = On, the motor will stopped at sewing direction change point

A22
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Reverse power on angle
     | Ornamental-stitch bartack at seam end:
     | 0 = Off;
     | 1 = On, the motor will stopped at sewing direction change point
 
T11
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1000
   -Min  1
   -Unit  ms
   -Description  Stop time for sewing direction change of individual bartack sections in order to reach the specified stitch lengths(forwards/backwards)

O09
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Activation duration of the reverse in the time period T1(100% duty)

O10
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Timeout release:
     | 0 = Off;
     | 1 = On

O11
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  The maximum time the reverse can powered on

O41
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  stitches
   -Description  Number of A-stitches which speed holding after sewing start bartck

O42
___

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  stitches
   -Description  none

O12
___

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Speed limt when number of bartack stitches is equal to 1



O13 
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Speed limt when number of bartack stitches is equal to 2

O14
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Speed limt when number of bartack stitches is equal to 3
