.. _assemble:

========
Assemble
========

.. attention::
   If certain parameters in this category are set incorrectly, 
   the machine may have unexpected problems.

Quick reference
===============

This table summarizes which parameter should be used for assemble:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Lock the Shortkeys                                   Developer  :option:`A07`
Function POSITION -1                                 Developer  :option:`A19` 
MACHINE ID                                           Developer  :option:`O03` 
Pedal Type                                           Developer  :option:`O08` 
Machine ID Storage Location                          Developer  :option:`O30` 
Pedal Calibration:POSITION END(Forward)              Developer  :option:`O56`
Pedal Calibration:POSITION 2 and POSITION 1          Developer  :option:`O57`
Pedal Calibration:POSITION 1 and POSITION 0          Developer  :option:`O58`
Pedal Calibration:POSTIION 0 and POSTIION -1         Developer  :option:`O59`
Pedal Calibration:POSTIION -1 and POSTIION -2        Developer  :option:`O60`
Pedal Calibration:POSITION END(Backward)             Developer  :option:`O61`
Pedal Calibration:Schmitt Loop value                 Developer  :option:`O62`
Speed Curve Pedal                                    Developer  :option:`O63`
Keypad Type                                          Developer  :option:`O80`
==================================================== ========== ==============

Parameter List
==============

.. option:: A07

   -Max  1  
   -Min  0
   -Unit  --
   -Description
     | To avoid the very thick material from triggering the shortkeys:
     | 0 = Off;
     | 1 = On.

.. option:: A19
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  
     | When pedal at :term:`POSITION -1` 
       which funcition is activared:
     | 1 = Sewing foot lift;
     | 2 = Thread trim.

.. option:: O03
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  :term:`MACHINE ID`

.. option:: O08
   
   -Max  2
   -Min  1
   -Unit  --
   -Description
     | Choice between an native and standing operation pedal:
     | 0 = Native;
     | 1 = Standing Operation Pedal.

.. option:: O30
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  
     | Choose where :term:`MACHINE ID` 
       is stored:
     | 1 = Stored in the controller;
     | 2 = Stored in the machine head

.. option:: O56
    
    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value by step forwards the pedal to the end position, value > O57

.. option:: O57

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSITION 2 and POSITION 1, O56 < value < O58

.. option:: O58

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSITION 1 and POSITION 0, O57 < value < O59

.. option:: O59

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSTIION 0 and POSTIION -1, O58 < value < O60

.. option:: O60

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSTIION -1 and POSTIION -2, O59 < value < O61

.. option:: O61

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value by step forwards the pedal to the end position,value < O60. 

.. option:: O62

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the schmitt loop.

.. option:: O63

   -Max  4095  
   -Min  0
   -Unit  --
   -Description
     | 0 = linear;
     | 1 = 2 lines;
     | 2 = Curve(start slowly,end fast);
     | 3 = Curve(start fast,end slowly);
     | 4 = S curve(start slowly,middle fast,end slowly);
     | 5 = S curve(start fast,middle slowly,end fast).

.. option:: O80

   -Max  3  
   -Min  1
   -Unit  --
   -Description
     | Type of the keypad:
     | 1 = 6 keys;
     | 2 = 7 keys;
     | 3 = 12 keys.
