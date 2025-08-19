Puller
======

**Functions:**

Automatic raising puller is associated with three cases:

- Sew foot lift
- Start/End backtack
- Reverse

When the sewing foot is lifted, the puller is automatically rised, when the foot is
lowered, the puller is also lowered.

During the sewing the start/end backtack, the puller is automatically raised, once the
start/end backtaak is complete, the puller is also lowered.

When manual reverse button is pressed, the puller is automatically raised, once the
reverse is turned off, the puller is also lowered.

An input port can be configured to switch between raising and lowering the puller. When
the key is pressed to raise the puller, it will remain raised until the key is pressed
again to lower it.

Quick reference
---------------

This table summarizes which parameter should be used for puller:

============================== ========== =============
Parameter                      Authority  See also
============================== ========== =============
Puller                         Operator   :option:`A89`
Delay stitches after foot down Technician :option:`A64`
Status(Read Only)              Developer  :option:`A90`
Full power duration            Developer  :option:`O97`
Duty cycle after full power    Developer  :option:`O98`
============================== ========== =============

Parameter List
--------------

.. option:: A89

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Upper puller:
      | 0 = Off;
      | 1 = On.

.. option:: A64

    -Max  255
    -Min  0
    -Unit  stitch
    -Description
      | 0 = the foot lifter is lowered, the puller is lowered immediately;
      | Other = At seam start, number of stitches after which the puller will automatically rise; In the seam, puller rise/lower with sewing foot.

.. option:: A90

    -Max  1
    -Min  0
    -Unit  --
    -Description  Upper puller status, raised or lowered, read only.

.. option:: O97

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Puller lifter: full power duration, :term:`time period t1` .

.. option:: O98

    -Max  100
    -Min  1
    -Unit  %
    -Description  Puller lifter: duty cycle after full power in :term:`time period t2` .
