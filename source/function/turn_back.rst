Turn back
=========

Set :option:`A13` to 1 to enable the turn back function, this function helps remove the
materials and prevent the needle from scratching the fabric.

The turning back function runs after the cutting procedure. After the delay time set by
:option:`T12` , then it turns back at speed set by :option:`S16` . When position is
reached the angle set by :option:`O35` , the motor stops.

Quick reference
---------------

This table summarizes which parameter should be used for turn back:

============================== ========== =============
Parameter                      Authority  See also
============================== ========== =============
Turn Back                      Operator   :option:`A13`
Turn Back Speed                Technician :option:`S16`
Turn Back Delay                Technician :option:`T12`
Needle postion after turn back Technician :option:`O35`
============================== ========== =============

Parameter List
--------------

.. option:: A13

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Turn back:
      | 0 = Off;
      | 1 = On.

.. option:: S16

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  Positioning speed of turn back

.. option:: T12

    -Max  1000
    -Min  1
    -Unit  ms
    -Description  Lag time, after which motor restarts and runs in reverse direction

.. option:: O35

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Needle position after turn back
