Input configuration
===================

Input ports allow you to connect devices that send data to controller. These devices
include buttons, optoelectronics, potentiometers, proximity sensor, and more. There are
two main categories of input ports: analog and digital.

- Digital Ports: For binary signals (on/off).
- Analog Ports: For continuous variable signals (e.g., potentiometer stroke).

**All input ports are flexible.** You can assign the desired functions to any available
port using a unified function code table. However, the allocation is subject to hardware
compatibility: the physical properties of the port must match the required function
type.

.. attention::

    Ensure that no two input ports are assigned to the same function. Redundant
    configurations may lead to logic conflicts.

    Function assignment is restricted by hardware capability. For instance, an analog
    input function cannot be assigned to a digital input port, despite sharing the same
    function code list.

Keypad
------

A :term:`Keypad` is a special input device, although each button on the Keypad can be
configured to perform a specific operation, they are different from traditional input
ports. It is neither analog nor digital. Usually, it can only be configured as those
"Switch" functions, and the sensor function cannot be connected to the Keypad.

.. _input_mode_code_list:

Input Mode Code List
--------------------

The following table lists the available function codes for input port configuration.

- 0 = No function;
- 1 = Manual reverse;
- 2 = Forward correction;
- 3 = Backward correction;
- 4 = Forward correction at stop, reverse at running;
- 5 = Backward correction at stop, reverse at running;
- 6 = Quick toggle stroke;
- 7 = Toggle start/end backtack on or off temporarily;
- 8 = Second stitch length;
- 9 = Additional thread tension;
- 10 = Pause [1]_ ;
- 11 = Thread a needle [2]_ ;
- 12 = Toggle seam center guide raised or lowered;
- 13 = Tilt switch;
- 14 = Up thread broken sensor;
- 15 = Eye protection sensor;
- 16 = Slide monitoring sensor;
- 17 = Toggle sewing foot lifter raised or lowered [3]_ ;
- 18 = lifting sewing foot via the knee switch;
- 19 = Lubricating oil level sensor(Digital type);
- 20 = Toggle puller raised or lowered;
- 21 = Reset bobbin counter;
- 22 = Simulate electronic handwheel rotation(forwards);
- 23 = Simulate electronic handwheel rotation(backwards);
- 24 = Toggle sewing direction [4]_ ;
- 25 = Toggle the clamp function on and off;
- 26 = Block Quick Keys;
- 27 = Remaining thread monitor sensor(Digital type);
- 100 = Sewing foot stroke knob potentiometer;
- 101 = Sewing foot height sensor
- 102 = Orthogonal encoder CHA for electronic handwheel;
- 103 = Orthogonal encoder CHB for electronic handwheel;
- 104 = Lubricating oil level sensor(Analog type);

.. [1] Pause mode, the machine can not run by step the pedal.

.. [2] Threading mode, the machine can not run by step the pedal, and the tension is
    activated.

.. [3] The function of code 17 is when you press the button, the sewing feet are lifted,
    at this time, you release the button, sewing feet are still lifted, then press the
    button again, sewing feet are lowered onto the sewing materrial; The function of
    code 18 is when you press the button, the sewing feet are lifted, at this time, you
    release the button, sewing feet are immediately lowered onto the sewing materrial.

.. [4] The function of code 1 is when you press the button, the machine sews backwards,
    at this time, you release the button, it sews forwards; The function of code 24 is
    when you press the button, the machine sews backwards, at this time, you release the
    button, it still sews backwards, the press the button again, it sews forwards.

.. important::

    Functions with codes greater than 100 needs special input ports, such as analog.

How to setup the function of input ports?
-----------------------------------------

Follow the steps:

1. Confirm which port you need to modify, such as *Input-01* or *Input-02*. In this
   step, you need to know the specific model of the system you are using, then refer to
   its wiring diagram. Refer to the :ref:`input_params_quick_reference` section of this
   chapter to find the parameter number that controls the function of this port;
2. Refer to the section at the beginning of this chapter :ref:`input_mode_code_list`,
   get the parameter value you need;
3. Modify the parameter obtained in step 1 to the function code obtained in step 2;
4. Restart the machine to adopt the settings.

Let's take an example:

1. You want use *Keypad-06* to control the puller;
2. In parameter list, you find :option:`A41`, which controls the mode of *Keypad-06* :

       A41 = Mode Keypad-06

3. See the section :ref:`input_mode_code_list`, *20* is code of puller function, then
   change :option:`A41` to 20:

       20 = Toggle puller raise up/down

4. Restart the machine.

.. _input_params_quick_reference:

Quick reference
---------------

This table summarizes which parameter should be used for input configuration:

============== ========== =============
Parameter      Authority  See also
============== ========== =============
Mode Keypad-01 Technician :option:`A36`
Mode Keypad-02 Technician :option:`A37`
Mode Keypad-03 Technician :option:`A38`
Mode Keypad-04 Technician :option:`A39`
Mode Keypad-05 Technician :option:`A40`
Mode Keypad-06 Technician :option:`A41`
Mode Keypad-07 Technician :option:`A68`
Mode Input-01  Technician :option:`A04`
Mode Input-02  Technician :option:`A05`
Mode Input-03  Technician :option:`A81`
Mode Input-04  Technician :option:`A82`
Mode Input-05  Technician :option:`A83`
Mode Input-06  Technician :option:`A84`
Mode Input-07  Technician :option:`A85`
Mode Input-08  Technician :option:`A86`
Mode Input-09  Technician :option:`A87`
Mode Input-10  Technician :option:`A88`
============== ========== =============

Parameter List
--------------

.. option:: A36

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-01.

.. option:: A37

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-02.

.. option:: A38

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-03.

.. option:: A39

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-04.

.. option:: A40

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-05.

.. option:: A41

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-06.

.. option:: A68

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Keypad-07.

.. option:: A04

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-01.

.. option:: A05

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-02.

.. option:: A81

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-03.

.. option:: A82

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-04.

.. option:: A83

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-05.

.. option:: A84

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-06.

.. option:: A85

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-07.

.. option:: A86

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-08.

.. option:: A87

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-09.

.. option:: A88

    -Max  199
    -Min  0
    -Unit  --
    -Description  Functional assignment for Input-10.
