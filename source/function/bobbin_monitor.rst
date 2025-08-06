.. _bobbin_monitor:

Bobbin stitch counter/monitor
=============================

Using Lower thread counter allows users to know the remaining thread amount.

Quick start
-----------

Following steps:

1. Set an appropriate value for :option:`O19`, every time N stitches are sewn which set
   by this parameter, the counter value :option:`O44` increases by 1.
2. Set an appropriate value for :option:`O43`, this is a very variable value, which
   depends on the size of the bobbin and the thickness of the thread.
3. Choose when to throw a warning by setting :option:`O20`, immediately or after thread
   cutting.
4. Set :option:`A12` to 1, enable the counter.
5. Refer to the beginning of this chapter `Bobbin Remaining Amount`_, as the sewing, the
   remaining amount is counted down, when it reaches 0, the machine will stop, and the
   controller will throw a warning. A reset is needed if you want continue.

How it works?
~~~~~~~~~~~~~

Here is a formula:

.. math::
    :name: Bobbin Remaining Amount

    N_{\text{Remaining thread amount}}
    = O43_{\text{reset value of the bobbin thread counter}} - O44_{\text{bobbin thread counter value}}

Quick reference
---------------

This table summarizes which parameter should be used for bobbin counter:

================================== ========== =============
Parameter                          Authority  See also
================================== ========== =============
Bobbin Stitch Counter              Operator   :option:`A12`
Bobbin Stitch Counter Reset Value  Technician :option:`O43`
Bobbin Counter Factor              Technician :option:`O19`
Timming of Warning(Bobbin Counter) Technician :option:`O20`
Bobbin Stitch Counter Value        Technician :option:`O44`
================================== ========== =============

Parameter List
--------------

.. option:: A12

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Activate the Bobbin stitch counter:
      | 0 = Off;
      | 1 = On.

.. option:: O43

    -Max  9999
    -Min  1
    -Unit  --
    -Description  Bobbin supply capacity. This is a very variable value, which depends
                  on the size of the bobbin and the thickness of the thread.

.. option:: O19

    -Max  200
    -Min  1
    -Unit  stitches
    -Description  Every sew over this number of stitches, increment the counter by 1.

.. option:: O20

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | When to throw a warning if bobbin counter reaches 0:
      | 0 = after thread cutting;
      | 1 = immediately.

.. option:: O44

    -Max  9999
    -Min  0
    -Unit  --
    -Description  The current value of bobbin stitch counter, the reset value minus
                  this value is remaining value.
