.. _bobbin_monitor:

==============
Bobbin Monitor
==============

Using Lower thread counter allows users to know the remaining thread amount.


**Here is a formula**:

Remaining thread amount = reset value of the bobbin thread counter(O43) - bobbin thread counter value(O44).

**Setup steps**:

- Set an appropriate value for O19, every time N stitches are sewn which set by parameter O19, the counter(O44) increases by 1.

- Set an appropriate value for O43, this is a very variable value, which depends on the size of the bobbin and the thickness of the thread.

- Choose when to throw a warning by setting O20, immediately or after thread cutting.

- Enable counter.
- As the sewing, the remaining thread amount(O43-O44) is counted down, when it reaches 0, the machine will stop, and the controller will throw a warning(Code 5). A reset is needed if you want continue.


Parameter List
==============

A12
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Lower thread counter:
     | 0: Off;
     | 1: On.

O43
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  Reset value of lower thread counter

O44
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Current value of Lower thread counter

O19
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  stitches
   -Description  Factor of lower thread counter

O20
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  stitches
   -Description  
     | Choose when to throw warning if the counter reaches 0:
     | 0 = after thread cutting;
     | 1 = immediately
