.. _safety-sensor:

=============
Safety Sensor
=============

Tilt safaty switch
==================

Quick reference
---------------

This table summarizes which parameter should be used for tilt safaty switch:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Debouncing of Tilt safaty Switch                     Technician :option:`T 09`
Warning: Tilt safety switch                          Technician :option:`O 31`
Sensor Polarity(Tilt Safety)                         Technician :option:`O 32`
==================================================== ========== ==============

Eye Guard
=========

Quick reference
---------------

This table summarizes which parameter should be used for eye guard:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Warning: Eye Guard                                   Technician :option:`O 28`
==================================================== ========== ==============

Hook cover missing
==================

Quick reference
---------------

This table summarizes which parameter should be used for hook cover missing:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Warning: Hook Cover                                  Technician :option:`O 29`
==================================================== ========== ==============

Oil Level
=========

Quick reference
---------------

This table summarizes which parameter should be used for oil level:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Warning:Oil Level                                    Technician :option:`O 34`
==================================================== ========== ==============

Upper Thread Breaking
=====================

Quick reference
---------------

This table summarizes which parameter should be used for upper thread breaking:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Debouncing of Upper Thread Break                     Technician :option:`T 13` 
Sensor Polarity(Upper Thread Breaking)               Technician :option:`O 92`
==================================================== ========== ==============

Parameter List
==============

.. option:: T 09
   
   -Max  1000
   -Min  1
   -Unit  ms
   -Description  The time is less and the sensitivity is higher,perfect debounce 
                 time can prevent false alarm

.. option:: O 31

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether to throw a warning when the machine is tilted:
     | 0 = Off;
     | 1 = On.
     
.. option:: O 32
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Normal close;
     | 1 = Normal open.

.. option:: O 28
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Optional features,whether to throw a warning when the eye guard isn't in the
       right place:
     | 0 = Off;
     | 1 = On.

.. option:: O 29
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Optional features,whether to throw a warning when the hook cover is removed:
     | 0 = Off;
     | 1 = On.

.. option:: O 34
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Optional features,whether to throw a warning when the lubricating oil level
       is too low:
     | 0 = Off;
     | 1 = On.

.. option:: T 13

   -Max  1
   -Min  0
   -Unit  --
   -Description  The time is less and the sensitivity is higher, perfect debounce
     time can prevent false alarm.

.. option:: O 92
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Normal open;
     | 1 = Normal closed.
