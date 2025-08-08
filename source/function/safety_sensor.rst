Safety Sensor
=============

Tilt safaty switch
------------------

Quick reference
~~~~~~~~~~~~~~~

This table summarizes which parameter should be used for tilt safaty switch:

================================ ========== =============
Parameter                        Authority  See also
================================ ========== =============
Debouncing of Tilt safaty Switch Technician :option:`T09`
Warning: Tilt safety switch      Technician :option:`O31`
Sensor Polarity(Tilt Safety)     Technician :option:`O32`
================================ ========== =============

Eye protection
--------------

Quick reference
~~~~~~~~~~~~~~~

This table summarizes which parameter should be used for eye protection:

======================= ========== =============
Parameter               Authority  See also
======================= ========== =============
Warning: Eye protection Technician :option:`O28`
======================= ========== =============

Slide monitoring
----------------

Quick reference
~~~~~~~~~~~~~~~

This table summarizes which parameter should be used for slide monitoring:

========================= ========== =============
Parameter                 Authority  See also
========================= ========== =============
Warning: Slide monitoring Technician :option:`O29`
========================= ========== =============

Oil Level
---------

Quick reference
~~~~~~~~~~~~~~~

This table summarizes which parameter should be used for oil level:

====================== ========== =============
Parameter              Authority  See also
====================== ========== =============
Information: Oil Level Technician :option:`O34`
Oil Level Sample       Technician :option:`O68`
====================== ========== =============

Upper Thread Breaking
---------------------

Quick reference
~~~~~~~~~~~~~~~

This table summarizes which parameter should be used for upper thread breaking:

====================================== ========== =============
Parameter                              Authority  See also
====================================== ========== =============
Warning: Upper Thread Break            Technician :option:`A53`
Debouncing of Upper Thread Break       Technician :option:`T13`
Sensor Polarity(Upper Thread Breaking) Technician :option:`O92`
====================================== ========== =============

Parameter List
--------------

.. option:: T09

    -Max  1000
    -Min  1
    -Unit  ms
    -Description  The time is less and the sensitivity is higher, a perfect debounce
                  time can prevent false alarm.

.. option:: O31

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether to throw a warning when the machine is tilted:
      | 0 = Off;
      | 1 = On.

.. option:: O32

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Sensor polarity used for detect whether the machine has tilted:
      | 0 = Normal close;
      | 1 = Normal open.

.. option:: O28

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Optional features,whether to throw a warning when the eye protection isn't in the right place:
      | 0 = Off;
      | 1 = On.

.. option:: O29

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Optional features,whether to throw a warning when the hook cover plate is removed:
      | 0 = Off;
      | 1 = On.

.. option:: O34

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Optional features, whether to throw a information when the lubricating oil level is too low:
      | 0 = Off;
      | 1 = On.

.. option:: O68

    -Max  4095
    -Min  0
    -Unit  --
    -Description  If lubricating oil level sensor signal is analog, and the actual sampling value
                  is lower than this parameter value, a low oil level exception will be thrown.

.. option:: A53

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Optional features, whether to throw a warning when the upper thread breaking:
      | 0 = Off;
      | 1 = On.

.. option:: T13

    -Max  1000
    -Min  1
    -Unit  ms
    -Description  The time is less and the sensitivity is higher, a perfect debounce
      time can prevent false alarm.

.. option:: O92

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Sensor polarity used for upper thread breaking:
      | 0 = Normal open;
      | 1 = Normal closed.
