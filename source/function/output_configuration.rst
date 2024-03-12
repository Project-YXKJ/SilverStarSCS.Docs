.. _output_configuration:

====================
Output configuration
====================

Output Mode Code List
=====================

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
  
  .. _15:
  
  - 15 = Puller；
  - 16 = Thread wiper(lower).

**How to setup the function of output ports?**:

Follow the steps:

1. Confirm which output port is connected to the solenoid valve, like output-07 or output-06. 
   In this step, you need to know the specific model of the system you are using, then refer
   to its wiring diagram. Refer to the `Parameter List`_ section of this chapter to find 
   the parameter number that controls the function of this port.
2. Refer to the table at the beginning of this chapter `Output Mode Code List`_, 
   get the parameter value you need.
3. Modify the parameter obtained in step 1 to the function code obtained in step 2,
   then restart the system.

Let's take an example:


You want set the function of **Output-01** to the puller. In the parameter list
you will find `A 71`_, which controls the function of **Output-01**. In the input model
code List, 15_ is code of puller function, then change A71 to 15.


Parameter List
==============

A 71
----

.. dropdown:: Mode Output-01 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-01

A 72
----

.. dropdown:: Mode Output-02 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-02    

A 73
----

.. dropdown:: Mode Output-03 <...>
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-03

A 74
----

.. dropdown:: Mode Output-4 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-04

A 75
----

.. dropdown:: Mode Output-05 <...>
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-05


A 76
----

.. dropdown:: Mode Output-06 <...>
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-06

A 77
----

.. dropdown:: Mode Output-07 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-07

A 78
----

.. dropdown:: Mode Output-08 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-08

A 79
----

.. dropdown:: Mode Output-09 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-09

A 80
----

.. dropdown:: Mode Output-10 <...> 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-10
