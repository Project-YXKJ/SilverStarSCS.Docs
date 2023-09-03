.. _puller:

Parameter List
==============

P00
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.
     
====== 
Puller 
======

How it works
============

- During lifting, raising of puller when lifting the sewing foot.
- During bartack, raising of puller when sewing the start/end bartack.
- During backwards, raising of puller when reverse button pressed.
- The puller is to be switched on via a button, if the puller is switched off, it is always up, if the button is pressed, the puller goes down.

# Parameter List
================

A89
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | puller function enable:
     | 0 = Off;
     | 1 = On.

A90
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | puller state(read only)
     | 0 = down;
     | 1 = raise up

O97
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down

   -Max  999
   -Min  1
   -Unit  ms
   -Description  Full activation duration.

O98
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down

   -Max  100
   -Min  1
   -Unit  --
   -Description  Duty cycle in time period when PWM activation.

A64
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down

   -Max  255
   -Min  0
   -Unit  stitch
   -Description
    | Delay stitches after foot down
    | 0 = foot lifter goes down, the puller goes down immediately;
    | N = At seam start, the puller goes down after sew N stitches; in the seam, puller go up/down with sewing foot lifter.
