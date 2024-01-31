.. _input_configuration:

===================
Input configuration
===================

Input Mode Code List
=====================

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

**How to setup the function of input ports?**:

Follow the steps:

1. Confirm which port you need to modify, such as Input-01 or Input-02.
   In this step, you need to know the specific model of the system you are using,
   then refer to its wiring diagram. Refer to the `Parameter List`_ section 
   of this chapter to find the parameter number that controls the function of 
   this port.
2. Refer to the table at the beginning of this chapter `Input Mode Code List`_, 
   get the parameter value you need.
3. Modify the parameter obtained in step 1 to the function code obtained in step 2,
   then restart the system.

Let's take an example:

Step1: You want use the sixth key of the keypad to control the puller;

Step2: In parameter list, you find *A41*, which controls the function;

   A41: Mode Keypad-Key6

Step3: In the input model code List, *20* is code of puller function;

   20 = Toggle puller raise up/down

Then change A41 to 20.

Parameter List
==============

A 04
----

.. dropdown:: Mode Input-01 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-01

A 05
----

.. dropdown:: Mode Input-02 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-02

A 36
----

.. dropdown:: Mode Keypad-Key1 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key1

A 37
----

.. dropdown:: Mode Keypad-Key2 <...> 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key2

A 38
----

.. dropdown:: Mode Keypad-Key3 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key3

A 39
----

.. dropdown:: Mode Keypad-Key4 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key4

A 40
----

.. dropdown:: Mode Keypad-Key5 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key5

A 41
----

.. dropdown:: Mode Keypad-Key6 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key6

A 68
----

.. dropdown:: Mode Keypad-Key7 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Keypad-Key7

A 81
----

.. dropdown:: Mode Input-03 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-03

A 82
----

.. dropdown:: Mode Input-04 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-04

A 83
----

.. dropdown:: Mode Input-05 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-05


A 84
----

.. dropdown:: Mode Input-06 <...> 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-06

A 85
----

.. dropdown:: Mode Input-07 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-07

A 86
----

.. dropdown:: Mode Input-08 <...> 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-08  


A 87
----

.. dropdown:: Mode Input-09 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-09

A 88
----

.. dropdown:: Mode Input-10 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function definition of Input-10
