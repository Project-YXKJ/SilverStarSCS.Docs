.. _hand_wheel:

==================
Electric Handwheel
==================

This function is only effective when the machine stops.

Quick reference
===============

This table summarizes which parameter should be used for electric handwheel:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Elec-Handwheel                                       Operator   :option:`A23`
Rotation Direction of Elec-Handwheel                 Technician :option:`A43` 
Elec-Handwheel Step                                  Technician :option:`O83`
Elec-Handwheel Speed                                 Technician :option:`O84`
==================================================== ========== ==============

Parameter List
==============

.. option:: A23
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Electronic handwheel:
     | 0 = Off;
     | 1 = On.
     
.. option:: A43
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Rotation direction of electronic handwheel:
     | 0 = Same with main motor;
     | 1 = Contrary.   

.. option:: O83
   
   -Max  720
   -Min  0
   -Unit  --
   -Description  Step width for electronic handwheel.

.. option:: O84
   
   -Max  200
   -Min  0
   -Unit  spm
   -Description  The speed of motor when using electric handwheel.
