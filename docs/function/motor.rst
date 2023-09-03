.. _motor: 

=====
Motor
=====

**Holding force of the motor:**

Enable this function by set **A54** to 1.

This function prevents unwanted wandering of the needle when machine has stopped. The effect can be checked by turning the hand wheel.

The maximum time the holding force can keep takes effect is determined by parameter **A66**.

- If **A66** equal to 0, it take effect always when stopped.
- If **A66** is not equal to 0, effective time is the value set by **A66**.

Parameter List
==============

S01
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed by pressing the pedal to the end position
     
S02
---
.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Minimum sewing speed, it is also the needle position up-down speed

A54
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Holding force of the motor:
     | 0 = Off;
     | 1 = On

A66
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Motor Holding duration:
     | 0 = Always;
     | N = After N ms, the holding force is released

D01
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Needle up position

D02
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Needle down position

O04
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Motor drive type:
     | 0 = Belt connection
     | 1 = Direct drive

O67
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Motor rotation direction:
     | 0 = Clockwise
     | 1 = Anticlockwise

I01
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  150
   -Unit  ms
   -Description  Acceleration, acceleration time from 0 to 4500rpm  

I02
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  150
   -Unit  ms
   -Description  Deceleration, deceleration time from 4500 to 0rpm 

I04
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  4096
   -Min  1 
   -Unit  --
   -Description  The number of code disc signals corresponding to one mechanical circle

I37
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0 
   -Unit  1°
   -Description  Braking advance deceleration distance

I30
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0 
   -Unit  --
   -Description  
     | Brake method
     | 0 = Soft stop;
     | 1 = Postion.
