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

============================== ========== =============
Parameter                      Authority  See also
============================== ========== =============
Stitch Length                  Operator   :option:`A46`
Max. Speed Long Stitch Length  Operator   :option:`S17`
Status of Second Stitch Length Technician :option:`A25`
Stitch length during backtack  Technician :option:`A50`
Speed limitation stitch length Technician :option:`O33`
Time(t1)                       Developer  :option:`O78`
Duty cycle(t2)                 Developer  :option:`O79`
============================== ========== =============

Parameter List
--------------

.. option:: A46

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Short/Long stitch length:
      | 0 = Off;
      | 1 = On.

.. option:: S17

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Limiting speed if long stitch length is activated

.. option:: A25

    -Max  1
    -Min  0
    -Unit  --
    -Description  Status of the second stitch length solenoid(read only)

.. option:: A50

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Choose whether to switch short stitch length automatically:
      | 0 = Off;
      | 1 = On.

.. option:: O33

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | The speed is limited during using long stitch length:
      | 0 = Off;
      | 1 = On.

.. option:: O78

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Second stitch length: activation duration of in :term:`time period t1`
                  (100% duty cycle).

.. option:: O79

    -Max  100
    -Min  1
    -Unit  %
    -Description  Second stitch length: duty cycle[%] in :term:`time period t2`.
