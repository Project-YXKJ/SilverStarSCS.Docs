Second stitch length
====================

Connect a button and configure its corresponding input port for stitch length switching,
allowing you to quickly switch between two stitch lengths.

Speed Limitation when long stitch length activated
--------------------------------------------------

If parameter :option:`O33` set to 1, the speed is reduced down to parameter
:option:`S17` when long stitch length activated.

Quick reference
---------------

This table summarizes which parameter should be used for second stitch length:

====================================== ========== =============
Parameter                              Authority  See also
====================================== ========== =============
Second Stitch Length                   Operator   :option:`A46`
Sewing speed during long stitch length Operator   :option:`S17`
Status(Read Only)                      Technician :option:`A25`
Stitch length during backtack          Technician :option:`A50`
Speed limit during long stitch length  Technician :option:`O33`
Full power duration                    Developer  :option:`O78`
Duty cycle after full power            Developer  :option:`O79`
====================================== ========== =============

Parameter List
--------------

.. option:: A46

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Second Stitch Length:
      | 0 = Off;
      | 1 = On.

.. option:: S17

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Sewing speed if long stitch length is activated.

.. option:: A25

    -Max  1
    -Min  0
    -Unit  --
    -Description  Status of the second stitch length, read only.

.. option:: A50

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | When sewing start or end backtack, automatically switch to small stitch length:
      | 0 = Off;
      | 1 = On.

.. option:: O33

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Speed limit during long stitch length:
      | 0 = Off;
      | 1 = On.

.. option:: O78

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Second stitch length:  full power duration, :term:`time period t1` .

.. option:: O79

    -Max  100
    -Min  1
    -Unit  %
    -Description  Second stitch length: duty cycle after full power in :term:`time period t2`.
