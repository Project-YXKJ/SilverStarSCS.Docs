.. _output_configuration:

====================
Output configuration
====================

Output ports allow the controller to to drive components on the machine.
These components mainly include various types of electromagnets and 
solenoid valves.

The mode of each output is flexible. In most cases, you can freely configure 
the mode of each port according to your actual wiring.

.. attention::
   Make sure that two output ports are not configured for the same mode.
   
   Depending on the model, some mode may not be available.

.. _output_mode_code_list:

Output Mode Code List
=====================

Here is the output mode code list:

- 0 = No function;
- 1 = Thread cutter;
- 2 = Thread tension;
- 3 = Thread clamp;
- 4 = Reverse;
- 5 = Sewing foot lifter;
- 6 = Stroke;
- 7 = Additional thread tension;
- 8 = Thread wiper(upper);
- 9 = Second stitch length;
- 10 = Needle cooling;
- 11 = Additional cutter for short thread cutter machine;
- 12 = Seam center guide;
- 13 = Zero stitch length for short thread cutter machine;
- 14 = Auto corner for 2-needle machine;
- 15 = Puller；
- 16 = Thread wiper(lower).

How to setup the function of output ports?
==========================================

Follow the steps:

1. Confirm which output port is connected to the solenoid valve, like *Output-07* 
   or *Output-06*. In this step, you need to know the specific model of the system
   you are using, then refer to its wiring diagram. Refer to the `Quick reference`_ 
   section of this chapter to find the parameter number that controls the function
   of this port.
2. Refer to the section at the beginning of this chapter :ref:`output_mode_code_list`, 
   get the parameter value you need.
3. Modify the parameter obtained in step 1 to the function code obtained in step 2,
   then restart the system.

Let's take an example:

1. You want set the function of *Output-01* to the puller;
2. In the parameter list you will find :option:`A 71`, which controls the function
   of *Output-01*::

      A71: Mode Output-01

3. See the section :ref:`output_mode_code_list`, 15 is code of puller function,
   then change :option:`A 71` to 15::
   
      15 = Puller;

Quick reference
===============

This table summarizes which parameter should be used for output configuration:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Mode Output-01                                       Technician :option:`A 71`
Mode Output-02                                       Technician :option:`A 72` 
Mode Output-03                                       Technician :option:`A 73`
Mode Output-04                                       Technician :option:`A 74`
Mode Output-05                                       Technician :option:`A 75`
Mode Output-06                                       Technician :option:`A 76`
Mode Output-07                                       Technician :option:`A 77`
Mode Output-08                                       Technician :option:`A 78`
Mode Output-09                                       Technician :option:`A 79`
Mode Output-10                                       Technician :option:`A 80` 
==================================================== ========== ==============

Parameter List
==============

.. option:: A 71
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-01

.. option:: A 72
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-02    

.. option:: A 73

   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-03

.. option:: A 74
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-04

.. option:: A 75
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-05


.. option:: A 76
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-06

.. option:: A 77
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-07

.. option:: A 78
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-08

.. option:: A 79
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-09

.. option:: A 80
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-10
