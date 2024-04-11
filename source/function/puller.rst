.. _puller:

======
Puller
======

Automation rules
================

Automation rules allow puller to automate actions while lifting or bartack.

How automation rules work:

* During lifting, raising of puller when lifting the sewing foot.
* During bartack, raising of puller when sewing the start/end bartack.
* During backwards, raising of puller when reverse button pressed.
* The puller is to be switched on via a button, if the puller is switched off, 
  it is always up, if the button is pressed, the puller goes down.

Quick reference
===============

This table summarizes which parameter should be used for puller:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Puller                                               Operator   :option:`A 89`
Delay stitch                                         Technician :option:`A 64`
Upper Puller Status                                  Developer  :option:`A 90`
Time(t1)                                             Developer  :option:`O 97`
Duty cycle(t2)                                       Developer  :option:`O 98`
==================================================== ========== ==============

Parameter List
================

.. option:: A 64

   -Max  255
   -Min  0
   -Unit  stitch
   -Description  Number of stitches until the puller is lowered after seam begin,
                 depens on stitch length and application.

.. option:: A 89

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Upper puller:
     | 0 = Off;
     | 1 = On.

.. option:: A 90

   -Max  1
   -Min  0
   -Unit  --
   -Description  Upper puller status,up or down(read only).

.. option:: O 97

   -Max  999
   -Min  1
   -Unit  ms
   -Description  Puller lifter:activation duration of in :term:`time period t1` (100% duty cycle).

.. option:: O 98

   -Max  100
   -Min  1
   -Unit  --
   -Description  Puller lifter:duty cycle[%] in :term:`time period t2`.
