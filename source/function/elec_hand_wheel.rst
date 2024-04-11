.. _hand_wheel:

==================
Electric Handwheel
==================

Only works when the machine stops.

Quick reference
===============

This table summarizes which parameter should be used for electric handwheel:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Elec-Handwheel                                       Operator   :option:`A 23`
Rotation Direction of Elec-Handwheel                 Technician :option:`A 43` 
Elec-Handwheel Step                                  Technician :option:`O 83`
Elec-Handwheel Speed                                 Technician :option:`O 84`
==================================================== ========== ==============

Parameter List
==============

.. option:: A 23
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Electronic handwheel:
     | 0 = Off;
     | 1 = On.
     
.. option:: A 43
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Rotation direction of electronic handwheel:
     | 0 = Same with main motor;
     | 1 = Contrary.   

.. option:: O 83
   
   -Max  720
   -Min  0
   -Unit  --
   -Description  Step width for electronic handwheel

.. option:: O 84
   
   -Max  200
   -Min  0
   -Unit  spm
   -Description  The speed of motor when using electric handwheel
