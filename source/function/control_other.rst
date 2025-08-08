Control, other
==============

Quick reference
---------------

This table summarizes which parameter should be used for control and other:

=========================== ========== =============
Parameter                   Authority  See also
=========================== ========== =============
Data Sending Interval       Technician :option:`T14`
IoT                         Technician :option:`A49`
Lock Panel                  Technician :option:`A52`
Debug                       Developer  :option:`A58`
Reset statisc data          Technician :option:`A59`
Password Required           Technician :option:`O15`
Clear error log             Technician :option:`O17`
Password                    Technician :option:`O27`
Reset parameter             Technician :option:`O51`
Reset the MACHINE ZERO      Technician :option:`O52`
Factory reset               Technician :option:`O66`
Bus Voltage Error Reporting Technician :option:`O70`
AC Voltage Error Reporting  Technician :option:`O71`
Max. Bus Voltage            Technician :option:`I44`
Max. AC Voltage             Technician :option:`I45`
=========================== ========== =============

Parameter List
--------------

.. option:: T14

    -Max  9999
    -Min  1
    -Unit  ms
    -Description  Interval time for sending IoT data

.. option:: A49

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | IoT network:
      | 0 = Off;
      | 1 = On.

.. option:: A52

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether the panel can be operated when foot lifting:
      | 0 = Not allowed;
      | 1 = Allowed.

.. option:: A58

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Debug serial port output function:
      | 0 = Off;
      | 1 = On.

.. option:: A59

    -Max  1
    -Min  0
    -Unit  --
    -Description  Set to 1, statisc data will be restored to default values after power cycle.

.. option:: O15

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether a password is required for parameter adjustment:
      | 0 = Off;
      | 1 = On.

.. option:: O17

    -Max  1
    -Min  0
    -Unit  --
    -Description  Set to 1,error log clead after power cycle.

.. option:: O27

    -Max  1
    -Min  0
    -Unit  --
    -Description  Password required to adjust parameters.

.. option:: O51

    -Max  1
    -Min  0
    -Unit  --
    -Description  Set to 1, parameters will be restored to default values after power cycle.

.. option:: O52

    -Max  1
    -Min  0
    -Unit  --
    -Description  Set to 1,the :term:`MACHINE ZERO` will be reset after power cycle

.. option:: O66

    -Max  1
    -Min  0
    -Unit  --
    -Description  Set to 1,reset all parameters to default value,clear the error log and stastics information,reset MACHINE ZERO after power cycle.

.. option:: O70

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether to throw a error if bus voltage is too high:
      | 0 = Off;
      | 1 = On.

.. option:: O71

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether to throw a error if AC 220 voltage is too high:
      | 0 = Off;
      | 1 = On.

.. option:: I44

    -Max  460
    -Min  400
    -Unit  V
    -Description  Maximum bus voltage

.. option:: I45

    -Max  300
    -Min  260
    -Unit  V
    -Description  Maximum AC voltage
