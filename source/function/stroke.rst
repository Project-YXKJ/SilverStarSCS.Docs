Stroke adjustment
=================

Depending on the equipment, the machine has can be used to sew two different storke
heights, and it can be activated with a press of button.

Speed Limitation via adjusting wheel
------------------------------------

If a component is installed in the stroke adjustment wheel, the system will
automatically limit the speed when adjusting the wheel. There are two types of
components used for speed limiting:

Switch
    Gear speed limiter, if 2 switches are installed, it will have four gears.

Potentiometer
    The speed can be continuously adjusted, and there is no speed limit until a certain
    stroke height is reached. As the stroke height continues to increase, the maximum
    seam speed will linearly decrease.

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

Number of stitches 2nd stroke off
---------------------------------

if :option:`A32` is not 0, when switching to 2nd sewing foot stroke, after sewing N
stitches set by :option:`A32` , the second sewing foot stroke is automatically
deactivated.

Quick reference
---------------

This table summarizes which parameter should be used for stroke:

================================= ========== =============
Parameter                         Authority  See also
================================= ========== =============
Stroke                            Operator   :option:`A45`
Max. Speed Stroke Whell Mark 1    Technician :option:`S09`
Max. Speed for Small Stroke       Technician :option:`S10`
Max. Speed Stroke Whell Mark 2    Technician :option:`S11`
Max. Speed Stroke Whell Mark 3    Technician :option:`S12`
Max. Speed Stroke Whell Mark 4    Technician :option:`S13`
Max. Speed for High Stroke        Technician :option:`S14`
Max. Speed for Elevated Stroke    Technician :option:`S15`
Number of Stitches 2nd Stroke Off Technician :option:`A32`
Status of Stroke                  Developer  :option:`A24`
Auto Speed Limit                  Operator   :option:`A35`
Min. Stroke Border                Technician :option:`O21`
Max. Stroke Point                 Technician :option:`O22`
Time(t1)                          Developer  :option:`O76`
Duty cycle(t2)                    Developer  :option:`O77`
The Stroke Height Sensor Type     Developer  :option:`O85`
================================= ========== =============

Parameter List
--------------

.. option:: A45

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Stroke height function:
      | 0 = Off
      | 1 = On

.. option:: S09

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The stroke height knob type is switch: Limit speed when turn adjusting
                  wheel to mark 1 position.

.. option:: S10

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The stroke height knob type is potentiometer: Limit speed for the small
                  stork height.

.. option:: S11

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The stroke height knob type is switch: Limit speed when turun adjusting
                  wheel to mark 2 position.

.. option:: S12

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The stroke height knob type is switch:Limit speed when turun adjusting
                  wheel to mark 3 position.

.. option:: S13

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The stroke height knob type is switch: Limit speed when turun adjusting
                  wheel to mark 4 position.

.. option:: S14

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The stroke height knob type is potentiometer:Limit speed for the high
                  stork height.

.. option:: S15

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Limit speed for the elevated sewing foot storke.

.. option:: A24

    -Max  1
    -Min  0
    -Unit  --
    -Description  Status of stroke height solenoid(read only).

.. option:: A32

    -Max  99
    -Min  0
    -Unit  stitches
    -Description
      | 0 = Manually switch;
      | Not 0 = Number of stitches after which the second stroke height is automatically deactivated.

.. option:: A35

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | If the second stroke is activated, speed reduced down to Parameter S15:
      | 0 = Off
      | 1 = On

.. option:: O21

    -Max  4095
    -Min  0
    -Unit  --
    -Description  The sensor value at the boundary position of the minimum stroke,
                  the speed is reduced down as continue to increase stroke height.

.. option:: O22

    -Max  4095
    -Min  0
    -Unit  --
    -Description  Sensor value at position of maximum stroke.

.. option:: O76

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Stroke height: activation duration of in :term:`time period t1` (100% duty cycle).

.. option:: O77

    -Max  100
    -Min  1
    -Unit  %
    -Description  Stroke height: duty cycle[%] in :term:`time period t2`.

.. option:: O85

    -Max  2
    -Min  0
    -Unit  --
    -Description
       | 0 = Off;
       | 1 = Switch;
       | 2 = Potentiometer.
