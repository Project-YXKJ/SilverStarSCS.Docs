.. _input_configuration:

===================
Input configuration
===================

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

P00
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.
     

| A04 | 199 | 0 | - | Function Input-01:<br>0 = No function;<br>1 = Manual bartack;<br>2 = Forward correction;<br>3 = Backward correction;<br>4 = Forward correction at stop, reverse at running;<br>5 = Backward correction at stop, reverse at running;<br>6 = Quick toggle stroke;<br>7 = Enable/unable bartack at seam start/end;<br>8 = Second stitch length;<br>9 = Additional thread tension;<br>10 = Pause;<br>11 = Thread a needle;<br>12 = Toggle seam center guide raise up/down;<br>13 = Tilt switch;<br>14 = Up thread broken sensor;<br>15 = Eye protection sensor;<br>16 = Hook cover missing sensor;<br>17 = Toggle sewing foot lifter raise up/down;<br>18 = lifting sewing foot via the knee switch;<br>19 = Oil Starvation;<br>20 = Toggle puller raise up/down;<br>100 = Sewing foot stroke knob potentiometer;<br>101 = Sewing foot height sensor; |
| A05 | 199 | 0 | - | Function of input-02, refer to A04 |
| A36 | 199 | 0 | - | Function of keypad key-01, refer to A04 |
| A37 | 199 | 0 | - | Function of keypad key-02, refer to A04 |
| A38 | 199 | 0 | - | Function of keypad key-03, refer to A04 |
| A39 | 199 | 0 | - | Function of keypad key-04, refer to A04 |
| A40 | 199 | 0 | - | Function of keypad key-05, refer to A04 |
| A41 | 199 | 0 | - | Function of keypad key-06, refer to A04 |
| A68 | 199 | 0 | - | Function of keypad key-07, refer to A04 |
| A81 | 199 | 0 | - | Function of input-03, refer to A04 |
| A82 | 199 | 0 | - | Function of input-04, refer to A04 |
| A83 | 199 | 0 | - | Function of input-05, refer to A04 |
| A84 | 199 | 0 | - | Function of input-06, refer to A04 |
| A85 | 199 | 0 | - | Function of input-07, refer to A04 |
| A86 | 199 | 0 | - | Function of input-08, refer to A04 |
| A87 | 199 | 0 | - | Function of input-09, refer to A04 |
| A88 | 199 | 0 | - | Function of input-10, refer to A04 |
