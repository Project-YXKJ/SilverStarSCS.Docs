.. _thread_wiper:

============
Thread wiper
============

*Thread wiper has two different action modes:*

Upper thread wiper function
   Set :option:`A 08` to 1 to enable this function.
   
   When thread cutter is completed and the time set by :option:`T 03` is delayed, the wiper 
   will switch on, it will switch off after the time set by :option:`T 04`.

lower thread wiper function
   Set :option:`A 08` to 2 to enable this function.

   When thread cutter is completed, while lifting the foot for the first time, the wiper
   will switch on, it will switch off after the time set by :option:`T 04`

Quick reference
===============

This table summarizes which parameter should be used for wiper:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Wiper                                                Operator   :option:`A 08`
Wiper Delay time                                     Technician :option:`T 03`
Wiper Activation Duration                            Technician :option:`T 04`
==================================================== ========== ==============

Parameter List
==============

.. option:: A 08
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Wiper thread:
     | 0 = Off;
     | 1 = Upper thread;
     | 2 = Lower thread;
     
.. option:: T 03
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Lag time, after which, wiper is activaed after trim

.. option:: T 04
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Time form activation to deactivation of the magnet of wiper.
