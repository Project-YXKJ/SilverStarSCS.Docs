Thread trimmer
==============

Thread trimming procedure
    Thread trimmer singnal is switched on when the angle value :option:`D03` has been
    reached, the switched off when the angle value :option:`D04` . If the position is
    not reached because of a mechanical error, the thread trimmer signal is switched off
    after 500ms for protect the magnet from damage.

    Thread trimming in the lockstitch modes is performed at trimming speed.

Activation of Short Trimmer
---------------------------

With sewing machines equipped with a short trimmer system, the required functional
sequence can be activated using parameter :option:`A42`. The thread trimming function
must be On.

Quick reference
---------------

This table summarizes which parameter should be used for thread trimmer:

======================================================== ========== =============
Parameter                                                Authority  See also
======================================================== ========== =============
Thread trimmer                                           Operator   :option:`A06`
Thread trimming speed                                    Technician :option:`S07`
Short Trimmer                                            Technician :option:`A42`
Short Trimmer Stitches                                   Technician :option:`A67`
Switch-on angle for Thread trimmer                       Technician :option:`D03`
Switch-off angle for Thread trimmer                      Technician :option:`D04`
Switch-on angle for Movable Knife of Short Trimmer       Technician :option:`D17`
Switch-off angle for Movable Knife of Short Trimmer      Technician :option:`D18`
Switch-on angle for Reverse of Short Trimmer             Technician :option:`D19`
Switch-off angle for Reverse of Short Trimmer            Technician :option:`D20`
Switch-on angle for Zero stitch length of Short Trimmer  Technician :option:`D21`
Switch-off angle for Zero stitch length of Short Trimmer Technician :option:`D22`
Pedal Reset After Trim                                   Technician :option:`O38`
Full power duration                                      Developer  :option:`O95`
Duty cycle after full power                              Developer  :option:`O96`
======================================================== ========== =============

Parameter List
--------------

.. option:: A06

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Thread trimmer:
      | 0 = Off;
      | 1 = On.

.. option:: S07

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  Thread trimming speed.

.. option:: A42

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Short Trimmer, feature for specific models:
      | 0 = Off;
      | 1 = On.

.. option:: A67

    -Max  10
    -Min  0
    -Unit  stitches
    -Description  When short thread trimmer is On, number of short length stitches before trim.

.. option:: D03

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for thread trimmer.

.. option:: D04

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-off angle for thread trimmer.

.. option:: D17

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for movable knife of short trimmer.

.. option:: D18

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-off angle for movable knife of short trimmer.

.. option:: D19

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for the reverse of short trimmer.

.. option:: D20

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for the reverse of short trimmer.

.. option:: D21

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-on angle for the zero stitch length of short trimmer.

.. option:: D22

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Switch-off angle for the zero stitch length of short trimmer.

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
    -Description  Zero stitch length of short trimmer: full power duration, :term:`time period t1` .

.. option:: O96

    -Max  100
    -Min  1
    -Unit  %
    -Description  Zero stitch length of short trimmer: duty cycle after full power in :term:`time period t2` .
