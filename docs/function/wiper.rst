.. _thread_wiper:

============
Thread wiper
============

The thread wiper function runs after the cutting procedure.

When thread cutter is completed and the time set by **T03** is delayed, the wiper 
will switch on, it will switch off after the time set by **T04**.

Parameter List
==============

A08
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread wiper function:
     | 0: Off;
     | 1: On.
     
T03
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Thread wiper switched on delay time

T04
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Thread wiper switched on duration
