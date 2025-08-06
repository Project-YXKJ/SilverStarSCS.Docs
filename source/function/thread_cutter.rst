.. _thread_cutter:

Thread cutter
=============

How it works?
-------------

Thread cutting procedure:

Thread cutting singnal is switched on when the angle value :option:`D03` has been
reached, the switched off when the angle value :option:`D04` . If the position is not
reached because of a mechanical error, the thread cutter signal is switched off after
500ms for protect the magnet from damage.

Quick reference
---------------

This table summarizes which parameter should be used for thread cutter:

====================================== ========== =============
Parameter                              Authority  See also
====================================== ========== =============
Thread Trim                            Operator   :option:`A06`
Trimming Speed                         Technician :option:`S07`
Short Thread Cutter                    Technician :option:`A42`
Short Thread Cutter Stitches           Technician :option:`A67`
Start trim position                    Technician :option:`D03`
Stop trim position                     Technician :option:`D04`
Start Movable Knife Position(STC)      Technician :option:`D17`
Stop Movable Knife Position(STC)       Technician :option:`D18`
Start Reverse Position(STC)            Technician :option:`D19`
Stop Reverse Position(STC)             Technician :option:`D20`
Start Zero Stitch Length Position(STC) Technician :option:`D21`
Stop Zero Stitch Length Position(STC)  Technician :option:`D22`
Pedal Reset After Trim                 Technician :option:`O38`
Time(t1)                               Developer  :option:`O95`
Duty cycle(t2)                         Developer  :option:`O96`
====================================== ========== =============

Parameter List
--------------

.. option:: A06

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Thread trim:
      | 0 = Off;
      | 1 = On.

.. option:: S07

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  Speed of the machine during trimming.

.. option:: A42

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Feature for specific models:
      | 0 = Off;
      | 1 = On.

.. option:: A67

    -Max  10
    -Min  0
    -Unit  stitches
    -Description  When short thread cutter active,number of short length stitches before trim.

.. option:: D03

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of thread cutter is activated.

.. option:: D04

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of thread cutter is deactivated.

.. option:: D17

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of movable knife(short thread cutter) is activated.

.. option:: D18

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of movable knife(short thread cutter) is deactivated.

.. option:: D19

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of the reverse(short thread cutter) is activated.

.. option:: D20

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of the reverse(short thread cutter) is deactivated.

.. option:: D21

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of zero stitch length(short thread cutter) is activated.

.. option:: D22

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of zero stitch length(short thread cutter) is deactivated.

.. option:: O38

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether the pedal need to return Position 0 before restart a new seam after trim:
      | 0 = Off;
      | 1 = On.

.. option:: O95

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Short thread zero length: activation duration of in :term:`time period t1` (100% duty cycle).

.. option:: O96

    -Max  100
    -Min  1
    -Unit  %
    -Description  Short thread zero length: duty cycle[%] in :term:`time period t2`.
