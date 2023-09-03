.. _input_configuration:

===================
Input configuration
===================

Input Mode Code List:

- 0 = No function
- 1 = Manual bartack
- 2 = Forward correction;
- 3 = Backward correction  
- 4 = Forward correction at stop, reverse at running
- 5 = Backward correction at stop, reverse at running
- 6 = Quick toggle stroke
- 7 = Enable/unable bartack at seam start/end
- 8 = Second stitch length
- 9 = Additional thread tension
- 10 = Pause
- 11 = Thread a needle
- 12 = Toggle seam center guide raise up/down
- 13 = Tilt switch
- 14 = Up thread broken sensor
- 15 = Eye protection sensor
- 16 = Hook cover missing sensor
- 17 = Toggle sewing foot lifter raise up/down
- 18 = lifting sewing foot via the knee switch
- 19 = Oil Starvation;
- 20 = Toggle puller raise up/down;
- 100 = Sewing foot stroke knob potentiometer
- 101 = Sewing foot height sensor

.. important::
  Functions with codes greater than 100 needs an analog port.

**How to setup the function of input ports**:

follow the steps:

- Confirm which input port is connected to the switch, keypad, sensor etc, like input-07 or input-06. In this step, you need to know the specific model of the system you are using, then refer to its wiring diagram.
- Refer to the table at the beginning of this chapter, get the parameter value you need.
- Restart the system

Let's take an example:

For example, you want use the sixth key of the keypad to control the puller, you need to set the function of **Keypad-Key06** to puller, that is, **A41** is set to 20 (20 is code of function switch the state of puller).


Parameter List
==============

A04
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function Input-01

A05
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function Input-02

A36
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-01

A37
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-01

A38
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-01

A39
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-01

A40
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-01

A41
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-01

A68
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function keypad key-07

A81
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03

A82
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03

A83
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03


A84
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03

A85
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03

A86
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03   


A87
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03

A88
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  Function input-03
