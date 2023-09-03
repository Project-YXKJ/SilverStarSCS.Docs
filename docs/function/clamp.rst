.. _thread_clamp:

============
Thread clamp
============

**Thread clamp at seam start**:

Switch on at position set by **D07**, switch off at position set by **D08**.

Action only during the first stitch, reset after thread trim.

**Thread clamp at turning back**:

Switch on during turning back, the Max. permissible time is set by **T15** to protect from damage.

**Thread clamp at sewing foot lifting**:

Switch on during foot lifting, the Max. permissible time is set by **T15** to protect from damage.

Parameter List
==============

A10
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread clamp:
     | 0: Off;
     | 1: On.

A29
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | Thread clamp option:
     | 0: Thread clamp only at start of seam;
     | 1: Thread clamp at start of seam and at turning back;
     | 2: Thread clamp at start of seam and with foot lifting
     | 3: Thread clamp at start seam, at turning back and with foot lifting

T15
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  2000
   -Min  1
   -Unit  ms
   -Description  The maximum time the thread clamp can keep switch on

D07
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position for activating the thread clamp

D08
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position for deactivating the thread clamp

O42
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Reduce sewing foot lifter pressure during the clamping cycle:
     | 0: Off;
     | 1: On.  

O48
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  0
   -Unit  %
   -Description  Duty cycle in time period T2(PWM)   
