.. _bartack:

Bartack
=======

Stitch in stitch
----------------

.. important::

    Before adjustment, make sure that forward stitch length is the same with backward
    stitch length use the reverse lever.

The time it takes for reverse actuator actions, adjust parameter :option:`T01` as the
guide of following figure:

.. figure:: ../_static/common/add-T01.svg
    :scale: 150 %
    :alt: Increase T01

    Increase T01

.. figure:: ../_static/common/sub-T01.svg
    :scale: 150 %
    :alt: Decrease T01

    Decrease T01

The time it takes for reverse actuator releases, adjust parameter :option:`T02` as the
guide of following figure:

.. figure:: ../_static/common/add-T02.svg
    :scale: 150 %
    :alt: Increase T02

    Increase T02

.. figure:: ../_static/common/sub-T02.svg
    :scale: 150 %
    :alt: Decrease T02

    Decrease T02

SD Mode
-------

SD mode is a special mode of start/end bartack, used to ensure the seam looks better.

When the SD mode is enabled, the motor will pause at the collagen turning point and wait
for the time set by :option:`T11` to ensure that the reverse action in place, then the
motor continue running.

SD mode can be activated for start bartack or end bartack respectively, controlled by
:option:`A20` and :option:`A22`.

Quick reference
---------------

This table summarizes which parameter should be used for bartack:

============================================== ========== =============
Parameter                                      Authority  See also
============================================== ========== =============
Speed in Start Bartack                         Operator   :option:`S03`
Speed in End Bartack                           Operator   :option:`S04`
SD mode for Start Bartack                      Operator   :option:`A20`
SD mode for End Bartack                        Operator   :option:`A22`
Reverse Action In Place Time                   Technician :option:`T01`
Reverse Release In Place Time                  Technician :option:`T02`
SD Mode Stop Time                              Technician :option:`T11`
Maintain Speed after Start Bartack             Technician :option:`A34`
Start Reverse Position                         Technician :option:`D05`
Stop Reverse Position                          Technician :option:`D06`
Auto Power-off Reverse                         Technician :option:`O10`
Reverse Max. Holding Time                      Technician :option:`O11`
Max. Speed of 1 stitch                         Technician :option:`O12`
Max. Speed of 2 stitch                         Technician :option:`O13`
Max. Speed of 3 stitch                         Technician :option:`O14`
Stitches of Maintain Speed after Start Bartack Technician :option:`O41`
Time(t1)                                       Developer  :option:`T08`
Duty cycle(t2)                                 Developer  :option:`O09`
============================================== ========== =============

Parameter List
--------------

.. option:: S03

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum speed in bartack at seam begin.

.. option:: S04

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum speed in bartack at seam end.

.. option:: A20

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Stop at direction change of start tacking in order to the bartack magnet reach the specified position:
      | 0 = Off;
      | 1 = On.

.. option:: A22

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Stop at direction change of end tacking in order to the bartack magnet reach the specified position:
      | 0 = Off;
      | 1 = On.

.. option:: T01

    -Max  200
    -Min  1
    -Unit  ms
    -Description  The time for the reverse solenoid finish the action,unit ms

.. option:: T02

    -Max  200
    -Min  1
    -Unit  ms
    -Description  The time for reverse solenoid finish the releasing,unit ms

.. option:: T11

    -Max  1000
    -Min  1
    -Unit  ms
    -Description  Motor standby duration at direction change of bartack if SD mode is On.

.. option:: A34

    -Max  1
    -Min  0
    -Unit  --
    -Description  Reverse power on angle
      | For better performance of start bartack:
      | 0 = Off;
      | 1 = On.

.. option:: D05

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of reverse is activated.

.. option:: D06

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Position when the magnet of reverse is deactivated.

.. option:: O10

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether the magnet of reverse automatic power-off after the set time:
      | 0 = Off;
      | 1 = On

.. option:: O11

    -Max  30
    -Min  5
    -Unit  s
    -Description  If Auto Power-off Reverse is turned on, this parameter sets the power-off time.

.. option:: O12

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum Speed of 1 stitch when bartack or W-sewing.

.. option:: O13

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum Speed of 2 stitch when bartack or W-sewing.

.. option:: O14

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum Speed of 3 stitch when bartack or W-sewing.

.. option:: O41

    -Max  10
    -Min  0
    -Unit  stitches
    -Description  Number of A-stitches which speed holding after sewing start bartck.

.. option:: T08

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Reverse:activation duration of in :term:`time period t1` (100% duty cycle),unit ms

.. option:: O09

    -Max  100
    -Min  1
    -Unit  %
    -Description  Reverse:duty cycle[%] in :term:`time period t2`.
