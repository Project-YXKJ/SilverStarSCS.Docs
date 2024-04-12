.. _input_configuration:

===================
Input configuration
===================

Input ports allow you to connect devices that send data to controller.
These devices include buttons, optoelectronics, potentiometers, proximity sensor, 
and more. There are two main categories of input ports: analog and digital.

Each input port is flexible. In most cases, you can freely configure 
the mode of each port according to your actual wiring.

.. attention::
   Make sure that two input ports are not configured for the same mode.
   
   Depending on the model, some mode may not be available.

.. _input_mode_code_list:

Input Mode Code List
=====================

Here is the input mode code list:

- 0 = No function;
- 1 = Manual bartack;
- 2 = Forward correction;
- 3 = Backward correction;
- 4 = Forward correction at stop, reverse at running;
- 5 = Backward correction at stop, reverse at running;
- 6 = Quick toggle stroke;
- 7 = Enable/unable bartack at seam start/end;
- 8 = Second stitch length;
- 9 = Additional thread tension;
- 10 = Pause [#]_;
- 11 = Thread a needle [#]_;
- 12 = Toggle seam center guide raise up/down;
- 13 = Tilt switch;
- 14 = Up thread broken sensor;
- 15 = Eye protection sensor;
- 16 = Hook cover missing sensor;
- 17 = Toggle sewing foot lifter raise up/down [#]_;
- 18 = lifting sewing foot via the knee switch;
- 19 = Oil Starvation;
- 20 = Toggle puller raise up/down;
- 21 = Reset bobbin counter;
- 22 = Simulate electronic handwheel rotation(forwards);
- 23 = Simulate electronic handwheel rotation(backwards);
- 24 = Toggle sewing direction [#]_;
- 100 = Sewing foot stroke knob potentiometer;
- 101 = Sewing foot height sensor
- 102 = Orthogonal encoder CHA for electronic handwheel;
- 103 = Orthogonal encoder CHB for electronic handwheel.
  
.. [#] Pause mode, the machine can not run by step the pedal.

.. [#] Threading mode, the machine can not run by step the pedal, and the tension
       is activated.

.. [#] The function of code 17 is when you press the button, the sewing feet are lifted,
       at this time, you release the button, sewing feet are still lifted, then press the button again,
       sewing feet are lowered onto the sewing materrial;
       
       The function of code 18 is when you press the button, the sewing feet are lifted,
       at this time, you release the button, sewing feet are immediately lowered onto the sewing materrial.

.. [#] The function of code 1 is when you press the button, the machine sews backwards,
       at this time, you release the button, it sews forwards.

       The function of code 24 is when you press the button, the machine sews backwards, 
       at this time, you release the button, it still sews backwards, the press the button again,
       it sews forwards.

.. important::
  Functions with codes greater than 100 needs special input ports, such as analog.

How to setup the function of input ports?
=========================================

Follow the steps:

1. Confirm which port you need to modify, such as *Input-01* or *Input-02*.
   In this step, you need to know the specific model of the system you are using,
   then refer to its wiring diagram. Refer to the :ref:`input_params_quick_reference` 
   section of this chapter to find the parameter number that controls the function of 
   this port;
2. Refer to the section at the beginning of this chapter :ref:`input_mode_code_list`, 
   get the parameter value you need;
3. Modify the parameter obtained in step 1 to the function code obtained in step 2,
   then restart the system.

Let's take an example:

1. You want use the sixth key of the keypad to control the puller;
2. In parameter list, you find :option:`A41`, which controls the function:
   
      Mode Keypad-Key6 -- A 41 

3. See the section :ref:`input_mode_code_list`, *20* is code of puller function, 
   then change :option:`A41` to 20:

      20 = Toggle puller raise up/down

.. _input_params_quick_reference:

Quick reference
===============

This table summarizes which parameter should be used for input configuration:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Mode Keypad-Key1                                     Technician :option:`A36`
Mode Keypad-Key2                                     Technician :option:`A37`
Mode Keypad-Key3                                     Technician :option:`A38`
Mode Keypad-Key4                                     Technician :option:`A39`
Mode Keypad-Key5                                     Technician :option:`A40`
Mode Keypad-Key6                                     Technician :option:`A41`
Mode Keypad-Key7                                     Technician :option:`A68`
Mode Input-01                                        Technician :option:`A04`
Mode Input-02                                        Technician :option:`A05`
Mode Input-03                                        Technician :option:`A81`
Mode Input-04                                        Technician :option:`A82`
Mode Input-05                                        Technician :option:`A83`
Mode Input-06                                        Technician :option:`A84`
Mode Input-07                                        Technician :option:`A85`
Mode Input-08                                        Technician :option:`A86` 
Mode Input-09                                        Technician :option:`A87`
Mode Input-10                                        Technician :option:`A88`
==================================================== ========== ==============

Parameter List
==============

.. option:: A36
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key1

.. option:: A37
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key2

.. option:: A38
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key3

.. option:: A39
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key4

.. option:: A40
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key5

.. option:: A41
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key6

.. option:: A68
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key7

.. option:: A04
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-01

.. option:: A05
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-02

.. option:: A81
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-03

.. option:: A82
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-04

.. option:: A83
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-05


.. option:: A84
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-06

.. option:: A85
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-07

.. option:: A86
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-08  

.. option:: A87
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-09

.. option:: A88
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-10
