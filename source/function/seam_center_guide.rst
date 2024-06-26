.. _seam_center_guide:

=================
Seam center guide
=================

Automation rules
================

Automatic lifting seam center guide is associated with three situations: 

* Sew Foot
* Bartack(start or end tack) and reverse
* Stroke

How automation rules work
-------------------------

Rule is seted by :option:`A51`:

* 0 = Toggle seam center guide raise up/down via a manual button;
* 1 = Raising of seam center guide when lifting the sewing foot;
* 2 = Raising of seam center guide when sewing the bartack/reverse;
* 3 = Raising of seam center guide when sewing the bartack/reverse and 
      lifting the sewing foot;
* 4 = Raising of seam center guide when high stroke;
* 5 = Raising of seam center guide when lifting the sewing foot and high stroke;
* 6 = Raising of seam center guide when sewing the bartack/reverse and high stroke;
* 7 = Raising of seam center guide when lifting the sewing foot, sewing 
      the bartack/reverse and high stroke.

Quick reference
===============

This table summarizes which parameter should be used for wiper:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Seam Center Guide                                    Operator   :option:`A47`
Auto Mode for Seam Center Guide                      Technician :option:`A51`
Status of Seam Center Guide                          Developer  :option:`A33`
Time(t1)                                             Developer  :option:`O89`
Duty cycle(t2)                                       Developer  :option:`O90`
==================================================== ========== ==============

Parameter List
==============

.. option:: A47
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Seam center guide function:
     | 0 = Off;
     | 1 = On.

.. option:: A51

   -Max  7
   -Min  0
   -Unit  --
   -Description
     | 0 = Manual;
     | 1 = Automatically up when foot lifting;
     | 2 = Automatically up when bartacking and reverse;
     | 3 = Both 1&2;
     | 4 = Automatically up when high stroke;
     | 5 = Both 1&4;
     | 6 = Both 2&4;
     | 7 = Both 1&2&4.

.. option:: A33
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the seam center guide solenoid(read only)

.. option:: O89
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Seam Center Guide: activation duration of in :term:`time period t1`
                 (100% duty cycle).

.. option:: O90
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Seam Center Guide: duty cycle[%] in :term:`time period t2`.
