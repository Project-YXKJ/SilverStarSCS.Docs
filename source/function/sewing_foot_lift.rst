Sewing foot lift
================

**Sewing foot is lifted:**

- In the seam

  - By half heelback, :term:`POSITION -1`
  - Automatically with :option:`A14` setted to 1
  - Press the key that has been allocated for the purpose

- After thread trimming

  - By heelback, :term:`POSITION -1` or :term:`POSITION -2`
  - Automatically with :option:`A15` setted to 1
  - Press the key that has been allocated for the purpose

It is possible to prevent unintentional foot lifting before thread trimming when
changing from pedal :term:`POSITION 0` to :term:`POSITION -2` by setting a switch-on
delay using parameter :option:`T05`.

**Sewing foot is lowered:**

- Press pedal to :term:`POSITION 0`
- Press pedal to :term:`POSITION 1`
- Release the key that has been allocated for the purpose

Holding force of the raised foot
--------------------------------

The sewing foot is lifted by full power. Then the system switches automatically to
partial power in order to reduce the load for the control and the connected solenoid.

Set the duration of full power using parameter :option:`T07` and the partial holding
power using parameter :option:`O05`.

.. attention::

    If the holding power is set too high, the solenoid and the control may be
    permanently damaged. Please observe the permissible duty cycle (ED) of the solenoid,
    and set the appropriate value.

Scheduled Switch Off
--------------------

In order to reduce heat generation, timed release can be set.

if parameter :option:`O06` is set to 1, the maximum time the foot lifter can keep raised
is determined by parameter :option:`O07`.

Start delay
-----------

When the sewing foot is the raised, in order to ensure that the sewing material is
pressed tightly before the machine starts running, a tiem lag will be inserted after
step the pedal forwards, which is controlled by parameter :option:`T06`.

Quick reference
---------------

This table summarizes which parameter should be used for sewing foot:

============================================================== ========== =============
Parameter                                                      Authority  See also
============================================================== ========== =============
Sewing foot lift                                               Operator   :option:`A09`
Switch-on delay                                                Technician :option:`T05`
Start delay Time                                               Technician :option:`T06`
Switch-on delay for Auto Foot                                  Technician :option:`T10`
Foot lift at sewing stop                                       Technician :option:`A14`
Foot lift after trim                                           Technician :option:`A15`
Scheduled switch off                                           Technician :option:`O06`
Upper limit Switch-on period                                   Technician :option:`O07`
Soft Foot Falling                                              Technician :option:`O39`
Full power duration                                            Developer  :option:`T07`
Duty cycle after full power                                    Developer  :option:`O05`
Effect of Soft Foot Falling                                    Technician :option:`O40`
Effect of PrePressure duiring Clamping(Without Start Backtack) Technician :option:`O53`
Effect of PrePressure duiring Clamping(Soft Start)             Technician :option:`O54`
Effect of PrePressure duiring Clamping                         Technician :option:`O55`
============================================================== ========== =============

Parameter List
--------------

.. option:: A09

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Sewing Foot lift:
      | 0 = Off;
      | 1 = On.

.. option:: T05

    -Max  500
    -Min  1
    -Unit  ms
    -Description  Switch-on delay with pedal in position –1 (half heelback), to avoid unexpected foot lifting when step backwards for trim.

.. option:: T06

    -Max  500
    -Min  1
    -Unit  ms
    -Description  Start delay after switching off the sewing foot lift signal, make sure the foot has pressed the material, after which, sewing can start.

.. option:: T10

    -Max  500
    -Min  1
    -Unit  ms
    -Description  When the automatic foot function is turned on, the delay time for switch on the foot.

.. option:: A14

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Automatic lifting sewing foot when stop in the middle of seam:
      | 0 = Off;
      | 1 = On.

.. option:: A15

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Automatic lifting sewing foot after trim or at seam end:
      | 0 = Off;
      | 1 = On.

.. option:: O06

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Sewing Foot scheduled switch off:
      | 0 = Off;
      | 1 = On.

.. option:: O07

    -Max  30
    -Min  5
    -Unit  s
    -Description  Set the foot hold time for the scheduled switch off.

.. option:: O39

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Decrease the falling speed of the foot by PWM control:
      | 0 = Off;
      | 1 = On.

.. option:: T07

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Sewing foot lifter: full power duration, :term:`time period t1` .

.. option:: O05

    -Max  100
    -Min  1
    -Unit  %
    -Description  Sewing foot lifter: duty cycle after full power in :term:`time period t2` .

.. option:: O40

    -Max  9
    -Min  1
    -Unit  --
    -Description  The larger value, the slower foot falls.

.. option:: O53

    -Max  10
    -Min  1
    -Unit  --
    -Description  Duty cycle of foot during clamping without start backtack.

.. option:: O54

    -Max  10
    -Min  1
    -Unit  --
    -Description  Duty cycle of foot during clamping with soft start.

.. option:: O55

    -Max  10
    -Min  1
    -Unit  --
    -Description  Duty cycle of foot during clamping.
