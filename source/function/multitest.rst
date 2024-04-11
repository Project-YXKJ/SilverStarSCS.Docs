.. _multitest:

=========
Multitest
=========

.. danger:: 
   Please set these options carefully!
   
   Risk of injury from moving, cutting and sharp parts!

When the endurance test starts, the machine will run automatically until the test time 
which set by :option:`O 25` is reached.

Quick reference
===============

This table summarizes which parameter should be used for multitest:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Running Time(EC)                                     Technician :option:`O 23`
Standby Time(EC)                                     Technician :option:`O 24`
Total Time(EC)                                       Technician :option:`O 25`
Endurance Running                                    Technician :option:`O 26`
==================================================== ========== ==============

Parameter List
==============

.. option:: O 23
   
   -Max  60
   -Min  1
   -Unit  s
   -Description  Running time of an endurance cycle,unit:second

.. option:: O 24
   
   -Max  60
   -Min  1
   -Unit  s
   -Description  Standby time of an endurance cycle,unit:second

.. option:: O 25
   
   -Max  720
   -Min  1
   -Unit  h
   -Description  Total endurance time,unit:hour

.. option:: O 26
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether to start an endurance running test:
     | 0 = Off;
     | 1 = On.
