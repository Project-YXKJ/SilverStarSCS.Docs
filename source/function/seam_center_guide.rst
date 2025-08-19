Seam center guide
=================

**Functions:**

Automatic lifting seam center guide is associated with three cases:

- Sew Foot
- Start/End backtack and reverse
- Stroke

When the sewing foot is lifted, the seam center guide is automatically rised; when the
foot is lowered, the seam center guide is also lowered.

During the sewing the start/end backtack and reverse, the seam center guide is
automatically raised, once the start/end backtack is complete, or the reverse is turned
off, the seam center guide is also lowered.

When the second stroke height is activated, the seam center is automatically rised, when
the stroke returns to its normal position, the seam center guide also lowers
accordingly.

The mode is set by parameter :option:`A51`, you can use the following table to quickly
check the parameter values ​​you need to set:

===== ==== ================ ======
Value Foot Backtack/reverse Stroke
===== ==== ================ ======
0     Off  Off              Off
1     On   Off              Off
2     Off  On               Off
3     On   On               Off
4     Off  Off              On
5     On   Off              On
6     Off  On               On
7     On   On               On
===== ==== ================ ======

Quick reference
---------------

This table summarizes which parameter should be used for wiper:

=============================== ========== =============
Parameter                       Authority  See also
=============================== ========== =============
Seam Center Guide               Operator   :option:`A47`
Auto Mode for Seam Center Guide Technician :option:`A51`
Status(Read Only)               Developer  :option:`A33`
Full power duration             Developer  :option:`O89`
Duty cycle after full power     Developer  :option:`O90`
=============================== ========== =============

Parameter List
--------------

.. option:: A47

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Seam center guide function:
      | 0 = Off;
      | 1 = On.

.. option:: A51

    -Max  7
    -Min  0
    -Unit  --
    -Description
      | Auto mode for seam center guide:
      | 0 = Manual;
      | 1 = Automatically raise when foot lifting;
      | 2 = Automatically raise when backtack/reverse;
      | 3 = Both 1&2;
      | 4 = Automatically raise when 2nd stroke;
      | 5 = Both 1&4;
      | 6 = Both 2&4;
      | 7 = Both 1&2&4.

.. option:: A33

    -Max  1
    -Min  0
    -Unit  --
    -Description  Status of the seam center guide solenoid, read only.

.. option:: O89

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Seam Center Guide: full power duration, :term:`time period t1` .

.. option:: O90

    -Max  100
    -Min  1
    -Unit  %
    -Description  Seam Center Guide: duty cycle after full power in :term:`time period t2` .
