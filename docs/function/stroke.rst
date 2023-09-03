.. _stroke:

==================
Sewing foot stroke
==================


**Speed limitation sewing foot stroke**

if parameter **A35** set to 1, when 2nd sewing foot stroke is activated, the speed is 
reduced down to the desired value of 2nd sewing foot stroke which set by **S15**.

**Number of stitches 2nd stroke off**

if **A32** is not 0, when switching to 2nd sewing foot stroke, after sewing N stitches 
set by **A32**, the second sewing foot stroke is automatically deactivated.


Parameter List
==============

S09
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke knob type is switch: limit speed for 1st sewing foot stroke

S10
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke knob type is switch: limit speed for 2nd sewing foot stroke

S11
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is potentiometer: limit speed for low stroke height

S12
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke knob type is switch: limit speed for 3rd sewing foot stroke

S13
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke knob type is switch: limit speed for 4th sewing foot stroke

S13
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke knob type is switch: limit speed for 4th sewing foot stroke


S14
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is potentiometer: limit speed for high stroke height

S15
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Limit speed for the maximum sewing foot stroke

A32
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  99
   -Min  0
   -Unit  stitches
   -Description  Number of stitches after which the second sewing foot stroke is automatically deactivated

A35
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  stitches
   -Description
     | Speed limitation sewing foot stroke:
     | 0 = Off
     | 1 = On

085
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  0
   -Unit  stitches
   -Description
     | Sensor type of stroke height knob:
     | 0 = No;
     | 1 = Switch;
     | 2 = Potentiometer

076
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  Activation duration of the foot stroke in the time period T1(100% duty)

077
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Duty cycle in time period T2(PWM)
