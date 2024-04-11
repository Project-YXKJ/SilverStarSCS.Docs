.. _second_stitch_length:

====================
Second stitch length
====================

Depending on the equipment, the machine has can be used to sew two different
stitch lengths, and it can be activated with a press of button.

Automation rules
================

Speed limit when long stitch length activated
---------------------------------------------

If parameter :option:`O 33` set to 1, the speed is reduced down to parameter
:option:`S 17` when long stitch length activated.

Quick reference
===============

This table summarizes which parameter should be used for second stitch length:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Stitch Length                                        Technician :option:`A 46`
Max. Speed Long Stitch Length                        Operator   :option:`S 17`
Status of Second Stitch Length                       Technician :option:`A 25`
Stitch length during bartack                         Technician :option:`A 50`
Speed limitation stitch length                       Technician :option:`O 33`
Time(t1)                                             Developer  :option:`O 78`
Duty cycle(t2)                                       Developer  :option:`O 79`
==================================================== ========== ==============

Parameter List
==============

.. option:: S 17
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Limiting speed if long stitch length is activated

.. option:: A 25
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the second stitch length solenoid(read only)

.. option:: A 46
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Short/Long stitch length:
     | 0 = Off;
     | 1 = On.

.. option:: A 50
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Choose whether to switch short stitch length automatically:
     | 0 = Off;
     | 1 = On.

.. option:: O 33
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | The speed is limited during using long stitch length:
     | 0 = Off;
     | 1 = On.

.. option:: O 78
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Second stitch length:activation duration of in :term:`time period t1`
                 (100% duty cycle).

.. option:: O 79
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Second stitch length:duty cycle[%] in :term:`time period t2`.
