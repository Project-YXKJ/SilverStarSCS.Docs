Seam center guide
=================

Automation rules
----------------

Automatic lifting seam center guide is associated with three situations:

- Sew Foot
- Bartack(start or end tack) and reverse
- Stroke

**Function:**

If the second sewing foot stroke is switched on, the seam center guide is automatically
raise up, when the stroke has returned to the normal position, the seam center guide has
also returned to normal settings.

During the sewing of the backtack/reverse, the seam center guide is automatically raised
up, when the backtack/reverse completes, the seam center guide has also returned to
normal settings.

If the second sewing foot stroke is switched on, the seam center guide is automatically
raised up, when the stroke has returned to the normal position, the seam center guide
has also returned to normal settings.

The mode is set by parameter :option:`A51`, you can use the following table to quickly
check the parameter values ​​you need to set:

===== ==== =============== ======
Value Foot Bartack/reverse Stroke
===== ==== =============== ======
0     Off  Off             Off
1     On   Off             Off
2     Off  On              Off
3     On   On              Off
4     Off  Off             On
5     On   Off             On
6     Off  On              On
7     On   On              On
===== ==== =============== ======

Quick reference
---------------

This table summarizes which parameter should be used for wiper:

=============================== ========== =============
Parameter                       Authority  See also
=============================== ========== =============
Seam Center Guide               Operator   :option:`A47`
Auto Mode for Seam Center Guide Technician :option:`A51`
Status of Seam Center Guide     Developer  :option:`A33`
Time(t1)                        Developer  :option:`O89`
Duty cycle(t2)                  Developer  :option:`O90`
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
    -Description  Status of the seam center guide solenoid(read only)

.. option:: O89

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Seam Center Guide: activation duration of in :term:`time period t1`
                  (100% duty cycle).

.. option:: O90

    -Max  100
    -Min  1
    -Unit  %
    -Description  Seam Center Guide: duty cycle[%] in :term:`time period t2`.
