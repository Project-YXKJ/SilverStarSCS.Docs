Thread tension
==============

Solenoid valve or electromagnet?
--------------------------------

If tension is controlled by electromagnet not solenoid valve, you need to be careful
when setting tha value of :option:`O75`. Over premissible power on time, the
electromagnet may burn out, thus a electromagnet with a small value of :option:`O75` is
protected form damage.

In parallel with trimmer
------------------------

Thread tension procedure:

The thread tension power on when position is reached with :option:`D13` and power off
when position is reached with :option:`D14` during thread trimming.

Modes when sewing foot is lifted
--------------------------------

When the foot is lifted, there are two cases: during sewing and after thread trimming,
there are 4 options for the automatic mode of thread tension, the mode is set by
parameter :option:`A27`:

- 0 = tension is not lifted;
- 1 = tension is lifted as the foot is lifted during sewing;
- 2 = tension is lifted as the foot is lifted after thread trim;
- 3 = tension is lifted as the foot is lifted during sewing and after trim.

Automation rules for additional thread tension
----------------------------------------------

Automatic activate additional thread tension is associated with three cases:

- Stroke
- Backtack at seam begin
- Backtack at seam end

**Function:**

If the second sewing foot stroke is switched on, the additional thread tension is
automatically activated, when the stroke has returned to the normal position, the
additional thread tension has also returned to normal settings.

During backtack at seam begin, the additional thread tension is automatically activated,
when the backtack completes, the additional thread tension has also returned to normal
settings.

During backtack at seam end, the additional thread tension is automatically activated,
when the backtack completes, the additional thread tension has also returned to normal
settings.

The mode is set by parameter :option:`A28`, you can use the following table to quickly
check the parameter values ​​you need to set:

===== ====== ====================== ====================
Value Stroke Backtack at seam begin Backtack at seam end
===== ====== ====================== ====================
0     Off    Off                    Off
1     On     Off                    Off
2     Off    On                     Off
3     On     On                     Off
4     Off    Off                    On
5     On     Off                    On
6     Off    On                     On
7     On     On                     On
===== ====== ====================== ====================

Quick reference
---------------

This table summarizes which parameter should be used for tension:

==================================================== ========== =============
Parameter                                            Authority  See also
==================================================== ========== =============
Status of Additional Thread Tension(Read Only)       Developer  :option:`A26`
Auto mode for tension at foot lifting                Technician :option:`A27`
Auto Additional Thread Tension                       Technician :option:`A28`
Switch-on angle                                      Technician :option:`D13`
Switch-off angle                                     Technician :option:`D14`
Full power duration(Main thread tension)             Developer  :option:`O49`
Duty cycle after full power(Main thread tension)     Developer  :option:`O50`
Upper limit Switch-on period                         Developer  :option:`O75`
Full power duration(Addition thread tension)         Developer  :option:`O86`
Duty cycle after full power(Addition thread tension) Developer  :option:`O87`
Addition tension solenoid work mode                  Developer  :option:`O88`
==================================================== ========== =============

Parameter List
--------------

.. option:: A26

    -Max  1
    -Min  0
    -Unit  --
    -Description  Status of the additional tension solenoid, read only.

.. option:: A27

    -Max  3
    -Min  0
    -Unit  --
    -Description
      | Mode for lifting the tension during active sewing foot lift:
      | 0 = tension is not lifted;
      | 1 = tension is lifted as the foot is lifted during sewing;
      | 2 = tension is lifted after trim;
      | 3 = tension is lifted as the foot is lifted during sewing and after trim.

.. option:: A28

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Auto mode for additional thread tension:
      | 0 = Off;
      | 1 = Automatically activated when the second sewing foot stroke is switched on;
      | 2 = Automatically activated during backtack at seam begin;
      | 3 = 1 & 2;
      | 4 = Automatically activated during backtack at seam end;
      | 5 = 1 & 4;
      | 6 = 2 & 4;
      | 7 = 1 & 2 & 4.

.. option:: D13

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for thread tension during trimming.

.. option:: D14

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-off angle for thread tension during trimming.

.. option:: O49

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Main thread tension: full power duration, :term:`time period t1` .

.. option:: O50

    -Max  100
    -Min  1
    -Unit  %
    -Description  Main thread tension: duty cycle after full power in :term:`time period t2` .

.. option:: O75

    -Max  9999
    -Min  0
    -Unit  ms
    -Description
      | 0 = Always Lifting;
      | Not 0 = This parameter sets the power-off time.

.. option:: O86

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Additional thread tension: full power duration, :term:`time period t1` .

.. option:: O87

    -Max  100
    -Min  1
    -Unit  %
    -Description  Additional thread tension: duty cycle after full power in :term:`time period t2` .

.. option:: O88

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 0 = When additional thread tension is switch on, the tension device is lifted;
      | 1 = When additional thread tension is switch off, the tension device is lifted;
