Thread wiper
============

Thread wiper has two different action modes:

- Mode 1

  Set :option:`A08` to 1 to enable this function.

  When thread trimmer is completed and the time set by :option:`T03` is delayed, the
  wiper will switch on, it will switch off after the time set by :option:`T04`.

- Mode 2

  Set :option:`A08` to 2 to enable this function.

  When thread trimmer is completed, while lifting the foot for the first time, the wiper
  will switch on, it will switch off after the time set by :option:`T04`.

Quick reference
---------------

This table summarizes which parameter should be used for wiper:

================================= ========== =============
Parameter                         Authority  See also
================================= ========== =============
Thread wiper                      Operator   :option:`A08`
Switch-on delay for thread wiper  Technician :option:`T03`
Switch-on period for thread wiper Technician :option:`T04`
================================= ========== =============

Parameter List
--------------

.. option:: A08

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Wiper thread:
      | 0 = Off;
      | 1 = Mode 1;
      | 2 = Mode 2.

.. option:: T03

    -Max  200
    -Min  1
    -Unit  ms
    -Description  Switch on delay time for thread wiper after trim.

.. option:: T04

    -Max  200
    -Min  1
    -Unit  ms
    -Description  Switch on period for thread wiper.
