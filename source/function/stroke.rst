Stroke adjustment
=================

Depending on the equipment, the machine has can be used to sew two different storke
heights, and it can be activated with a press of button.

Speed Limitation via adjusting wheel
------------------------------------

If additional components are installed within the stroke adjustment wheel, the system
will automatically limit speed when adjusting the wheel. Parameter :option:`O85` is used
to set the component type. If set to 0, no speed limit applies when adjusting stroke
using the wheel.

There are two types of components used for speed limiting:

Switch
    Set :option:`O85` to 1.

    Gear speed limiter, if two switches are installed, it will have four gears.

Potentiometer
    Set :option:`O85` to 2.

    The sew speed is continuously adjustable, The system maintains the full programmed
    speed until a certain stroke height is reached As the stroke height continues to
    increase, the maximum sewing speed will decrease linearly.

    .. important::

        Ensure that the larger the stroke level, the smaller the potentiometer sampling
        value.

    Set maximum speed using parameter :option:`S10`

    Set minimum speed using parameter :option:`S14`

    Set sample value of upper break point using parameter :option:`O21`, stroke level up
    to which full speed is to be maintained

    Set sample value of upper break point using parameter :option:`O22`, stroke level
    from which minimum speed is to be effective

    .. figure:: ../_static/common/speed_limit_potentiometer.excalidraw.svg
        :scale: 100 %
        :alt: speed_limit_potentiometer

        Correspondence between sampling value parameters and speed parameters

Speed Limitation during quick stroke adjustment
-----------------------------------------------

If parameter :option:`A35` set to 1, when 2nd sewing foot stroke is activated, the speed
is reduced down to the desired value of 2nd sewing foot stroke which set by
:option:`S15`.

Quick Stroke Auto-Reset Stitches
--------------------------------

if :option:`A32` is not 0, when switching to 2nd sewing foot stroke, after sewing N
stitches set by :option:`A32` , the second sewing foot stroke is automatically
deactivated.

Quick reference
---------------

This table summarizes which parameter should be used for stroke:

======================================== ========== =============
Parameter                                Authority  See also
======================================== ========== =============
Stroke                                   Operator   :option:`A45`
Stroke Limit Level 1                     Technician :option:`S09`
Linear Limit Start                       Technician :option:`S10`
Stroke Limit Level 2                     Technician :option:`S11`
Stroke Limit Level 3                     Technician :option:`S12`
Stroke Limit Level 1                     Technician :option:`S13`
Linear Limit End                         Technician :option:`S14`
Max. Stroke Speed Limit                  Technician :option:`S15`
Quick Stroke Auto-Reset Stitches         Technician :option:`A32`
Quick Stroke Adjustment Status           Developer  :option:`A24`
Quick stroke adjustment auto speed limit Operator   :option:`A35`
Sample value of upper speed break point  Technician :option:`O21`
Sample value of lower speed break point  Technician :option:`O22`
Full power duration                      Developer  :option:`O76`
Duty cycle after full power              Developer  :option:`O77`
The Stroke Height Sensor Type            Developer  :option:`O85`
======================================== ========== =============

Parameter List
--------------

.. option:: A45

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Sewing foot stroke:
      | 0 = Off;
      | 1 = On.

.. option:: S09

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Switch Type: Speed limit for stroke height level 1.

.. option:: S10

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Potentiometer Type: Limit speed at the start of linear reduction.

.. option:: S11

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Switch Type: Speed limit for stroke height level 2.

.. option:: S12

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Switch Type: Speed limit for stroke height level 3.

.. option:: S13

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Switch Type: Speed limit for stroke height level 4.

.. option:: S14

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Potentiometer Type: Limit speed at the end of linear reduction.

.. option:: S15

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Safety speed limit at the maximum stroke height.

.. option:: A24

    -Max  1
    -Min  0
    -Unit  --
    -Description  Activation status of the Quick Stroke Adjustment, read only.

.. option:: A32

    -Max  99
    -Min  0
    -Unit  stitches
    -Description
      | Number of stitches for automatic switch off the 2nd stroke:
      | 0 = Manual;
      | Not 0 = Number of stitches after which quick stroke adjustment is automatically deactivated.

.. option:: A35

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Limits maximum speed automatically during quick stroke adjustment:
      | 0 = Off;
      | 1 = On, if the second stroke is activated, speed reduced down to Parameter :option:`S15` .

.. option:: O21

    -Max  4095
    -Min  0
    -Unit  --
    -Description  Sample value of upper break point, stroke level up to which full speed is to be maintained.

.. option:: O22

    -Max  4095
    -Min  0
    -Unit  --
    -Description  Sample value of upper break point, stroke level from which minimum speed is to be effective.

.. option:: O76

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Stroke height: Activation duration in :term:`time period t1` (100% duty cycle).

.. option:: O77

    -Max  100
    -Min  1
    -Unit  %
    -Description  Stroke height: Duty cycle [%] in :term:`time period t2` .

.. option:: O85

    -Max  2
    -Min  0
    -Unit  --
    -Description
      | Type of stroke adjustment sensor:
      | 0 = No;
      | 1 = Switch;
      | 2 = Potentiometer.
