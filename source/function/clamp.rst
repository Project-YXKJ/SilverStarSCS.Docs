Thread clamp
============

**Functions:**

The timing of the electronic clamp's action is determined by parameter :option:`O29` and
is divided into three cases:

- At seam start

  Switch on at position set by :option:`D07`, switch off at position set by
  :option:`D08`.

  Action only during the first stitch, reset after thread trim.

- At turning back

  Switch on during turning back, the Max. permissible time is set by :option:`T15` to
  protect from damage.

- At sewing foot lifting

  Switch on during foot lifting, the Max. permissible time is set by :option:`T15` to
  protect from damage.

Quick reference
---------------

This table summarizes which parameter should be used for clamp:

=========================== ========== =============
Parameter                   Authority  See also
=========================== ========== =============
Thread Clamp                Operator   :option:`A10`
Thread Clamp Limit Time     Technician :option:`T15`
Thread Clamp option         Technician :option:`A29`
Switch-on angle             Technician :option:`D07`
Switch-off angle            Technician :option:`D08`
PrePressure duiring Clamp   Technician :option:`O42`
Duty cycle after full power Developer  :option:`O48`
=========================== ========== =============

Parameter List
--------------

.. option:: A10

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Thread clamp:
      | 0 = Off;
      | 1 = On.

.. option:: T15

    -Max  1000
    -Min  1
    -Unit  ms
    -Description  Switch-on duration for the thread clamp during foot lift or needle bar positioning.

.. option:: A29

    -Max  3
    -Min  0
    -Unit  --
    -Description
      | Thread clamp option:
      | 0 = At seam start only;
      | 1 = At seam start and during turn back;
      | 2 = At seam start and during sewing foot lift;
      | 3 = At seam start, during turn back and sewing foot lift.

.. option:: D07

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for thread clamp at seam start.

.. option:: D08

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-off angle for thread clamp at seam start.

.. option:: O42

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Reduce the sewing foot pressure during the clamping cycle:
      | 0 = Off;
      | 1 = On.

.. option:: O48

    -Max  100
    -Min  0
    -Unit  %
    -Description  Thread clamp: Duty cycle [%] in :term:`time period t2` .
