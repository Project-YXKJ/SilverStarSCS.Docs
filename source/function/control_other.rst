.. _control_other:

==============
Control, other
==============

Quick reference
===============

This table summarizes which parameter should be used for control and other:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Data Sending Interval                                Technician :option:`T 14`
IoT                                                  Technician :option:`A 49`
Lock Panel                                           Technician :option:`A 52`
Debug                                                Technician :option:`A 58`
Reset statisc data                                   Technician :option:`A 59`
Password Required                                    Technician :option:`O 15`
Clear error log                                      Technician :option:`O 17`
Password                                             Technician :option:`O 27`
Reset parameter                                      Technician :option:`O 51`
Reset the MACHINE ZERO                               Technician :option:`O 52`
Factory reset                                        Technician :option:`O 66`
Bus Voltage Error Reporting                          Technician :option:`O 70`
AC Voltage Error Reporting                           Technician :option:`O 71`
Max. Bus Voltage                                     Technician :option:`I 44`
Max. AC Voltage                                      Technician :option:`I 45`
==================================================== ========== ==============

Parameter List
==============

.. option:: T 14

   -Max  9999
   -Min  1
   -Unit  ms
   -Description  Interval time for sending IoT data

.. option:: A 49

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | IoT network:
     | 0 = Off;
     | 1 = On.

.. option:: A 52
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the panel can be operated when foot lifting:
     | 0 = Not allowed;
     | 1 = Allowed.

.. option:: A 58

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Debug serial port output function:
     | 0 = Off;
     | 1 = On.

.. option:: A 59
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1, statisc data will be restored to default values after power cycle.

.. option:: O 15
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether a password is required for parameter adjustment:
     | 0 = Off;
     | 1 = On.

.. option:: O 17
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1,error log clead after power cycle.

.. option:: O 27
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Password required to adjust parameters.

.. option:: O 51
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1, parameters will be restored to default values after power cycle.

.. option:: O 52
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1,the :term:`MACHINE ZERO` will be reset after power cycle

.. option:: O 66
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1,reset all parameters to default value,clear the error log and stastics information,reset MACHINE ZERO after power cycle.

.. option:: O 70
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether to throw a error if bus voltage is too high:
     | 0 = Off;
     | 1 = On.
   
.. option:: O 71
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether to throw a error if AC 220 voltage is too high:
     | 0 = Off;
     | 1 = On.

.. option:: I 44
   
   -Max  460
   -Min  400
   -Unit  --
   -Description  Maximum bus voltage

.. option:: I 45

   -Max  300
   -Min  260
   -Unit  V
   -Description  Maximum AC voltage
