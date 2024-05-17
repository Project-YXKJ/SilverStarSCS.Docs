.. _needle_cooling:

============== 
Needle cooling
==============

Needle cooling can assist in cooling the needle to avoid damage to 
the sewing material and breakage of the upper thread.

How it works?
=============

Above the speed set by :option:`S18`, the needle cooling start;

Below the speed set by :option:`S18`, the needle cooling does not stop immediately,
needle cooling to continue until the time setted by :option:`T16` has elapsed.

During the follow-up time, if the speed exceeds :option:`S18` again,
the needle cooling start again.

Quick reference
===============

This table summarizes which parameter should be used for needle cooling:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Needle Cooling                                       Operator   :option:`A48`
Cool Speed                                           Technician :option:`S18`
Needle Cooling Follow Up Time                        Technician :option:`T16`
Time(t1)                                             Developer  :option:`O93`
Duty cycle(t2)                                       Developer  :option:`O94`
==================================================== ========== ==============

Parameter List
==============

.. option:: A48
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Needle cooling function:
     | 0 = Off;
     | 1 = On.

.. option:: S18
   
   -Max  4500
   -Min  50
   -Unit  spm
   -Description  Above this speed,the needle cooling is activated.

.. option:: T16
   
   -Max  10
   -Min  0
   -Unit  s
   -Description  Lag time, after which,needle cooling is deactivaed when speed
                 lower than cool speed.

.. option:: O93
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Needle cooling: activation duration of in :term:`time period t1` (100% duty cycle).

.. option:: O94
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Needle cooling: duty cycle[%] in :term:`time period t2`.
